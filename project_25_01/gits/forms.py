from django import forms

class HashInfoForm(forms.Form):
    #user_id = forms.IntegerField(label='user_id')
    hash_name = forms.CharField(label='hash_name')
    complexity_brut = forms.IntegerField(label='complexity_brut')
    edition_year = forms.DateField(label='edition_year')
    #when_used = forms.DateTimeField(label='when_used')
    military = forms.BooleanField(label='military')

class ImplantInfoForm(forms.Form):
    TYPE_CHOICES = (
    ("IMPOSSIBLE", "im"),
    ("DIFFICULT", "df"),
    ("MIDDLE", "md"),
    ("EASY", "ez"),
)
    implant_name = forms.CharField(label='implant_name')
    buy_possibility = forms.ChoiceField(label='buy_possibility', choices=TYPE_CHOICES)
    strange_type = forms.ChoiceField(label='strange_type', choices=TYPE_CHOICES)
    defense = forms.IntegerField(label='defense')

class SendMailForm(forms.Form):
    to_mail = forms.EmailField(label='to_user')
    message_mail = forms.CharField(label='message_mail')
    reminder = forms.DateTimeField(label='reminder', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
