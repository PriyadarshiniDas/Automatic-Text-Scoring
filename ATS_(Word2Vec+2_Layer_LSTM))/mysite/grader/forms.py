from django import forms

from .models import Question, Essay
class AnswerForm(forms.ModelForm):
    answer = forms.CharField(max_length=100000, widget=forms.Textarea(attrs={'rows': 5, 'placeholder': "Paste essay here"}))

    class Meta:
        model = Essay
        fields = ['answer']

