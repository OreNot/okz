from django.db import models

# Create your models here.
class Operatoranswers(models.Model):
    answer_title = models.CharField(max_length=255)
    answer_description = models.TextField(null=True)
    link1 = models.CharField(max_length=555, null=True)
    link2 = models.CharField(max_length=555, null=True)
    link3 = models.CharField(max_length=555, null=True)
    link4 = models.CharField(max_length=555, null=True)
    link5 = models.CharField(max_length=555, null=True)
    link6 = models.CharField(max_length=555, null=True)
    link7 = models.CharField(max_length=555, null=True)
    link8 = models.CharField(max_length=555, null=True)
    link9 = models.CharField(max_length=555, null=True)
    link10 = models.CharField(max_length=555, null=True)

    def __str__(self):
        return self.answer_title