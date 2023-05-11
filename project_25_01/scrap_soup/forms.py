from django import forms

class StartScrapForm(forms.Form):
    time = forms.CharField(label="how long do you want scraping?")
    
