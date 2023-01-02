from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #homepage 'views.IndexView' is referenced in 'views.py' model
    path('<int:pk>/', views.StoryView.as_view(), name='story'), #int:pk is telling django to find the number of the primary key > referenced in 'views.py' under 'StoryView'
    path('add-story/', views.AddStoryView.as_view(), name='newStory') #find in 'views.py' under 'AddStoryView' > this is telling Django what you want the story to look like
    ]
