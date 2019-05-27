from django.db import models
from datetime import datetime



class HandSituation(models.Model):

    hand_situation = models.CharField(max_length=200)
    situation_summary = models.CharField(max_length=200)
    situation_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Situations"

    def __str__(self):
        return self.hand_situation



class Hand(models.Model):
    hand_title = models.CharField(max_length=200)
    hand_content = models.TextField()
    hand_published = models.DateTimeField('date published', default=datetime.now())
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    hand_situation = models.ForeignKey(HandSituation, default=1, verbose_name="Situation", on_delete=models.SET_DEFAULT)
    hand_slug = models.CharField(max_length=200, default=1)


    def __str__(self):
        return self.hand_title
