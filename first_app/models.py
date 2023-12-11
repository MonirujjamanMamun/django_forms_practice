from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default='Lutfor Rahman')

    def __str__(self) -> str:
        return f'Roll- {self.roll} - {self.name}'


class modelPractice(models.Model):
    boolField = models.BooleanField()
    name = models.CharField(max_length=50)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    email = models.EmailField()
    file_field = models.FileField()
    int_field = models.IntegerField()
    float_field = models.FloatField()
    img_filed = models.ImageField()
    join_field = models.JSONField()
    slig_field = models.SlugField()
    text_field = models.TextField()
    time_field = models.TimeField()
