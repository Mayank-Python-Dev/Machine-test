from django.test import SimpleTestCase
from django.urls import reverse , resolve
from demo.views import SongAPI



class testUrls(SimpleTestCase):


	def test_song_url_is_resolved(self):
		url =  reverse('song')
		print(resolve(url))
		self.assertEqual(resolve(url).func.view_class, SongAPI)


	def test_songcrud_url_is_resolved(self):
		url = reverse('songCrud',args = ['gettype','pk'])
		self.assertEqual(resolve(url).func.view_class, SongAPI)



	def test_getsong_url_is_resolved(self):
		url = reverse('getSong',args = ['gettype'])
		self.assertEqual(resolve(url).func.view_class, SongAPI)