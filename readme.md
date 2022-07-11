# Bday-reminder 

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Sigmanificient/bday-reminder/badges/quality-score.png?b=mvp)](https://scrutinizer-ci.com/g/Sigmanificient/bday-reminder/?branch=mvp)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/corentin384/bday-reminder)
![GitHub repo size](https://img.shields.io/github/repo-size/corentin384/bday-reminder)
![Lines of code](https://img.shields.io/tokei/lines/github/corentin384/bday-reminder)
![GitHub](https://img.shields.io/github/license/corentin384/bday-reminder)
![GitHub last commit](https://img.shields.io/github/last-commit/corentin384/bday-reminder)

A Flask based application for birthday saving.


# Installation

Clone the repository
```bash
git clone https://github.com/Sigmanificient/bday-reminder.git
```

*If you are on GNU/Linux, you can use the makefile configuration*
```bash
make
```

Otherwise, you must install the dependencies manually.

- Install a python virtualenv (optional)
```bash
python -m venv venv
# Activate the virtualenv
```

- Install the bday_reminder package as editable
```bash
pip install -e .
```
- Install Sass cli tool
```bash
yarn install
```

- Build the static files
```bash
sass --style compressed bday_reminder/static/scss/style.scss:bday_reminder/static/css/style.css
```

- Run the application
```bash
python bday_reminder
```
