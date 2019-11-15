from os import getenv
from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
import requests as r
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher


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
                    link = res[0]["hyperlinks"]
                    if link:
                        dispatcher.utter_template("utter_course_list_with_link", tracker, course_name=category_entity,
                                                  link=link)
                    else:
                        dispatcher.utter_template("utter_course_list", tracker, course_name=category_entity)
                else:
                    dispatcher.utter_template("utter_no_course_name", tracker, course_name=category_entity)
            else:
                dispatcher.utter_template("utter_server_wrong", tracker)
        else:
            dispatcher.utter_template("utter_no_course", tracker)
        return []


class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List["Event"]:
        dispatcher.utter_template("utter_out_of_scope", tracker)
        dispatcher.utter_template("utter_possibilities", tracker)
        return []


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List["Event"]:
        dispatcher.utter_template("utter_default", tracker)
        return [UserUtteranceReverted()]
