# Kiwibot Bots, Orders and Reports API

API developed by Angela Haydee Cobos as an exercise for Kiwibot.

## Technologies used:

- Python 3.11
- Flask: API routes.
- GTP-3 davinci model: Natural language recognition.
- Unittest Python module: Unit tests.
- Git: Version control.

## How to run
### API
1. Clone the Git repository.
2. Create a .env file on the root of the project. You can use the .env.example file to see what environment variables are needed.
3. Run `flask --app main run` to run the API locally
### Tests
1. Run `python test.py` to run the tests locally.

## API Docs

### POST /heartbeat
Endpoint for bots to send status updates.

Body JSON:

```
{
    "bot_id": "string",
    "timestamp": "ISO 8601 Date",
    "location": {
        "lat": "float",
        "lon": "float"
    },
    "status": "available" | "busy" | "reserved",
    "battery_level": "float",
    "software_version": "string",
    "hardware_version": "string"
}
```

Respose codes: 
- 200: OK

### GET /heartbeat
Retrieves the last status of each bot.

Respose codes: 
- 200: OK

### GET /tickets/<ticket_id>
Retrieves the ticket with the given id.

Respose codes: 
- 200: OK
- 404: Ticket not found

### PATCH /tickets/<ticket_id>
Update the status of the ticket with the given id.

Body JSON:
```
{
    "status": "available" | "busy" | "reserved"
}
```

Respose codes: 
- 200: OK
- 400: Invalid status
- 404: Ticket not found

### POST /reports/<bot_id>
Endpoints for employees to send reports about problems with bots. A ticket is created and returned in the response.

Body Plaintext

Respose codes: 
- 200: OK
- 400: Failed to parse report

Response JSON:
```
{
    "ticket_id": "string",
    "problem_location": "string",
    "problem_type": "software" | "hardware" | "field",
    "summary": "string",
    "bot_id": "string",
    "status": "open" | "in progress" | "closed"
}
```




