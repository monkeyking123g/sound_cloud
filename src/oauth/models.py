from django.core.validators import FileExtensionValidator
from django.db import models

from src.base.services import get_path_upload_avatar, validate_size_image


class AuthUser(models.Model):
    """ Platform user model
    """
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    @property
    def is_authenticated(self):
        """ Always returns True. This is the way to find out if the user has been authenticated
        """
        return True

    def __str__(self):
        return self.email


class Follower(models.Model):
    """ Subscriber model
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='subscribers')

    def __str__(self):
        return f'{self.subscriber} subscribed to {self.user}'


class SocialLink(models.Model):
    """ social link model user network
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'



