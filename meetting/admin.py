from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'prev_title', 'title', 'created_at', 'is_published')
    list_editable = ('prev_title', 'title', 'is_published')



@admin.register(Strongest)
class StrongestAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', "get_logo")

    def get_logo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="75px">')




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_editable = ('title',)



class TimeMeetingAdmin(admin.StackedInline):
    model = TimeMeeting
    extra = 1

class PhoneAdmin(admin.StackedInline):
    model = Phone
    extra = 1

@admin.register(Meeting)
class AdminMeeting(admin.ModelAdmin):
    list_display = ('pk', 'title', 'get_price', 'location', 'get_image')
    list_editable = ('title', 'location')
    list_display_links = ('get_image',)
    inlines = [
        TimeMeetingAdmin,
        PhoneAdmin,
    ]

    def get_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100px">')

    def get_price(self, obj):
        if obj.price:
            return f"${obj.price}"



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'get_price', 'get_photo')
    list_editable = ('title',)
    list_display_links = ('pk', 'get_photo')

    def get_price(self, obj):
        if obj.price:
            return f"${obj.price}"

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75px">')


@admin.register(AboutUniversity)
class AboutUniversityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_succesed_students', 'new_students', 'current_teachers', 'awards')
    list_editable = ('new_students', 'current_teachers', 'awards')

    def get_succesed_students(self, obj):
        if obj.succesed_students:
            return f"{obj.succesed_students}%"


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone', 'mail', 'address', 'url')
    list_editable = ('phone', 'mail', 'address', 'url')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'mail', 'subject', 'message')
    readonly_fields = ('pk', 'name', 'mail', 'subject', 'message')