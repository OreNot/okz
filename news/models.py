from django.db import models

class News(models.Model):
    new_name = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.new_name