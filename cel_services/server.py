from sanic import Sanic, json
from helpers import load_settings
from database import ScheduledEvent

app = Sanic("cel_server")
settings = load_settings("settings.yml")

@app.get(settings["server"]["routes"]["schedules"])
async def get_schedules(request):
    if(request.json.id):
        result = ScheduledEvent.get(ScheduledEvent.id == request.json.id)
    if(request.json.after):
        result = ScheduledEvent.get(
            ScheduledEvent.start_date_time >= result.json.after)
    if(request.json.before):
        result = ScheduledEvent.get(
            ScheduledEvent.start_date_time <= result.json.after)
    return json(result)

@app.post(settings["server"]["routes"]["schedules"])
async def create_schedules(request):
    result = ScheduledEvent.create(request.json)
    return json(result)

@app.put(settings["server"]["routes"]["schedules"])
async def updates_schedules(request):
    result = ScheduledEvent.update(request.json).where(
        ScheduledEvent.id == request.json.id)
    return json(result)

@app.delete(settings["server"]["routes"]["schedules"])
async def delete_schedules(request):
    result = Null
    if(request.json.id):
        result = ScheduledEvent.delete(ScheduledEvent.id == request.json.id)
    if(request.json.after):
        result = ScheduledEvent.delete().where(
            ScheduledEvent.start_date_time >= result.json.after)
    if(request.json.before):
        result = ScheduledEvent.delete().where(
            ScheduledEvent.start_date_time <= result.json.after)
    return json(result)

if __name__ == "__main__":
    # start server here
    app.run()
