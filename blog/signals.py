from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogPost
from django.core.mail import send_mail

@receiver(post_save, sender=BlogPost)
def check_views_count(sender, instance, **kwargs):
    if instance.views_count == 100:
        send_mail(
            'Congratulations!',
            'Your post has reached 100 views.',
            'from@example.com',
            ['your_email@example.com'],
            fail_silently=False,
        )
