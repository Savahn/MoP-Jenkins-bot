# MoP-Jenkins-bot
Simple Utility bot for Mist of Pandaria information

## Installing dependencies
You must have Python 3.8 or higher installed on your machine

Create a virtual environment and activate it

```Bash
python -m venv .venv
.venv/Scripts/activate.bat
```

Install dependencies

```Bash
pip install poetry
poetry install
```

## Bot token
Rename, or copy, the .env.example file to .env and add your discord bot's token to this line (replace <TOKEN>)

```
BOT_TOKEN=<TOKEN>
```

## Running

Run the project locally

```Bash
poetry run python application.py
```

## Contributing

Have an idea of new funtionality to add? Add a [suggestion](https://github.com/Savahn/MoP-Jenkins-bot/issues) 
Want to try your hand at a new feature? Fork the [repo](https://github.com/Savahn/MoP-Jenkins-bot) and create a [pull request](https://github.com/Savahn/MoP-Jenkins-bot/pulls)