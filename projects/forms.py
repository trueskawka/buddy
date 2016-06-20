from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django.forms.extras import SelectDateWidget
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'expiration_date', 'number_of_users_required', 'opensource', 'url')
        widgets = {
	    'name': Textarea(attrs={'rows':2, 'cols':50}),
	    'description': Textarea(attrs={'rows':2, 'cols':45}),
	    'expiration_date': SelectDateWidget(),
	    'number_of_users_required': NumberInput(attrs={'style':'text-align:right'}),
	    'url': TextInput(attrs={'size':54}),
	    }
