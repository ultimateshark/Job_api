from django.db import models

# Create your models here.
class AllPosts(models.Model):
    job_id=models.IntegerField()
    role=models.CharField(max_length=200)
    locations=models.CharField(max_length=200)
    min_experience=models.IntegerField()
    max_experience=models.IntegerField()
    salary_range_from=models.FloatField()
    salary_range_to=models.FloatField()
    description=models.CharField(max_length=255)
    required_skills=models.CharField(max_length=255)
    perks=models.CharField(max_length=150)
    date_posted=models.DateTimeField(blank=True)
