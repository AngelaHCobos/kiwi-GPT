from flask import Flask, request
import openai
import json
import utils
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# API key to connect to OPENAI GPT service
openai.api_key = os.environ["OPENAI_API_KEY"]

# Store tickets and heartbeats in memory
# In a real-world scenario this would be a database
tickets = {}
heartbeats = {}


# Routes definition

@app.post('/heartbeat')
def heartbeat_post():
    data = json.loads(request.data)

    heartbeats[data.bot_id] = data

    return 'Ok'


@app.get('/heartbeat')
def heartbeats_get():
    return heartbeats


@app.get('/tickets/<ticket_id>')
def ticket_get_by_id(ticket_id):
    ticket = tickets.get(ticket_id)
    if not ticket:
        return "ticket not found", 404
    return ticket


@app.patch('/tickets/<ticket_id>')
def ticket_update_by_id(ticket_id):
    ticket = tickets.get(ticket_id)
    data = json.loads(request.data)
    if not data.status or data.status not in ["open", "in progress", "closed"]:
        return "invalid status", 400
    if not ticket:
        return "ticket not found", 404

    # Update the ticket
    ticket = {
        **ticket,
        "status": data.status
    }
    tickets[ticket.ticket_id] = ticket

    return 'Ok'


@app.post('/reports/<bot_id>')
def report_post(bot_id: str):
    report = str(request.data)

    gpt_response = utils.parse_report(report)
    if not gpt_response:
        return "failed to parse report", 400

    error = utils.validate_gpt_response(gpt_response)
    if error:
        return error, 400

    return json.dumps(utils.create_ticket(bot_id, gpt_response))
