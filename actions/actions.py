# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from email import message
from re import template
from typing import Any, Text, Dict, List
from urllib import response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from mail import send_email
from rasa_sdk.events import SlotSet
from database_connectivity import DataUpdate
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionEmail(Action):

    def name(self) -> Text:
        return "action_subject_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_subject")

        return [SlotSet('email',tracker.latest_message['text'])]

class ActionSubject(Action):

    def name(self) -> Text:
        return "action_message_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_message")

        return [SlotSet('subject',tracker.latest_message['text'])]

class ActionMessage(Action):

    def name(self) -> Text:
        return "action_mail_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_send")

        return [SlotSet('message',tracker.latest_message['text'])]

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        email= tracker.get_slot("email")
        subject=tracker.get_slot("subject")
        message=tracker.get_slot("message")
        send_email(
        email,
        subject ,
        message)
            

        dispatcher.utter_message(text="We have sent you an email at {}".format(email))
        DataUpdate(tracker.get_slot("email"),tracker.get_slot("subject"),tracker.get_slot("message"))
        dispatcher.utter_message(text="Stored in database")
        return []
