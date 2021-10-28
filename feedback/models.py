from django.db import models

class Message(models.Model):
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.message