from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

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

def uploadSuccess(request):
    return render(request, 'IFC/uploadSuccess.html')

def handle_uploaded_file(f):
    with open("uploaded_file.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/upload")
    else:
        form = UploadFileForm()
    return render(request, "IFC/upload_file.html", {"form": form})