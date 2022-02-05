from django.db import models
import re
import bcrypt
from datetime import datetime

EMAIL_REGEX = re.compile(
    '^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')


class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        check = User.objects.filter(email=post_data['email'])
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        if len(post_data['password']) < 8:
            errors['password'] = "Password cannot be less than 8 characters."
        if len(post_data['email']) < 1:
            errors['reg_email'] = "Email address cannot be blank."
        elif not EMAIL_REGEX.match(post_data['email']):
            errors['reg_email'] = "Please enter a valid email address."
        elif check:
            errors['reg_email'] = "Email address is already registered."
        return errors

    def login_validator(self, post_data):
        errors = {}
        check = User.objects.filter(email=post_data['login_email'])
        if not check:
            errors['login_email'] = "Email has not been registered."
        else:
            if not bcrypt.checkpw(post_data['login_password'].encode(), check[0].password.encode()):
                errors['login_email'] = "Email and password do not match."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by=models.ManyToManyField("Game")
    objects = UserManager()


class GameManager(models.Manager):
     def create_validator(self, post_data):
         errors = {}
         if len(post_data['gameType']) < 2:
             errors['gameType'] = 'Game type  field should be at least 2 characters'
         if datetime.now(post_data['start'], ) < datetime.now():
            errors['start'] = ' Start time should be in the future'
         if datetime.now(post_data['end'],) > datetime.now():
            errors['end'] = ' End time should be in the future'
         if post_data['notes'] != '' and len(post_data['notes']) < 10:
            errors['notes'] = 'Notes should be at least 10 characters'
#         
# if len(form['network']) < 3:
#             errors['network'] = 'Network field should be at least 3 characters'
         return errors
# 
class Game(models.Model):
    gameType = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    start = models.TimeField (auto_now= True) 
    end = models.TimeField()
    location = models.CharField(max_length=255)
    notes = models.TextField(max_length=2500)
    creator = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = GameManager()
    def __str__(self):
        return f"Type of Game: {self.gameType}"
