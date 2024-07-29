from django.contrib import admin
from django import forms

from . import models

# Register your models here.
class SendNotificationForm(forms.Form):
    message = forms.CharField(label="Notification message", max_length=200)

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    add_form_template = "admin/custom_add_form.html"