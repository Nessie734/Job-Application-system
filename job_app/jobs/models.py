from django.db import models
from django.conf import settings
# Create your models here.
class Job(models.Model):
    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'employer'},
        related_name='jobs'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=[
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('internship', 'Internship'),
        ('remote', 'Remote'),
    ])
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.employer.username})"
