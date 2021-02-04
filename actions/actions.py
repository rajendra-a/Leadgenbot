# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import smtplib, ssl

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import Slotset


class ActionSendEmail(FormAction):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        username = tracker.get_slot("username")
        email_address = tracker.get_slot("email_address")
        phone_number = tracker.get_slot("phone-number")

        smtp_server = "smtp.syberzen.com"
        port = 465
        sender_email_address = "rajendra@syberzen.com"
        receiver_email_address = "rajendra@syberzen.com"
        password = "Rajendra@sz"

        message = f"This message sent from chatbot user name is {username},email address {email-address}\n and phone number {phone-number}"

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, receiver_email, message)
            server.sendmail(sender_email, receiver_email, message)
        

        dispatcher.utter_message(template="utter_contact_you")

        return []
