from peewee import *

db = SqliteDatabase(":memory:")

class BaseModel(Model):
    class Meta:
        database = db

class ScheduledEvent(BaseModel):
    event_id = CharField(unique=True, index=True)
    start_date_time = DateTimeField(unique=True, index=True)
    duration = TimestampField(null=True)
    name = CharField()
    repeat = CharField(null=True)
    last_run = DateTimeField(null=True)
        
def init_db():
    db.connect()
    db.create_tables([ScheduledEvent])

init_db()
