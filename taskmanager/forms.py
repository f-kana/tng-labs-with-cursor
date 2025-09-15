from django import forms
from .models import Task
from datetime import datetime


class TaskForm(forms.ModelForm):
    """タスク作成・編集用フォーム"""
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'assignee', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'タスクの件名を入力してください'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'タスクの詳細を入力してください（任意）',
                'rows': 3
            }),
            'deadline': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'assignee': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '担当者名を入力してください'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'title': '件名',
            'description': '詳細',
            'deadline': '期限',
            'assignee': '担当者',
            'category': 'カテゴリ',
            'status': '進捗'
        }


class TaskFilterForm(forms.Form):
    """タスクフィルタ用フォーム"""
    
    assignee = forms.CharField(
        label='担当者',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '担当者名で検索'
        })
    )
    
    category = forms.ChoiceField(
        label='カテゴリ',
        required=False,
        choices=[('', 'すべて')] + Task.CATEGORY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    status = forms.ChoiceField(
        label='進捗',
        required=False,
        choices=[('', 'すべて')] + Task.STATUS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    deadline_from = forms.DateTimeField(
        label='期限（開始）',
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        })
    )
    
    deadline_to = forms.DateTimeField(
        label='期限（終了）',
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        })
    )
