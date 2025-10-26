from django.contrib import admin
from django.utils.safestring import mark_safe

from courses.models import Category, Course, Lesson
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)


class Meta:
    model = Lesson
    fields = '__all__'


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'active']
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'created_date']
    readonly_fields = ['image_view']

    def image_view(self, course):
        if course.image:
            return mark_safe(f'<image src="/static/{course.image.name}"/>')

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm


admin.site.register(Category)
admin.site.register(Course, CoursesAdmin)
admin.site.register(Lesson, LessonAdmin)
