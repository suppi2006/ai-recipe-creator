# AI Recipe Creator 🍳

An AI-powered web application that generates recipe suggestions based on the ingredients provided by the user. It helps users discover recipe ideas and cooking instructions using artificial intelligence.

## Features

- Generate recipe ideas from available ingredients.
- Get AI-powered recipe suggestions.
- Simple and user-friendly web interface.
- Built using Python, Flask, and the Gemini API.

## Technologies Used

- Python
- Flask
- HTML and CSS
- Google Gemini API

## Project Structure

```text
AI_Recipe_Creator/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── templates/
├── static/
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-recipe-creator
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project folder and add your Gemini API key using the environment variable name expected by `app.py`.

Do not upload your actual `.env` file or API key to GitHub.

### 5. Run the application

```bash
python app.py
```

Open this address in your browser:

```text
http://127.0.0.1:5000
```

## Security

The Gemini API key is stored in an environment file and should not be shared publicly.

## Author

Created as a Python and AI learning project.
