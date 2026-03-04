from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name or self.address
