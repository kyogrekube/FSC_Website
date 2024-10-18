from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .forms import ChapterForm
from .models import Chapter


def create_user_accounts(request):
    # Create an admin account
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='',   # Add an email here when we pass code to FSC
            password='adminPassword'
        )
        print('Admin account created successfully')

    # Create
    if not Group.objects.filter(name='Chapter Users').exists():
        chapter_users_group = Group.objects.create(name='Chapter Users')
        print('Created chapter users grouping')

        # Create user for Phi Gamma Delta
        if not User.objects.filter(username='Phi_Gamma_Delta').exists():
            phi_gamma_delta_user = User.objects.create_user(
                username='phi_gamma_delta',
                email='',
                password='password123'
            )
            phi_gamma_delta_user.groups.add(chapter_users_group)
            print('Phi Gamma Delta user created and added to chapter users grouping')

        # Create user for Sigma Alpha Epsilon
        if not User.objects.filter(username='Sigma_Alpha_Epsilon').exists():
            sigma_alpha_epsilon_user = User.objects.create_user(
                username='sigma_alpha_epsilon',
                email='',
                password='password123'
            )
            sigma_alpha_epsilon_user.groups.add(chapter_users_group)
            print('Sigma Alpha Epsilon user created and added to chapter users grouping')

    return HttpResponse("Admin account and chapter user accounts created successfully!")


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


def eventSchedule(request):
    return render(request, 'IFC/eventSchedule.html')

def chapterInfoEdit(request):
    return render(request, 'IFC/chapterInfoEdit.html')


def select_chapter(request):
    chapter = Chapter.objects.all()
    return render(request, 'IFC/select_chapter.html', {'chapters': chapter})


# @login_required
def chapter_detail(request, chapter_name):
    #chapter = get_object_or_404(Chapter, id=chapter_name)
    return render(request, 'IFC/chapterPages/' + chapter_name + '.html')


# @login_required
def edit_chapter(request, chapter_name):
    # Get the chapter by ID (or use some other logic to assign chapters to users)
    chapter_name = chapter_name.replace('-', ' ')
    chapter = get_object_or_404(Chapter, name=chapter_name)

    # Ensure the user is authorized to edit this chapter (this depends on your user model/permissions setup)
    # You might need to compare request.user with the user related to the chapter

    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a chapter detail page
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'IFC/chapterInfoEdit.html', {'form': ChapterForm, 'chapter': chapter})


def chapter_list(request):
    chapters = Chapter.objects.all()
    return render(request, 'IFC/chapter_list.html', {'chapters': chapters})

#def chapter_detail(request, slug):
#    chapter = get_object_or_404(Chapter, slug=slug)
#    return render(request, 'IFC/<slug>.html', {'chapter': chapter})
