from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text','pub_date')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)