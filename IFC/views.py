from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group, login_required
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
    return render(request, 'IFC/ourChapters.html')


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


def Acacia(request):
    return render(request, 'IFC/chapterPages/Acacia.html')


def AlphaEpsilonPi(request):
    return render(request, 'IFC/chapterPages/AlphaEpsilonPi.html')


def AlphaSigmaPhi(request):
    return render(request, 'IFC/chapterPages/AlphaSigmaPhi.html')


def AlphaChiRho(request):
    return render(request, 'IFC/chapterPages/AlphaChiRho.html')


def ChiPhi(request):
    return render(request, 'IFC/chapterPages/ChiPhi.html')


def DeltaKappaEpsilon(request):
    return render(request, 'IFC/chapterPages/DeltaKappaEpsilon.html')


def DeltaPhi(request):
    return render(request, 'IFC/chapterPages/DeltaPhi.html')


def DeltaTauDelta(request):
    return render(request, 'IFC/chapterPages/DeltaTauDelta.html')


def LambdaChiAlpha(request):
    return render(request, 'IFC/chapterPages/LambdaChiAlpha.html')


def PhiGammaDelta(request):
    return render(request, 'IFC/chapterPages/PhiGammaDelta.html')


def PhiKappaTheta(request):
    return render(request, 'IFC/chapterPages/PhiKappaTheta.html')


def PhiMuDelta(request):
    return render(request, 'IFC/chapterPages/PhiMuDelta.html')


def PhiSigmaKappa(request):
    return render(request, 'IFC/chapterPages/PhiSigmaKappa.html')


def PiKappaAlpha(request):
    return render(request, 'IFC/chapterPages/PiKappaAlpha.html')


def PiLambdaPhi(request):
    return render(request, 'IFC/chapterPages/PiLambdaPhi.html')


def PsiUpsilon(request):
    return render(request, 'IFC/chapterPages/PsiUpsilon.html')


def SigmaChi(request):
    return render(request, 'IFC/chapterPages/SigmaChi.html')


def SigmaAlphaEpsilon(request):
    return render(request, 'IFC/chapterPages/SigmaAlphaEpsilon.html')


def SigmaPhiEpsilon(request):
    return render(request, 'IFC/chapterPages/SigmaPhiEpsilon.html')


def TauEpsilonPhi(request):
    return render(request, 'IFC/chapterPages/TauEpsilonPhi.html')


def TauKappaEpsilon(request):
    return render(request, 'IFC/chapterPages/TauKappaEpsilon.html')


def ThetaXi(request):
    return render(request, 'IFC/chapterPages/ThetaXi.html')


def ZetaPsi(request):
    return render(request, 'IFC/chapterPages/ZetaPsi.html')


def editChapterInfo(request):
    return render(request, 'IFC/chapterInfoEdit.html')


#@login_required
def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    return render(request, 'chapters', {'chapter': chapter})


#@login_required
def edit_chapter(request, chapter_id):
    # Get the chapter by ID (or use some other logic to assign chapters to users)
    chapter = get_object_or_404(Chapter, id=chapter_id)
    
    # Ensure the user is authorized to edit this chapter (this depends on your user model/permissions setup)
    # You might need to compare request.user with the user related to the chapter
    
    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('chapter_detail', chapter_id=chapter.id)  # Redirect to a chapter detail page
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'chapterInfoEdit.html', {'form': ChapterForm, 'chapter': chapter})
