# Discord Agent

A small Python Discord bot project with two runnable versions:

- `discord_only.py`: Basic Discord bot that responds to the `$hello` command.
- `discord_only_plus_openai.py`: Discord bot that responds to `$hello` and can answer `$question ...` prompts using OpenAI.

## Requirements

- Python 3.10+
- A Discord bot token
- (Optional, for OpenAI version) An OpenAI API key

## Project Files

- `.env.example`: Example environment variables file
- `.env`: Your local secrets file (not committed)
- `requirements.txt`: Python dependencies
- `discord_only.py`: Basic bot entrypoint
- `discord_only_plus_openai.py`: OpenAI-enabled bot entrypoint

## Setup

1. Create and activate a virtual environment.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create your `.env` file from the example:

```bash
cp .env.example .env
```

If `cp` is not available on Windows PowerShell, use:

```powershell
Copy-Item .env.example .env
```

4. Fill in `.env` values:

```env
DISCORD_TOKEN=your_discord_bot_token_here
OPENAI_KEY=your_openai_api_key_here
```

- `DISCORD_TOKEN` is required for both bot versions.
- `OPENAI_KEY` is required only for `discord_only_plus_openai.py`.

## Run In GitHub Codespaces

Use this flow when working from a cloned repo in Codespaces.

1. Create a Codespace from the repository:
	- Open the repo on GitHub.
	- Select **Code** -> **Codespaces** -> **Create codespace on main**.

2. In the Codespaces terminal, create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create your `.env` file:

```bash
cp .env.example .env
```

5. Add your credentials to `.env`:

```env
DISCORD_TOKEN=your_discord_bot_token_here
OPENAI_KEY=your_openai_api_key_here
```

6. Start one of the bot versions:

```bash
python discord_only.py
```

or

```bash
python discord_only_plus_openai.py
```

Optional (recommended): store `DISCORD_TOKEN` and `OPENAI_KEY` as GitHub Codespaces secrets for the repo, then populate `.env` from those values inside the Codespace.

## Run

### Basic Discord bot

```bash
python discord_only.py
```

Commands:
- `$hello`

### Discord bot with OpenAI

```bash
python discord_only_plus_openai.py
```

Commands:
- `$hello`
- `$question your message here`

## Notes

- In the Discord Developer Portal, make sure your bot has the Message Content Intent enabled; this project reads message content.
- Keep `.env` private and never commit real tokens or keys.

## Troubleshooting

- `ModuleNotFoundError` for `discord`, `openai`, or `dotenv`:
	Install dependencies in the active environment with `pip install -r requirements.txt`.
- `LoginFailure` or bot does not start:
	Verify `DISCORD_TOKEN` in `.env` is correct and has no extra spaces/quotes.
- Bot is online but not responding to commands:
	Ensure Message Content Intent is enabled in Discord Developer Portal and your bot has permission to read/send messages in the channel.
- `OPENAI_KEY` errors when using `discord_only_plus_openai.py`:
	Confirm `OPENAI_KEY` is set in `.env` and your OpenAI account has API access.
- `IndexError` when using `$question` with no text:
	Use the command with content, for example: `$question What can you do?`.
