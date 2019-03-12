# -*- coding: utf-8 -*-
import pickle
import random
import io
from ast import literal_eval
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import socket


class Lan1Commands:
	def __init__(self, config):
		self.config = config
		self.wanted_intents = []  # For reacting only with wanted intents

	def set_alarm(self, intentmessage):
		response= "OK"
		return response
	def activate_object(self, intentmessage):
		if(len(intent_message.slots.object) >= 1):
			response = "OK"
		else:
			response = "Entschuldigung. Ich habe leider nicht Verstanden was ich anschalten soll."
		return response
	def deactivate_object(self, intentmessage):
		if(len(intent_message.slots.object) >= 1):			
			response = "OK"
		else:
			response = "Entschuldigung. Ich habe leider nicht Verstanden was ich ausschalten soll."
		return response


