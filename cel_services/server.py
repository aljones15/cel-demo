from sanic import Sanic, json
from helpers import load_settings
from database import ScheduledEvent, init_db
from playhouse.shortcuts import model_to_dict

app = Sanic("cel_server")
settings = load_settings("settings.yml")

# return model as json with string serializations for datetime
def model_response(model):
    return json(model_to_dict(model), default=str)

@app.get(settings["server"]["routes"]["schedules"])
async def get_schedules(request):
    if(request.args.get("id")):
        result = ScheduledEvent.get(ScheduledEvent.event_id == request.args.get("id"))
    if(request.args.get("after")):
        result = ScheduledEvent.get(
            ScheduledEvent.start_date_time >= request.args.get("after"))
    if(request.args.get("before")):
        result = ScheduledEvent.get(
            ScheduledEvent.start_date_time <= result.args.get("before"))
    return model_response(result)

@app.post(settings["server"]["routes"]["schedules"])
async def create_schedules(request):
    result = ScheduledEvent.create(**request.json)
    return model_response(result)

@app.put(settings["server"]["routes"]["schedules"])
async def updates_schedules(request):
    result = ScheduledEvent.update(**request.json).where(
        ScheduledEvent.event_id == request.json["event_id"])
    count = result.execute()
    return json({"updated": count})

@app.delete(settings["server"]["routes"]["schedules"])
async def delete_schedules(request):
    count = 0
    if(request.args.get("id")):
        count = ScheduledEvent.delete().where(
            ScheduledEvent.event_id == request.args.get("id")).execute()
    if(request.args.get("after")):
        count = ScheduledEvent.delete().where(
            ScheduledEvent.start_date_time >= request.args.get("after")).execute()
    if(request.args.get("before")):
        count = ScheduledEvent.delete().where(
            ScheduledEvent.start_date_time <= request.args.get("before")).execute()
    return json({"deleted": count})

if __name__ == "__main__":
    # start server here
    app.run()
