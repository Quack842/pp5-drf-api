from django.db import models
from django.contrib.auth.models import User


class CameraType(models.Model):
    CAMERA_CHOICES = [
        ('dslr_camera', 'DSLR Camera'),
        ('mirrorless_camera', 'Mirrorless Camera'),
        ('bridge_camera', 'Bridge Camera'),
        ('compact_digital_camera', 'Compact Digital Camera'),
        ('smartphone', 'Smartphone'),
    ]

    name = models.CharField(max_length=100, choices=CAMERA_CHOICES)

    def __str__(self):
        return self.name


class PhotoType(models.Model):
    PHOTO_CHOICES = [
        ('abstract', 'Abstract'),
        ('action', 'Action'),
        ('animals', 'Animals'),
        ('architecture', 'Architecture'),
        ('black_and_white', 'Black and White'),
        ('colors', 'Colors'),
        ('city', 'City'),
        ('fashion', 'Fashion'),
        ('food', 'Food'),
        ('landscape', 'Landscape'),
        ('macro', 'Macro'),
        ('manipulation', 'Manipulation'),
        ('nature', 'Nature'),
        ('night', 'Night'),
        ('objects', 'Objects'),
        ('people', 'People'),
        ('sports', 'Sports'),
        ('transportation', 'Transportation'),
        ('water', 'Water'),
        ('wedding', 'Wedding'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100, choices=PHOTO_CHOICES)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=25)
    camera_type = models.ForeignKey(CameraType, on_delete=models.PROTECT)
    photo_type = models.ForeignKey(PhotoType,  on_delete=models.PROTECT)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_yyxugh', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
