# 🧮 Django Calculator Web App

<div align="center">
  <img src="calculator_app/static/img/m_d calc.jpg" alt="Calculator Screenshot" width="400">
  <p><em>Modern web calculator powered by Django</em></p>
</div>

---

## ✨ Features

| Feature              | Description                                                      |
|----------------------|------------------------------------------------------------------|
| **Operations**       | +, -, ×, ÷, parentheses, decimals                                |
| **UI/UX**            | Clean, responsive design with smooth animations                  |
| **Performance**      | AJAX-powered instant calculations (no page reloads)              |
| **Error Handling**   | Clear error messages for invalid expressions                     |
| **Keyboard Support** | Full support for mouse and keyboard input                        |

---

## 🛠️ Tech Stack

- **Backend:** Python 3.8+, Django 4.0+
- **Frontend:** Vanilla JavaScript, Modern CSS (Flexbox, Grid), Responsive design

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/Bunny-Developers/django-calculator.git
cd django-calculator

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📂 Project Structure

```
django-calculator/
├── calculator_app/         # Main application
│   ├── static/             # CSS, JS, images
│   ├── templates/          # HTML templates
│   └── [Django files]      # views.py, urls.py, etc.
├── calculator_project/     # Project config
├── .gitignore
├── requirements.txt
└── manage.py
```

---

## 🎮 Usage

- Click buttons or use your keyboard to enter expressions.
- Press `=` or `Enter` to calculate.
- Use `C` to clear, `DEL` to backspace.
- Supports complex expressions: `(5+3)*2/4`

---

## 🧑‍💻 Development in Visual Studio Code

### 1. Install VS Code & Extensions

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Django Template](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) (optional, for JS linting)

### 2. Recommended VS Code Settings

Create or update `.vscode/settings.json`:

```json
{
  "python.pythonPath": "venv/Scripts/python.exe",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "files.autoSave": "afterDelay",
  "emmet.includeLanguages": {
    "django-html": "html"
  }
}
```

### 3. Debugging Configuration

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": true
    }
  ]
}
```

### 4. Common Tasks

```bash
# Run tests
python manage.py test

# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

---

## 🧪 Frontend Development

For JavaScript linting/formatting:

```bash
npm init -y
npm install --save-dev eslint prettier
```

Create `.eslintrc.json`:

```json
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": ["eslint:recommended"],
  "parserOptions": {
    "ecmaVersion": 12
  },
  "rules": {}
}
```

---

## ⌨️ Useful VS Code Shortcuts

- <kbd>Ctrl</kbd>+<kbd>`</kbd> : Toggle terminal
- <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd> : Explorer view
- <kbd>Ctrl</kbd>+<kbd>,</kbd> : Open settings
- <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> : Search across files
- <kbd>F12</kbd> : Go to definition

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📜 License

MIT © [Hillary Okoth] — See [LICENSE](LICENSE) for details.

---

<div align="center"><sub>Built with ❤️ and Django</sub></div>
