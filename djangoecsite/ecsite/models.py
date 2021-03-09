from django.db import models


class EcSite(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(default='Unstarted', max_length=100)

    def __str__(self):
        """A string representation of th model."""
        return self.title
