from django.test import TestCase , Client 

from django.urls import reverse

from demo.models import *

from datetime import datetime

import json

class TestViews(TestCase):

	def SetUp(self):
		self.client = Client()

	def test_song_id_GET(self):
		response = self.client.get(reverse('songCrud',args = ['gettype','pk']))
		self.assertEqual(response.status_code,200)


	def test_song_all_GET(self):
		response = self.client.get(reverse('songCrud',args = ['gettype',None]))
		self.assertEqual(response.status_code,200)



	def test_song_add_POST(self):
		with open('E://techsolvo//techsolvo//media//audio/Jaane_Meri_Jaaneman_Bachpan_Ka_Pyar.mp3', 'rb') as fp:
			response = self.client.post('http://127.0.0.1:8000/song/',{'duration': 100, 'file': fp})
			self.assertEqual(response.status_code,201)


	def test_song_url_DELETE(self):
		response = self.client.delete(reverse('songCrud',kwargs = {'gettype':'mp3','pk':4}))
		self.assertEqual(response.status_code,200)

	def test_song_url_PUT(self):
		with open('E://techsolvo//techsolvo//media//audio/Jaane_Meri_Jaaneman_Bachpan_Ka_Pyar.mp3', 'rb') as fp:
			response = self.client.put(reverse('songCrud',kwargs = {'gettype':'mp3','pk':4}),{'file' : fp ,'duration' : 1000})
			self.assertEqual(response.status_code,415)