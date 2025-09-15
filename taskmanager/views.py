from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from django.db.models import Q
from .models import Task
from .forms import TaskForm, TaskFilterForm


class TaskListView(ListView):
    """タスク一覧表示"""
    model = Task
    template_name = 'taskmanager/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10
    
    def get_queryset(self):
        """フィルタ機能付きクエリセット"""
        queryset = Task.objects.all()
        filter_form = TaskFilterForm(self.request.GET)
        
        if filter_form.is_valid():
            # 担当者フィルタ
            assignee = filter_form.cleaned_data.get('assignee')
            if assignee:
                queryset = queryset.filter(assignee__icontains=assignee)
            
            # カテゴリフィルタ
            category = filter_form.cleaned_data.get('category')
            if category:
                queryset = queryset.filter(category=category)
            
            # 進捗フィルタ
            status = filter_form.cleaned_data.get('status')
            if status:
                queryset = queryset.filter(status=status)
            
            # 期限フィルタ
            deadline_from = filter_form.cleaned_data.get('deadline_from')
            if deadline_from:
                queryset = queryset.filter(deadline__gte=deadline_from)
            
            deadline_to = filter_form.cleaned_data.get('deadline_to')
            if deadline_to:
                queryset = queryset.filter(deadline__lte=deadline_to)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """コンテキストデータにフィルタフォームを追加"""
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskFilterForm(self.request.GET)
        return context


class TaskCreateView(CreateView):
    """タスク新規作成"""
    model = Task
    form_class = TaskForm
    template_name = 'taskmanager/task_form.html'
    
    def get_success_url(self):
        return reverse('taskmanager:task_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'タスクが正常に作成されました。')
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    """タスク編集（進捗更新含む）"""
    model = Task
    form_class = TaskForm
    template_name = 'taskmanager/task_form.html'
    
    def get_success_url(self):
        return reverse('taskmanager:task_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'タスクが正常に更新されました。')
        return super().form_valid(form)


def task_detail(request, pk):
    """タスク詳細表示"""
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskmanager/task_detail.html', {'task': task})


def task_delete(request, pk):
    """タスク削除"""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'タスクが削除されました。')
        return redirect('taskmanager:task_list')
    return render(request, 'taskmanager/task_confirm_delete.html', {'task': task})