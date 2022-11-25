import os
from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env


DB = PostgresEngine(config={
    "database": os.environ["DB_NAME"],
    "user":os.environ["POSTGRES_USER"],
    "password":os.environ["POSTGRES_PASSWORD"],
    "host":os.environ["DB_HOST"],
    "port":os.environ["DB_PORT"],
})


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=["testbot.piccolo_app"])
