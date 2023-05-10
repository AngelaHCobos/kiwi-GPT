import json
import uuid
import openai
import typing


# Create a new ticket object
def create_ticket(bot_id: str, gpt_response: typing.Dict) -> typing.Dict:
    return {
        "ticket_id": str(uuid.uuid4()),  # Generate a new id for this ticket
        "bot_id": bot_id,
        "status": "open",
        **gpt_response  # Expand info obtained from GPT
    }


# Validate that the GPT response has the correct structure and types
def validate_gpt_response(response: typing.Dict) -> str | None:
    try:
        if type(response["problem_location"]) != str:
            return "Invalid failure location"
        if type(response["problem_type"]) != str or response["problem_type"] not in ["hardware", "software", "field"]:
            return "Invalid problem type"
        if type(response["summary"]) != str:
            return "Invalid summary"
    except KeyError:
        return "missing field"
    return None


# Send a prompt to GPT and try to parse the response as JSON
def parse_report(report: str) -> typing.Dict | None:
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt='''Consider the following report:
```
        '''
        + report +
        '''
```
Put this message in the following JSON structure
{
  "problem_location": "string",
  "problem_type": "hardware" | "software" | "field"
  "summary": "string"
}
''',
        temperature=0,
        max_tokens=100
    )
    try:
        return json.loads(res.choices[0].text)
    except json.JSONDecodeError:
        return None
