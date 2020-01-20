from django.db import models
from wagtail.core.models import Page


class FlexPage(Page):
    class Meta:
        verbose_name = "Flex (.mis) Page"
        verbose_name_plural = "Flex (.mis) Pages"
