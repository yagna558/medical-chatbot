import os


def require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or not value.strip():
        raise RuntimeError(
            f"Missing required environment variable: {name}. "
            f"Add it to your .env file or environment before starting the app."
        )
    return value
