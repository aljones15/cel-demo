from peewee import *

db = SqliteDatabase(":memory:")

class ScheduledEvent(Model):
    event_id: TextField(unique=True, index=True)
    state_date_time: DateTimeField(unique=True, index=True)
    duration: TimestampField()
    name: CharField()
    repeat: CharField()
    last_run: DateTimeField()
    class Meta:
        database = db #use cel db
        
def init_db():
    db.connect()
    db.create_tables([ScheduledEvent])

init_db()
