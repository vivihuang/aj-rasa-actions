from rasa_sdk import Action


class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in [
            "ask_weather",
            "ask_howdoing",
            "ask_howold",
            "ask_restaurant",
            "ask_time",
        ]:
            dispatcher.utter_template("utter_" + intent, tracker)
        return []
