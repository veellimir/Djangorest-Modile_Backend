import os

from dotenv import load_dotenv

load_dotenv()


CONFIG__SECRET_KEY = os.getenv("CONFIG__SECRET_KEY")
CONFIG__DEBUG = os.getenv("CONFIG__DEBUG")
CONFIG__PROJECT_DOMAIN_NAME = os.getenv("CONFIG__PROJECT_DOMAIN_NAME")

CONFIG__ROTATE_REFRESH_TOKENS = os.getenv("CONFIG__ROTATE_REFRESH_TOKENS")
CONFIG__BLACKLIST_AFTER_ROTATION = os.getenv("CONFIG__BLACKLIST_AFTER_ROTATION")