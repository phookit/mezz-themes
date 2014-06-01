from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide, IconBlurb, Statement

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class StatementInline(TabularDynamicInlineAdmin):
    model = Statement

class IconBlurbline(TabularDynamicInlineAdmin):
    model = IconBlurb

class HomePageAdmin(PageAdmin):
    inlines = (StatementInline, SlideInline, IconBlurbline)

admin.site.register(HomePage, HomePageAdmin)

