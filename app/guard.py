import time
from email.utils import parseaddr


def skip_reason(
    message: dict,
    headers: dict[str, str],
    own_address: str,
    max_age_minutes: int,
    allowed_senders: set[str] = frozenset(),
) -> str | None:
    """Return why the bot must not answer this message, or None when it may.

    allowed_senders: lowercase addresses the bot may answer; empty means everyone.
    """
    sender = parseaddr(headers.get("from", ""))[1].lower()
    if "SENT" in message.get("labelIds", []):
        return "sent by us"
    if sender == own_address.lower():
        return "from our own address"
    if allowed_senders and sender not in allowed_senders:
        return "sender not in allowed senders"
    auto_submitted = headers.get("auto-submitted", "no").strip().lower()
    if auto_submitted != "no":
        return f"auto-submitted: {auto_submitted}"
    if headers.get("precedence", "").strip().lower() in {"bulk", "list", "junk"}:
        return "bulk or list mail"
    # internalDate is when Gmail received the message, in epoch milliseconds.
    age_seconds = time.time() - int(message.get("internalDate", 0)) / 1000
    if age_seconds > max_age_minutes * 60:
        return f"older than {max_age_minutes} minutes"
    return None
