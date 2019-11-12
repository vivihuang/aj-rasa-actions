from random import random
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


class ActionSearchCourse(Action):
    def name(self):
        return "action_search_course"

    def run(self, dispatcher, tracker, domain):
        if random() > 0.5:
            dispatcher.utter_template("utter_course_list", tracker)
        else:
            sports_category = next(tracker.get_latest_entity_values("sports_category"), None)
            cooking_category = next(tracker.get_latest_entity_values("cooking_category"), None)
            category_entity = sports_category or cooking_category
            if category_entity:
                dispatcher.utter_template("utter_no_course_name", tracker, course_name=category_entity)
            else:
                dispatcher.utter_template("utter_no_course", tracker)
        return []
