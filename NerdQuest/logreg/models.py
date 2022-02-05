from django.db import models
from events.models import Game
import re

# Create your models here.
class UserManager(models.Manager):
    def create_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First Name must be minimum of 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last Name must be minimum of 2 characters"
        if len(post_data['email']) < 6:
            errors['email'] = "email must be a minimum of 6 characters"
        if len(post_data['password']) < 6:
            errors['password'] = "Password must be a minimum of 6 characters"
        if len(post_data['password']) != len(post_data['confirm_pw']):
            errors['match'] = "Password and Password confirmation do not match"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['regex'] = "Email is in incorrect format"
        users_with_emails = User.objects.filter(email=post_data['email'])
        if len(users_with_emails) >= 1:
            errors['dup'] = "Email is taken, please use another"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # created_by = models.ForeignKey(Game, related_name='creator', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
 

# Create your models here.
