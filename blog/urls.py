from django.urls import path
from .views import index, BlogList, BlogDetail
from django.conf.urls import url 

urlpatterns = [
	path("home/", index),
	path("blogs", BlogList.as_view()),
	path("blog_detail/<int:pk>/", BlogDetail.as_view()),
]