from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Text to display",)

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"


class Link(blocks.StructBlock):

    link_text = blocks.CharBlock(max_length=50, default="More Details")
    internal_page = blocks.PageChooserBlock(required=False)
    external_page = blocks.URLBlock(required=False)


class Card(blocks.StructBlock):

    title = blocks.CharBlock(
        max_length=100,
        help_text="Bold title text for this card. Max lenght 100 characters",
    )
    text = blocks.TextBlock(
        max_length=500,
        help_text="Optional help text for this card. Max lenght is 500 characters.",
        required=False,
    )
    image = ImageChooserBlock(help_text="Image automatically croped to 570px by 370px")
    link = Link(help_text="Enter a link or select a page")


class CardBlock(blocks.StructBlock):

    cards = blocks.ListBlock(Card())

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard cards"
