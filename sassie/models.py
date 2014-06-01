from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="The heading under the icon blurbs")
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading")
    latest_posts_heading = models.CharField(max_length=200,
        default="Latest Posts")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    caption = models.CharField(max_length=200)
    text_colour = models.CharField(max_length=15, default='#ffffff', verbose_name="Text Colour")


class Statement(Orderable, RichText):
    '''
    Statement on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="statements")
    title = models.CharField(max_length=200, null=True, blank=True)
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Statement.image", "statement"),
        format="Image", max_length=255, null=True, blank=True)
    image_align = models.CharField(max_length=5,
                                   choices=( ('left', 'Left'),('right', 'Right') ),
                                   default='left')

class IconBlurb(Orderable, RichText):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="blurbs")
    icon = models.CharField(max_length=100, help_text="A font-awesome icon name")
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the blurb will go here.")
