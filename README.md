# Todo-auth# todo-auth

Simple Flask TODO-auth example project.

Getting started

1. Create and activate a virtual environment

On Windows (PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

On Git Bash / *nix shells:

```bash
python -m venv venv
source venv/Scripts/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app (development)

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

On Windows (PowerShell):

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run
```

Prepare for GitHub

- Initialize the repo locally, commit, then add a remote and push:

```bash
git init
git add .
git commit -m "Initial project"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

If your repo is created on GitHub already, replace the remote URL above. If you need me to push to a GitHub repository, provide the repository URL and tell me whether you want me to push (I cannot access your credentials, so I will provide the commands you can run locally if you prefer).

Notes

- There are existing files: `app.py`, `models.py`, and templates under `templates/`.
- To set a default LLM model for server configuration, add an environment variable `DEFAULT_MODEL=claude-haiku-4.5` (if you want me to add this to the repo's `.env` or configuration, tell me and I will prepare it).
