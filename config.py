import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mariadb+mariadbconnector://root:P%40%24%24w0rd@pup.qzz.io:3306/todo",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
