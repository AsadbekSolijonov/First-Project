from django.db import models


# Create your model here.
# News nomli jadval ustunlar (id, title, description, created)
class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField()
