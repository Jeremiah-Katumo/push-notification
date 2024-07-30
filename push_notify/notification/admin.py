
from django.contrib import admin
from django import forms
from django.http import HttpResponseRedirect
from django.urls import path
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from . import models
from . import tasks

# Register your models here.
class SendNotificationForm(forms.Form):
    message = forms.CharField(label="Notification message", max_length=200)

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    add_form_template = "admin/custom_add_form.html"

    def add_view(self, request, form_url="", extra_context=None):
        if request.method == "POST":
            form = SendNotificationForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data["message"]

                notification = models.Notification.objects.create(message=message)

                send_notification_task = tasks.send_notification.delay(message)
                
                # channel_layer = get_channel_layer()
                # async_to_sync(channel_layer.group_send)(
                #     "notifications",
                #     {
                #         "type": "send_notification",
                #         "message": message,
                #     }
                # )

                return HttpResponseRedirect("../{}/".format(notification.pk))
        else:
            form = SendNotificationForm()

        context = self.get_changeform_initial_data(request=request)
        context["form"] = form

        return super().add_view(request, form_url, extra_context=context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("send-notification/", self.admin_site.admin_view(self.add_view), name="send-notification"),
        ]
        return custom_urls + urls