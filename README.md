# AI Customer Support

**Automate the customer support of an e-commerce company with Gmail, Supabase, and Anthropic models through Pydantic AI, then deploy it with Docker on your own VPS.**

This project automates the entire customer support of an e-commerce company. A backend checks a Gmail inbox, an AI pipeline reads each email, searches a knowledge base, and then replies or hands the email to a person. It runs on your own server, and nothing on that server is reachable from the internet except SSH from your IP address.

---

## How it works

```
 Gmail inbox ──► Backend (FastAPI) ──► AI pipeline (Pydantic AI + Claude)
                                            │
                          ┌─────────────────┼─────────────────┐
                          ▼                 ▼                 ▼
                   Classify email    Search knowledge    Decide: reply
                                     base (Supabase)     or hand to a human
```

1. **Poll Gmail** – the backend checks the support inbox on a schedule.
2. **Read and classify** – a fast model classifies each incoming email.
3. **Search the knowledge base** – an agent looks up answers in Supabase (Postgres).
4. **Reply or escalate** – the agent either replies automatically or hands the email to a person.
5. **Monitor** – a password-protected dashboard shows what the system is doing.

## Tech stack

| Layer | Tool |
| --- | --- |
| Backend | [FastAPI](https://fastapi.tiangolo.com/) |
| AI framework | [Pydantic AI](https://ai.pydantic.dev/) |
| Models | Anthropic Claude (Haiku for classification, Sonnet for the agent) |
| Email | Gmail API |
| Database / knowledge base | Supabase (Postgres) |
| Evals | pydantic-evals |
| Deployment | Docker on your own VPS |

## Security

The server is locked down. Nothing on it is reachable from the internet except **SSH from your IP address**.

## Getting started

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- A Gmail account with API access
- A Supabase project
- An Anthropic API key

### Install

```bash
git clone https://github.com/parsimeikoikai/ai-customer-support.git
cd ai-customer-support
uv sync
```

### Configure

Copy the example environment file and fill in your values:

```bash
cp .env.example .env
```

| Variable | Description |
| --- | --- |
| `GOOGLE_CLIENT_ID` | Google OAuth client ID |
| `GOOGLE_CLIENT_SECRET` | Google OAuth client secret |
| `GOOGLE_REFRESH_TOKEN` | Refresh token for the support inbox |
| `DATABASE_URL` | Supabase Postgres connection string |
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `CLASSIFIER_MODEL` | Model used to classify emails (default `anthropic:claude-haiku-5-5`) |
| `AGENT_MODEL` | Model used by the support agent (default `anthropic:claude-sonnet-5-5`) |
| `POLL_INTERVAL_SECONDS` | How often to check the inbox (default `30`) |
| `DASHBOARD_USERNAME` | Dashboard login username (default `admin`) |
| `DASHBOARD_PASSWORD` | Dashboard login password |

> Never commit your `.env` file. It is listed in `.gitignore`.

### Run locally

```bash
uv run fastapi dev app/main.py
```

- API: http://127.0.0.1:8000
- Docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Project structure

```
ai-customer-support/
├── app/
│   ├── config.py      # Settings loaded from environment variables
│   └── main.py        # FastAPI application
├── .env.example       # Environment variable template
├── pyproject.toml     # Dependencies
└── README.md
```

## License

Add a license of your choice.
