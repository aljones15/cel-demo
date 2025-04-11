from sanic import Sanic, json
from helpers import load_settings
from database import ScheduledEvent

app = Sanic("cel_server")
settings = load_settings("settings.yml")

print(settings)

@app.before_server_start
async def init_db():
    app.ctx.db = await start_db()

@app.get(settings["server"]["routes"]["schedules"])
async def get_schedules(request):
    return json({get: true})

@app.post(settings["server"]["routes"]["schedules"])
async def create_schedules(request):
    return json({post: true})

@app.put(settings["server"]["routes"]["schedules"])
async def updates_schedules(request):
    return json({put: true})

@app.delete(settings["server"]["routes"]["schedules"])
async def delete_schedules(request):
    return json({delete: true})

def start():
    print("start")
