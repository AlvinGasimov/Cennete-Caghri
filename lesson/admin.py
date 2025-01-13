from django.contrib import admin
from .models import LessonCategory, Lesson

@admin.register(LessonCategory)
class LessonCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'lesson_count', 'slug', 'created_at')
    search_fields = ('name',)
    
    def lesson_count(self, obj):
        return obj.lesson_count()
    lesson_count.short_description = 'Ders Sayısı'
    
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'image', 'slug', 'created_at')
    search_fields = ('title', 'author', 'category', 'description')