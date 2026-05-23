# medical-chatbot

## Project setup

Use the template script to create the initial project structure:

```bash
sh template.sh
```

This creates:

- `src/` for application code
- `research/` for notebooks and experiments
- `.env` for environment variables
- `setup.py`, `app.py`, `requirements.txt`, and `README.md`

## Run locally

1. Create and activate a virtual environment (optional but recommended)
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
python app.py
```

## Git commands

Clone the repository:

```bash
git clone https://github.com/yagna558/medical-chatbot.git
cd medical-chatbot
```

After opening the repository, create and activate a Conda environment:

```bash
conda create -n medical-chatbot python=3.11
conda activate medical-chatbot
pip install -r requirements.txt
```

Configure your Git identity once on this machine:

```bash
git config --global user.name "your-name"
git config --global user.email "your-email@example.com"
```

Check the current Git configuration:

```bash
git config --global user.name
git config --global user.email
```

Basic workflow:

```bash
git status
git add .
git commit -m "your commit message"
git push origin main
```

If you need to pull the latest changes:

```bash
git pull origin main
```

