from django.urls import path
from .views import blog_list_views,details_list_views
urlpatterns = [
    path("",blog_list_views,name="blog_list_views"),
    path('blog/<int:id>/',details_list_views,name="details")
]