curl -X POST http://127.0.0.1:8000/schedules -H 'Content-Type: application/json' -d '{"event_id":"urn:schedule:example","start_date_time":"2025-04-11T22:36:24.681Z","duration": 180000,"name":"Mow The Lawn","repeat":"Weekly-Thursday"}'

curl http://127.0.0.1:8000/schedules?id="urn:schedule:example"

curl -X PUT http://127.0.0.1:8000/schedules -H 'Content-Type: application/json' -d '{"event_id":"urn:schedule:example","start_date_time":"2025-04-11T22:36:24.681Z","duration":180000,"name":"Mow The Lawn 2","repeat":"Weekly-Monday"}'

curl -X DELETE http://127.0.0.1:8000/schedules?id="urn:schedule:example"

