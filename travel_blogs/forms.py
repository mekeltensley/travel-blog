from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # This widget overrides Djangos default widget to make the page customizable
        # Gives users the space to write a meaningful entry
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
