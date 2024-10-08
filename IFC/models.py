from django.db import models

# Create your models here.
class Chapter(models.Model):
    name = models.CharField(max_length=255)
    letters = models.CharField(max_length=10)  # Assuming Greek letters are short
    rush_chair = models.CharField(max_length=255)
    president = models.CharField(max_length=255)
    info = models.TextField(max_length=900)  # A 900 character info blob
    chapter_size = models.PositiveIntegerField()  # Non-negative integer

    def __str__(self):
        return self.name