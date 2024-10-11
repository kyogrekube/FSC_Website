# myapp/models.py

from django.db import models

"""
EXAMPLE OF HOW TO MAKE A TABLE:
class table_name(models.Model):
    name = models.CharField(max_length=100)   # This creates a VARCHAR column
    age = models.IntegerField()               # This creates an INTEGER column
    price = models.DecimalField(max_digits=10, decimal_places=2) # This creates a DECIMAL column

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'table_table'   # Explicitly set the table name
"""
class Chapter(models.Model):
    name = models.CharField(max_length=255)
    letters = models.CharField(max_length=10)  # Assuming Greek letters are short
    rush_chair = models.CharField(max_length=255)
    president = models.CharField(max_length=255)
    info = models.TextField(max_length=900)  # A 900 character info blob
    chapter_size = models.PositiveIntegerField()  # Non-negative integer
    def __str__(self):
        return self.name
