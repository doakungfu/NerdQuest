from django.db import models
from logreg.models import *
import re
import bcrypt
from datetime import datetime
class GameManager(models.Manager):
     def create_validator(self, post_data):
         errors = {}
         if len(post_data['gameType']) < 2:
             errors['gameType'] = 'Game type  field should be at least 2 characters'
        #  if datetime.now(post_data['start'], ) < datetime.now():
            # errors['start'] = ' Start time should be in the future'
        #  if datetime.now(post_data['end'],) > datetime.now():
            # errors['end'] = ' End time should be in the future'
        #  if post_data['notes'] != '' and len(post_data['notes']) < 10:
        #     errors['notes'] = 'Notes should be at least 10 characters'
#         
# if len(form['network']) < 3:
#             errors['network'] = 'Network field should be at least 3 characters'
         return errors
# 
# class Organizer(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     event =models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     # organized_by=models.ForeignKey(Game, related_name='creator', on_delete=models.CASCADE)
# 

class Game(models.Model):
    gameType = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    startTime = models.TimeField (auto_now= True) 
    endTime = models.TimeField(auto_now=False)
    location = models.CharField(max_length=255)
    notes = models.TextField(max_length=2500)
    # creator = models.ForeignKey(User, related_name="creator", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = GameManager()

    def __str__(self):
        return f"Type of Game: {self.gameType}"
