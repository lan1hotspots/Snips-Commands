#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
import io
from lan1commands import Lan1Commands

USERNAME_INTENTS = "lan1hotspots"

def user_intent(intentname):
    return USERNAME_INTENTS + ":" + intentname

def read_configuration_file(configuration_file):
    try:
        cp = configparser.ConfigParser()
        with io.open(configuration_file, encoding="utf-8") as f:
            cp.read_file(f)
        return {section: {option_name: option for option_name, option in cp.items(section)}
                for section in cp.sections()}
    except (IOError, configparser.Error):
        return dict()

def subscribe_intent_callback(hermes, intent_message):
    # conf = read_configuration_file(CONFIG_INI)
    intentname = intent_message.intent.intent_name
	if intentname == user_intent("Alarm"):
		result_sentence = shoppinglist.set_alarm(intent_message)
		hermes.publish_end_session(intent_message.session_id, result_sentence)
	elif intentname == user_intent("Aktivate_Object"):
		result_sentence = shoppinglist.activate_object(intent_message)
		hermes.publish_end_session(intent_message.session_id, result_sentence)
	elif intentname == user_intent("Deaktivate_Object"):
		result_sentence = shoppinglist.deactivate_object(intent_message)
		hermes.publish_end_session(intent_message.session_id, result_sentence)

if __name__ == "__main__":
    config = read_configuration_file("config.ini")
    lan1commands = Lan1Commands(config)
    with Hermes("localhost:1883") as h:
        h.subscribe_intents(subscribe_intent_callback).start()

