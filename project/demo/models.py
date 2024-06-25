from django.db import models
from django.urls import reverse

# Create your models here.

class Feedback(models.Model):
    
    GOOD = 'G'
    MODERATE = 'M'
    BAD = 'B'
    
    RATING_CHOICES = [
        (GOOD, 'Good'),
        (MODERATE, 'Moderate'),
        (BAD, 'Bad'),
    ]
    
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    d_rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    t_rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    

    def __str__(self):
        return self.name