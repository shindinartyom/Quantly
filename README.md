# Quantly

**Quantly** is a sleek, Django-powered web platform designed to streamline quantitative interview preparation. It allows users to post, solve, and track probability, statistics, and mathematics problems using automatic checking, including native fraction inputs.

## Features
- 📊 **Performance Dashboard**: Real-time tracking of personal accuracy, success rates, and attempt logs.
- 🔍 **Filtering System**: Dynamically search any question utilizing its multi-word Tag/Theme, Title, or Difficulty.
- 🎨 **Modern Aesthetics**: Built entirely around a dark-themed Glassmorphism aesthetic featuring neon accent gradients.

## Tech Stack
- **Backend Frame**: Python, Django 6.0.3
- **Frontend Form**: CSS3, Bootstrap 5.3 (Dark Layout)
- **Database**: SQLite3 (Local Configuration)

## Local Development Setup

**1. Activate your environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux (WSL)
source venv/bin/activate
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Apply the database framework**
```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Launch the application**
```bash
python manage.py runserver
```

> **Note**: Your local instance will bind to `http://127.0.0.1:8000/`.
