from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.http import Http404


# Home Page
def index(request):
	return render(request, "index.html")


#Blog List
class BlogList(APIView):
	def get(self, request, format=None):
		blog = Blog.objects.all()
		serializer = BlogSerializer(blog, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = BlogSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_404_BAD_REQUEST)

#BlogDetail
class BlogDetail(APIView):
	def get_object(self, pk):
		try:
			return Blog.objects.get(pk=pk)
		except Blog.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		blog = self.get_object(pk)
		serializer = BlogSerializer(blog)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		blog = self.get_object(pk)
		serializer = BlogSerializer(blog, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
	def delete(self, request, pk, format=None):
		blog = self.get_object(pk)
		blog.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)