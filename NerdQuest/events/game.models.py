from django.db import models


class Game(models.Model):
    type = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    start = models.TimeField()
    end = models.TimeField()
    location = models.CharField(max_length=255)
    notes = models.TextField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Type of Show: {self.type}"

        # Validations to come this is just the beginning model to create the form ****kevin
