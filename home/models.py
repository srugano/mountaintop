from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    
    lead_text = models.CharField(max_length=140, blank=True, help_text='Subheading title under the banner title')
    