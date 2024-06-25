from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'company_name', 'email', 'd_rating', 't_rating']
        widgets = {
            'd_rating': forms.RadioSelect,
            't_rating': forms.RadioSelect,
        }