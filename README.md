This project uses [poetry](https://python-poetry.org/docs/) for dependency
management.

Install dependencies in a virtual environment:

```
poetry shell
poetry install
```

Copy .env.sample into a new .env file and add your credentials.

Run with [Chainlit](https://docs.chainlit.io):
```
chainlit run bot.py -w
```
