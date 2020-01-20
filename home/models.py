from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class HomePage(Page):

    lead_text = models.CharField(
        max_length=140, blank=True, help_text="Subheading text under the banner title"
    )
    button = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="Select an optional text to link to",
        on_delete=models.SET_NULL,
    )
    button_text = models.CharField(
        max_length=50, default="Read More", blank=False, help_text="Read more "
    )
    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        help_text="The banner background image",
        on_delete=models.SET_NULL,
    )
    body = StreamField(
        [("title", blocks.TitleBlock()), ("cards", blocks.CardBlock()),],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
        StreamFieldPanel("body"),
    ]
