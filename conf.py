import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5535847652:AAFkR7zNSByPnkKx_nw0chq5zT95O1_esOk")

    APP_ID = int(os.environ.get("APP_ID", 4926633))

    API_HASH = os.environ.get("API_HASH", "be7b1d39ac5116d22701f8b6ac956785")

