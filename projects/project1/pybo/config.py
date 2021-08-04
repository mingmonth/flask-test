import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
#     os.path.join(BASE_DIR, 'pybo.db'))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test5555@localhost:3306/pybodb'

SQLALCHEMY_TRACK_MODIFICATIONS = False
