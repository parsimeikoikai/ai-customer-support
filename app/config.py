from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load .env into the environment, so Pydantic AI also finds ANTHROPIC_API_KEY.
load_dotenv()


class Settings(BaseSettings):
    google_client_id: str
    google_client_secret: str
    google_refresh_token: str
    database_url: str
    classifier_model: str = "anthropic:claude-haiku-5-5"
    agent_model: str = "anthropic:claude-sonnet-5-5"
    poll_interval_seconds: int = 60
    # Only emails received within this many minutes are processed or answered.
    max_message_age_minutes: int = 60
    # Comma-separated sender addresses the bot may answer. Empty means everyone.
    allowed_senders: str = ""
    dashboard_username: str = "admin"
    dashboard_password: str = ""

    @property
    def allowed_sender_set(self) -> set[str]:
        return {a.strip().lower() for a in self.allowed_senders.split(",") if a.strip()}


settings = Settings()