import time
from slackclient import SlackClient
from translate import Translator
import json

translatorToFrench = Translator(to_lang="fr")
translatorToGerman = Translator(to_lang="de")
translatorToEnglish = Translator(to_lang="en")


if __name__ == "__main__":
    token='xoxp-19745829781-38048263175-38056115377-d6ad0242f9'
    sc = SlackClient(token)

    if sc.rtm_connect():
        while True:
            json_messages = sc.rtm_read()
            for message in json_messages:
                print("DEBUG: json message is: " + str(message))
                print("DEBUG: type is: " + message['type'])
                if (message['type'] == "message" and message['channel'] == 'C0NP34ZCG' and "group3botRyan" not in json.dumps(message)):
                    print("DEBUG: Actual message is: " + message['text'])
                    frenchTranslation = translatorToFrench.translate(message['text'])
                    print("DEBUG: Translated message to french is: " + frenchTranslation)
                    
                    englishTranslation = translatorToEnglish.translate(frenchTranslation)
                    print("DEBUG: Translated message to english is: " + englishTranslation)
                    #sc.api_call("chat.postMessage", channel="#group3", text=frenchTranslation, username="group3botRyan", icon_emoji=':robot_face:')
                    sc.api_call("chat.postMessage", channel="#group3", text=englishTranslation, username="group3botRyan", icon_emoji=':robot_face:')

                print("")
                print("")
                print("")

            time.sleep(1)
    else:
        print "Connection Failed, invalid token?"
