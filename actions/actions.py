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
from rasa_sdk.events import SlotSet


class ActionSendEmail(FormAction):

    def name(self) -> Text:
        return "action_send_email"

    def required_slots():
        return ['username', 'email-address', 'phone-number']

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        username = tracker.get_slot("username")
        email_address = tracker.get_slot("email-address")
        phone_number = tracker.get_slot("phone-number")

        smtp_server = "smtp.gmail.com"
        port = 465
        sender_email_address = "rajendrareddy.akkala@gmail.com"
        receiver_email_address = "rajendra@syberzen.com"
        password = "Rajendra@11*#"

        message = "This message sent from chatbot user name is {}, email address is {} and phone number is {}".format(username, email_address, phone_number)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email_address, password)
            server.sendmail(sender_email_address, receiver_email_address, message)
        

        dispatcher.utter_message(template="utter_contact_you")

        return [SlotSet(username,None),
                SlotSet(email_address,None),
                SlotSet(phone_number,None)]
        