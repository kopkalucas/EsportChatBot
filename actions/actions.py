# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import random


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
    

class ActionDisplayEsportCompetitions(Action):
    def name(self):
        return 'action_display_esport_competitions'

    def run(self, dispatcher, tracker, domain):
        

        with open('./data/esport_competitions.json') as json_file:
            competitions = json.load(json_file)
        
        response = ""
        for i in competitions:
            response += f"Name: {i['name']}, Game: {i['game']}, Date: {i['date']}, Location: {i['location']}\n"
            
        
        dispatcher.utter_message(response)

        return []
    
class ActionProvideEsportNews(Action):
    def name(self):
        return 'action_provide_esport_news'

    def run(self, dispatcher, tracker, domain):

        with open('./data/esport_news.json') as json_file:
            news = json.load(json_file)
    
        chosen_news = random.choice(news)
        
        response = "Title: {}\nSource: {}\nDate: {}\nContent: {}".format(chosen_news["title"], chosen_news["source"], chosen_news["date"], chosen_news["content"])
                        
        dispatcher.utter_message(response)

        return []