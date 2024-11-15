from django import forms
from django.forms import BooleanField

from mailing.models import Client, Message, Mailing


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        # fields = "__all__"
        exclude = ("owner",)


class MailingForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания модели рассылка"""

    def __init__(self, owner, *args, **kwargs):
        self.request = kwargs.pop("request")
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields["clients"].queryset = Client.objects.filter(owner=owner)
        self.fields["message"].queryset = Message.objects.filter(owner=owner)

    class Meta:
        model = Mailing
        # fields = "__all__"
        exclude = ("owner",)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        # fields = "__all__"
        exclude = ("owner",)
