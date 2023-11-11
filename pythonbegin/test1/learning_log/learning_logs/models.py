from django.db import models

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns string value"""
        return self.text

class Entry(models.Model):
    """About info of user"""
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='entries'

    def __str__(self):
        """Returns string value"""
        return f"{self.text[:50]}..."
# Create your models here.
