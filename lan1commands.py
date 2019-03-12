# -*- coding: utf-8 -*-
import pickle
import random
import io
from ast import literal_eval
import datetime
import socket
import paho.mqtt.client as mqtt


class Lan1Commands:
  def __init__(self, config):
    self.config = config
    self.mqtt = mqtt.Client()
    self.mqtt.connect("localhost", 1883, 60)
    self.wanted_intents = []  # For reacting only with wanted intents

  def set_alarm(self, intentmessage):
    response= "OK"
    return response
  def activate_object(self, intentmessage):
    if(len(intent_message.slots.object) >= 1):
      str_object = str(intent_message.slots.object.first().value)
      if(len(intent_message.slots.object_location) >= 1):
        str_object_location = str(intent_message.slots.object_location.first().value)
      else:
        str_object_location = "default"      
      mqtt_topic = "{}/{}/{}".format(self.config['secret']['mqtt_path'] ,str_object_location, str_object)
      self.mqtt.public(mqtt_topic, 1)
      response = "OK"
    else:
      response = "Entschuldigung. Ich habe leider nicht Verstanden was ich anschalten soll."
    return response
  def deactivate_object(self, intentmessage):
    if(len(intent_message.slots.object) >= 1):      
      str_object = str(intent_message.slots.object.first().value)
      if(len(intent_message.slots.object_location) >= 1):
        str_object_location = str(intent_message.slots.object_location.first().value)
      else:
        str_object_location = "default"
      mqtt_topic = "{}/{}/{}".format(self.config['secret']['mqtt_path'] ,str_object_location, str_object)
      self.mqtt.public(mqtt_topic, 0)
      response = "OK"
    else:
      response = "Entschuldigung. Ich habe leider nicht Verstanden was ich ausschalten soll."
    return response


