from os import getenv
from rasa_sdk import Action
import requests as r


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
        sports_category = next(tracker.get_latest_entity_values("sports_category"), None)
        cooking_category = next(tracker.get_latest_entity_values("cooking_category"), None)
        category_entity = sports_category or cooking_category
        if category_entity:
            backend_host = getenv("BACKEND_API", "localhost")
            course_api = "http://" + backend_host + ":8080/api/course"
            response = r.get(course_api, params={"subcategory": category_entity})
            if response.status_code == 200:
                res = response.json()
                if res:
                    dispatcher.utter_template("utter_course_list", tracker, course_name=category_entity)
                else:
                    dispatcher.utter_template("utter_no_course_name", tracker, course_name=category_entity)
            else:
                dispatcher.utter_template("utter_server_wrong", tracker)
        else:
            dispatcher.utter_template("utter_no_course", tracker)
        return []
