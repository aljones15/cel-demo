from sanic import Sanic, json
from helpers import load_settings
from database import ScheduledEvent, init_db
from playhouse.shortcuts import model_to_dict

app = Sanic("cel_server")
settings = load_settings("settings.yml")

@app.get(settings["server"]["routes"]["schedules"])
async def get_schedules(request):
    return json(list(ScheduledEvent.__dict__.keys()))
    if(request.args.get("id")):
        result = ScheduledEvent.get(ScheduledEvent.event_id == request.args.get("id"))
    if(request.args.get("after")):
        result = ScheduledEvent.get(
            ScheduledEvent.start_date_time >= request.args.get("after"))
    if(request.args.get("before")):
        result = ScheduledEvent.get(
            ScheduledEvent.start_date_time <= result.args.get("before"))
    return json(model_to_dict(result))

@app.post(settings["server"]["routes"]["schedules"])
async def create_schedules(request):
    result = ScheduledEvent(**request.json)
    result.save()
    return json(model_to_dict(result))

@app.put(settings["server"]["routes"]["schedules"])
async def updates_schedules(request):
    result = ScheduledEvent.update(**request.json).where(
        ScheduledEvent.event_id == request.json.id)
    return json(result)

@app.delete(settings["server"]["routes"]["schedules"])
async def delete_schedules(request):
    result = None
    if(request.args.get("id")):
        result = ScheduledEvent.delete(ScheduledEvent.event_id == request.args.get("id"))
    if(request.args.get("after")):
        result = ScheduledEvent.delete().where(
            ScheduledEvent.start_date_time >= request.args.get("after"))
    if(request.args.get("before")):
        result = ScheduledEvent.delete().where(
            ScheduledEvent.start_date_time <= request.args.get("before"))
    return json(result)

if __name__ == "__main__":
    # start server here
    app.run()
