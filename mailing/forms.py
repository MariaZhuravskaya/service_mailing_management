from django import forms

from mailing.models import MessageSettings, Client


class MessageSettingsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        uuid = kwargs.pop('uuid')
        super().__init__(*args, **kwargs)
        self.fields['customers'].queryset = Client.objects.all().filter(client_user=uuid)

    class Meta:
        model = MessageSettings
        fields = ('name', 'time_from', 'time_by', 'period', 'message', 'customers',)

