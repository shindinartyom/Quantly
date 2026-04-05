from django import forms
from .models import Problem, Tag
from django.core.validators import MinValueValidator, MaxValueValidator

class ProblemForm(forms.ModelForm):
    tags_input = forms.CharField(
        required=False,
        label='Themes',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter themes separated by space or comma...'
        })
    )

    correct_answer = forms.CharField(
        label='Correct Answer (Number or proportion)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a number or fraction (e.g. 1/211)'
        })
    )

    class Meta:
        model = Problem
        fields = ['title', 'description', 'correct_answer', 'tolerance', 'difficulty']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Calculate the probability'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Problem description...'
            }),
            'tolerance': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'placeholder': 'e.g. 0.01'
            }),
            'difficulty': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'title': 'Problem Title',
            'description': 'Description',
            'correct_answer': 'Correct Answer (Number)',
            'tolerance': 'Tolerance (margin of error)',
            'difficulty': 'Difficulty',
        }
    
    def clean_correct_answer(self):
        answer_str = str(self.cleaned_data['correct_answer']).strip()
        num = None
        if '/' in answer_str:
            parts = answer_str.split('/')
            if len(parts) == 2:
                try:
                    num = float(parts[0]) / float(parts[1])
                except ValueError:
                    pass
        else:
            try:
                num = float(answer_str)
            except ValueError:
                pass
        
        if num is None:
            raise forms.ValidationError('Invalid input. Please enter a valid number or fraction.')
            
        if num < -1000000 or num > 1000000:
            raise forms.ValidationError('Answer must be between -1,000,000 and 1,000,000')
        return num

class AnswerForm(forms.Form):
    user_answer = forms.CharField(
        label='Your Answer',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a number or fraction (e.g. 1/211)'
        })
    )