from django.shortcuts import render

import mutagen

from .serializers import *

from .models import *

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

import re

from django.db.models import F

from django.db.models import Q

# Create your views here.

class SongAPI(APIView):

	'''
		1. Create an api to upload audio file and the extension of audio file is mp3 , wav , wma , amr and it also
		   show you the metadata of audio file as a response

	'''

	def post(self,request):
		serializer = SongSerializer(data=request.data)
		# mutagen is a python library it is used for getting the metadata of any file
		getFile = mutagen.File(request.data['file'],easy=True)
		if serializer.is_valid():
			serializer.save()
			Serializer_list = [serializer.data,getFile]
			content = {
	        'status': 1, 
	        'responseCode' : status.HTTP_200_OK, 
	        'data': Serializer_list,
	        }
			return Response(content['data'], status=status.HTTP_201_CREATED)
		return Response('Allowed extensions are: mp3, wav, wma, amr.',status=status.HTTP_400_BAD_REQUEST)



	'''
		2. Delete the data by passing extension of audio file and id of audio file

		   requirement : 
		   				1. both extension type and id have to match to delete the file
		   				2. if it is not matching it will raise an error with 400 Bad request
	'''

	def delete(self,request,gettype,pk):
		getSong = Song.objects.get(id=pk)
		pattern = r"[.]"
		getList = re.split(pattern, str(getSong))
		if gettype in getList:
			getSong.delete()
			return Response({"Message": "Song Deleted"},status = status.HTTP_200_OK)
		else:
			return Response({"Error" : "This Filetype is not present with that id"},status=status.HTTP_400_BAD_REQUEST)


	'''
		3. we use get method to fetch tha data from server

	       First i am checking what user want 
	       1. user want to get all objects what he has requested for
	       	  Note : user only give you the extension name like mp3 , wav ,wma ,amr
	       2. user want particular data
	       	  Note : in this case he will pass extension name and id
	       	  if it is matching it will give you the output as a response
	       	  otherwise it will raise an error that extension and id is not matching in database with status of 400 bad request

	'''

	def get(self,request,gettype,pk=None):
		if pk == None:
			getFiltered = Song.objects.filter(Q(file__iendswith=(gettype)))
			serializer = SongSerializer(getFiltered,many=True)
			return Response(serializer.data,status = status.HTTP_200_OK)
		else:
			try:
				getSong = Song.objects.get(id=pk)
			except:
				return Response({"Error" : "This ID is not present in the database"})
			pattern = r"[.]"
			getList = re.split(pattern, str(getSong))
			serializer = SongSerializer(getSong)
			if gettype in getList:
				return Response(serializer.data)
			else:
				return Response({'error' : 'This audiotype file is note present with that id'},status=status.HTTP_400_BAD_REQUEST)


	'''
		4. we use put method to update existing object.

		   user will pass extension name and id
		   note : user only give you the extension name like mp3 , wav ,wma ,amr 
		   if it is matching user will update that particular object that he has requested for
		   otherwise it will raise an error that extension name with that id is not present in database with status of 400 bad request
	'''


	def put(self,request,gettype,pk):
		getSong = Song.objects.get(id=pk)
		pattern = r"[.]"
		getList = re.split(pattern, str(getSong))
		if gettype in getList:
			serializer  = SongSerializer(getSong, data = request.data)
			if serializer.is_valid():
				serializer.save()
				return Response({"Message": "Song Updated"})
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({"Error" : "This Filetype is not present with that id"},status=status.HTTP_400_BAD_REQUEST)












