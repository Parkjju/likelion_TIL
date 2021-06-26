from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from django.forms.widgets import CheckboxInput

from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

## 이 부분은 무시하셔도 됩니다. 작성은 하시고 이해하실 필요는 없어요
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        FormHelper.form_show_labels = False

    class Meta:
        model = Task
        fields = '__all__'



        


