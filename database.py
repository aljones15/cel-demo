from peewee import *

db = SqliteDatabase(":memory:")

class BaseModel(Model):
    class Meta:
        database = db

class ScheduledEvent(BaseModel):
    event_id: CharField(unique=True, index=True)
    state_date_time: DateTimeField(unique=True, index=True)
    duration: TimestampField()
    name: CharField()
    repeat: CharField()
    last_run: DateTimeField()
        
def init_db():
    db.connect()
    db.create_tables([ScheduledEvent])

init_db()
