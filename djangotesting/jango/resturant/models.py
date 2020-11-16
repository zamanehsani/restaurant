from django.db import models
from django.db import models
from django.contrib.auth.models import User
# from PIL import Image

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete = models.CASCADE)
    genders = (
        ('m', 'male'),
        ('f', 'female'),
        ('other', 'other')
    )
    gender = models.CharField(max_length=50, null=True, choices=genders)

    image = models.ImageField(default='defualt.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        # img = Image.open(self.image.path)

        # if img.height > 300 or width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)