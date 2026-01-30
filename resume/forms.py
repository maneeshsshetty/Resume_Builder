from django import forms
from django.forms import inlineformset_factory
from .models import Resume, Education, Experience, Project

class ResumeForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = Resume
        fields = ['full_name', 'email', 'phone', 'address', 'linkedin_url', 'website_url', 'summary', 'skills']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'john@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+1 234 567 890'}),
            'address': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'City, Country'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'https://linkedin.com/in/johndoe'}),
            'website_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'https://johndoe.com'}),
            'summary': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Brief professional summary...'}),
            'skills': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Python, Django, JavaScript, etc.'}),
        }

class EducationForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'description']
        widgets = {
            'institution': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'University Name'}),
            'degree': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Bachelor of Science'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Computer Science'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3}),
        }

class ExperienceForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'location', 'start_date', 'end_date', 'is_current', 'description']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Software Engineer'}),
            'company': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Tech Corp'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Remote'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3}),
        }

class ProjectForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = Project
        fields = ['title', 'role', 'start_date', 'end_date', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Project Title'}),
            'role': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Role in Project'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3}),
        }

EducationFormSet = inlineformset_factory(Resume, Education, form=EducationForm, extra=1, can_delete=False)
ExperienceFormSet = inlineformset_factory(Resume, Experience, form=ExperienceForm, extra=1, can_delete=False)
ProjectFormSet = inlineformset_factory(Resume, Project, form=ProjectForm, extra=1, can_delete=False)
