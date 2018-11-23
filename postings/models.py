from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

# django hosts --> subdomain for reverse


# class ApiPost(models.Model):
class ApiPost(models.Model):
    # pk aka id --> numbers
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Length = models.CharField(max_length=200, default=0)
    AbsoluteLength = models.CharField(max_length=200, default=0)
    Duration = models.CharField(max_length=200, default=0)
    AvgSpeed = models.CharField(max_length=200, default=0)
    StartPressure = models.CharField(max_length=200, default=0)
    EndPressure = models.CharField(max_length=200, default=0)
    AvgPressure = models.CharField(max_length=200, default=0)
    StartSize = models.CharField(max_length=200, default=0)
    EndSize = models.CharField(max_length=200, default=0)
    AvgSize = models.CharField(max_length=200, default=0)
    StartX = models.CharField(max_length=200, default=0)
    StartY = models.CharField(max_length=200, default=0)
    EndX = models.CharField(max_length=200, default=0)
    EndY = models.CharField(max_length=200, default=0)
    Direction = models.CharField(max_length=200, default=0)
    Area = models.CharField(max_length=200, default=0)
    MoveType = models.TextField(max_length=200, default='null')
    UserID = models.TextField(max_length=200, default='null')
    TrOrTst = models.CharField(max_length=200, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
     #   return str(self.user.user)

    @property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'

    def get_api_url(self, request=None):
        return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)
