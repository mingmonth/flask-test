from dotenv import load_dotenv
from pathlib import Path

import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

DB_USER = os.getenv("DB_USER")
DB_PASSWD = os.getenv("DB_PASSWD")
DB_IP = os.getenv("DB_IP")
DB_PORT = os.getenv("DB_PORT")

# BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
#     os.path.join(BASE_DIR, 'pybo.db'))

# 사전에 database 미리 생성 필요
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWD}@{DB_IP}:{DB_PORT}/pybodb"

SQLALCHEMY_TRACK_MODIFICATIONS = False
