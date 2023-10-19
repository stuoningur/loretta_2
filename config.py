import os

DEBUG = os.getenv("DEBUG", False)

if DEBUG:
    from pathlib import Path
    from dotenv import load_dotenv

    env_path = Path("./.env_debug")
    load_dotenv(env_path)
    from configs.dev import *
else:
    from configs.prod import *
