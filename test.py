import unittest
from app import handler, parse

class TestStringMethods(unittest.TestCase):
    def test_add_remove_item(self):
        # first addition
        parameter = {
            "item": "apple"
        }
        result = handler("item.add", parameter)
        expected = [
            "apple"
        ]
        self.assertEqual(result, expected)

        # second addition
        parameter = {
            "item": "apple"
        }
        result = handler("item.add", parameter)
        expected = [
            "apple",
            "apple"
        ]
        self.assertEqual(result, expected)

        # second addition
        parameter = {
            "item": "orange"
        }
        result = handler("item.add", parameter)
        expected = [
            "apple",
            "orange"
        ]
        self.assertEqual(result, expected)

        # third addition
        parameter = {
            "item": "apple"
        }
        result = handler("item.add", parameter)
        expected = [
            "apple",
            "apple",
            "orange"
        ]
        self.assertEqual(result, expected)

        # remotion
        parameter = {
            "item": "apple"
        }
        result = handler("item.remove", parameter)
        expected = [
            "orange"
        ]
        self.assertEqual(result, expected)

    def test_parse(self):
        request = """{
  "responseId": "8a360a4a-fd3c-4c3b-8ad5-097f93fb77af",
  "result": {
    "queryResult": 0.25462029225897354,
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            ""
          ]
        }
      }
    ],
    "languageCode": "en",
    "allRequiredParamsPresent": true,
    "intent": {
      "name": "projects/grocery-list/agent/intents/704ffd67-e157-4461-a2b9-9f7163750aa8",
      "displayName": "item add"
    },
    "action": "item.add",
    "parameters": {
      "item": "apple"
    },
    "queryText": "perform action"
  },
  "originalDetectIntentRequest": {
    "source": "DIALOGFLOW_CONSOLE",
    "payload": {}
  },
  "session": "projects/grocery-list/agent/sessions/f1bd0d72-bef4-4895-94c1-74e8a55bf8b8"
}
"""
        action, parameters = parse(request)
        self.assertEqual(action, "item.add")
        self.assertEqual(parameters, {"item": "apple"})

    def test_remove_item(self):
        # first addition
        parameter = {
            "item": "apple"
        }
        result = handler("item.add", parameter)
        expected = [
            "apple"
        ]
        self.assertEqual(result, expected)

        # second addition
        parameter = {
            "item": "orange"
        }
        result = handler("item.add", parameter)
        expected = [
            "apple",
            "orange"
        ]
        self.assertEqual(result, expected)

        # third addition
        parameter = {
            "item": "apple"
        }
        result = handler("item.add", parameter)
        expected = [
            "apple",
            "orange",
            "apple"
        ]
        self.assertEqual(result, expected)

        # remotion
        parameter = {
            "item": "apple"
        }
        result = handler("item.remove", parameter)
        expected = [
            "orange"
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
