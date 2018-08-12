from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(),max_length=5000)
    widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
    class Meta:
        model = Topic
        fields = ['subject','message']
