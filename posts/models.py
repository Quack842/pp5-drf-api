from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    camera_choices = [
        ('dslr_camera', 'DSLR Camera'),
        ('mirrorless_camera', 'Mirrorless Camera'),
        ('bridge_camera', 'Bridge Camera'),
        ('compact_digital_camera', 'Compact Digital Camera'),
        ('smartphone', 'Smartphone'),
    ]

    photo_type_choices = [
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
        ('sport', 'Sport'),
        ('transportation', 'Transportation'),
        ('water', 'Water'),
        ('wedding', 'Wedding'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=25)
    camera_type = models.CharField(
        max_length=100, choices=camera_choices, default='other'
    )
    photo_type = models.CharField(
        max_length=100, choices=photo_type_choices, default='other'
    )
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_yyxugh', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
