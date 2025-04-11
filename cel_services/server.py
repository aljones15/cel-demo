from sanic import Sanic
from helpers import load_settings

app = Sanic("cel_server")
settings = load_settings("settings.yml")

def start():
    print("start")
