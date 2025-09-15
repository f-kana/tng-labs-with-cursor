from django.db import models
from django.utils import timezone


class Task(models.Model):
    """タスク管理用のモデル"""
    
    STATUS_CHOICES = [
        ('not_started', '未着手'),
        ('in_progress', '仕掛中'),
        ('completed', '完了'),
    ]
    
    CATEGORY_CHOICES = [
        ('work', '仕事'),
        ('personal', '個人'),
        ('study', '学習'),
        ('health', '健康'),
        ('finance', '財務'),
        ('other', 'その他'),
    ]
    
    title = models.CharField('件名', max_length=200)
    description = models.TextField('詳細', blank=True, null=True)
    deadline = models.DateTimeField('期限')
    assignee = models.CharField('担当者', max_length=100)
    category = models.CharField(
        'カテゴリ',
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='work'
    )
    status = models.CharField(
        '進捗',
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_started'
    )
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    
    class Meta:
        verbose_name = 'タスク'
        verbose_name_plural = 'タスク'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title