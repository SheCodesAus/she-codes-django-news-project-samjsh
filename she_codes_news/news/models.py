from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    class Meta:
        ordering = ['-pub_date'] #this has been added from 'class meta'

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(blank = True) #new addition from 'image_url'


    #add image function here and then add some 'logic' of the info related to images in 'views.py'
