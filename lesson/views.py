from django.shortcuts import render, get_object_or_404
from .models import LessonCategory, Lesson

def lessons(request):
    lessons = Lesson.objects.all().order_by('-created_at')
    categories = LessonCategory.objects.all().order_by('-created_at')
    
    context = {
        'lessons': lessons,
        'categories': categories
    }
    
    return render(request, 'lesson/lessons.html', context)


def lesson_detail(request, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    
    context = {
        'lesson': lesson
    }
    
    return render(request, 'lesson/lesson-detail.html', context)