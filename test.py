import unittest
import utils


class TestUtils(unittest.TestCase):
    # Test that creating a ticket results in an object with the correct keys and values
    def test_create_ticket(self):
        ticket = utils.create_ticket("bot_123", {"gpt_key": 123})
        self.assertDictEqual(
            ticket,
            {
                "ticket_id": ticket["ticket_id"],
                "bot_id": "bot_123",
                "status": "open",
                "gpt_key": 123
            }
        )

    # Test that a correctly formed GPT response doesn't return an error when validating
    def test_valid_gpt_response(self):
        error = utils.validate_gpt_response({
            "ticket_id": "c467afb2-0dcc-45fe-beac-80c503a04f86",
            "bot_id": "bot-123",
            "status": "open",
            "problem_location": "Los Angeles, California",
            "problem_type": "hardware",
            "summary": "The bot broke today due to a hardware malfunction."
        })
        self.assertIsNone(error)


if __name__ == '__main__':
    unittest.main()
