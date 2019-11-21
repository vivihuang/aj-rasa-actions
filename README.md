## aj-lithuania for Rasa actions
This is a repository showing an example bot and the setup needed to run it with Rasa.

## Steps to Setup Rasa actions with local mode

### Create virtual env with python3
use `python3 -m venv venv` or `python -m venv venv` to create venv

### Enable to use virtual env
use `source venv/bin/activate` to enable venv

### Upgrade pip if needed
`pip install --upgrade pip`

### Install dependencies
`pip install -r requirements.txt`

### Run actions
`make run`

## Steps to Setup Rasa actions with Docker

### Build docker image
`docker build . -t aj/lithuania`

### Run with docker
`docker run -d --name rasa-action-server -p 5055:5055 aj/lithuania`

## Test rasa actions connection

### Rasa actions api endpoint
`http://localhost:5055/webhook`

### Rasa actions api request body
```json
{
  "next_action": "string",
  "sender_id": "string",
  "tracker": {
    "conversation_id": "default",
    "slots": [
      {
        "slot_name": "slot_value"
      }
    ],
    "latest_message": {
      "entities": [
        {
          "start": 0,
          "end": 0,
          "value": "string",
          "entity": "string",
          "confidence": 0
        }
      ],
      "intent": {
        "confidence": 0.6323,
        "name": "greet"
      },
      "intent_ranking": [
        {
          "confidence": 0.6323,
          "name": "greet"
        }
      ],
      "text": "Hello!"
    },
    "latest_event_time": 1537645578.314389,
    "followup_action": "string",
    "paused": false,
    "events": [
      {
        "event": "slot",
        "timestamp": 1559744410
      }
    ],
    "latest_input_channel": "rest",
    "latest_action_name": "action_listen",
    "active_form": {
      "name": "restaurant_form"
    }
  },
  "domain": {
    "config": {
      "store_entities_as_slots": false
    },
    "intents": [
      {
        "property1": {
          "use_entities": true
        },
        "property2": {
          "use_entities": true
        }
      }
    ],
    "entities": [
      "person",
      "location"
    ],
    "slots": {
      "property1": {
        "auto_fill": true,
        "initial_value": "string",
        "type": "string",
        "values": [
          "string"
        ]
      },
      "property2": {
        "auto_fill": true,
        "initial_value": "string",
        "type": "string",
        "values": [
          "string"
        ]
      }
    },
    "templates": {
      "property1": {
        "text": "string"
      },
      "property2": {
        "text": "string"
      }
    },
    "actions": [
      "utter_greet",
      "utter_goodbye",
      "action_listen"
    ]
  }
}
```
