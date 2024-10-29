from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .forms import ChapterForm, SignUpForm
from .models import Chapter


# Requesting Webpages:
def homepage(request):
    return render(request, 'IFC/homepage.html')


def leadership(request):
    return render(request, 'IFC/leadership.html')


def contacts(request):
    return render(request, 'IFC/contacts.html')


def ourChapters(request):
    chapters = Chapter.objects.all()
    return render(request, 'IFC/ourChapters.html', {'chapters': chapters})


def schedule(request):
    return render(request, 'IFC/schedule.html')


def documents(request):
    return render(request, 'IFC/importantDocuments.html')


def forChapters(request):
    return render(request, 'IFC/forChapters.html')


def calendar(request):
    return render(request, 'IFC/calendar.html')


def recruitment(request):
    return render(request, 'IFC/recruitment.html')


def fall(request):
    return render(request, 'IFC/fall.html')


def spring(request):
    return render(request, 'IFC/spring.html')


def awards(request):
    return render(request, 'IFC/awards.html')


def eventSchedule(request):
    return render(request, 'IFC/eventSchedule.html')


def select_chapter(request):
    chapters = Chapter.objects.all()
    return render(request, 'IFC/select_chapter.html', {'chapters': chapters})


# @login_required
def chapter_detail(request, chapter_name):
    chapter_name = chapter_name.replace('-', ' ')
    chapter = get_object_or_404(Chapter, name=chapter_name)
    return render(request, 'IFC/Chapter_base.html', {'chapter': chapter})


# @login_required
def edit_chapter(request, chapter_name):
    # Get the chapter by ID (or use some other logic to assign chapters to users)
    chapter_name = chapter_name.replace('-', ' ')
    chapter = get_object_or_404(Chapter, name=chapter_name)

    # Ensure the user is authorized to edit this chapter (this depends on your user model/permissions setup)
    # You might need to compare request.user with the user related to the chapter

    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect("/chapters/" + chapter.slug + "/")  # Redirect to a chapter detail page
    else:
        form = ChapterForm(instance=chapter)

    return render(request, 'IFC/chapterInfoEdit.html', {'form': form, 'chapter': chapter})

#   def chapter_detail(request, slug):
#    chapter = get_object_or_404(Chapter, slug=slug)
#    return render(request, 'IFC/<slug>.html', {'chapter': chapter})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'IFC/login.html', {'error': 'Invalid username or password'})
    return render(request, 'IFC/login.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'IFC/signup.html', {'signup_form': form})

def user_logout(request):
    logout(request)
    return redirect('/')