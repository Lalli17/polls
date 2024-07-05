
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['question', 'option_1', 'option_2', 'option_3', 'option_4']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'option_1': forms.TextInput(attrs={'class': 'form-control'}),
            'option_2': forms.TextInput(attrs={'class': 'form-control'}),
            'option_3': forms.TextInput(attrs={'class': 'form-control'}),
            'option_4': forms.TextInput(attrs={'class': 'form-control'}),
        }
