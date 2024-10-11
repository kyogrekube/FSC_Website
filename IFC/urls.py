"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from IFC import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # IFC app URLs
    path("", views.homepage, name="home"),
    path("documents", views.documents, name="documents"),
    path("chapters", views.ourChapters, name="chapters"),
    path("calendar", views.calendar, name="calendar"),
    path("leadership", views.leadership, name="leadership"),
    path("recruitment", views.recruitment, name="recruitment"),
    path("fall", views.fall, name="fall"),
    path("spring", views.spring, name="spring"),
    path("event-schedule", views.eventSchedule, name="event-schedule"),
    path("chapters/Acacia", views.Acacia, name="Acacia"),
    path("chapters/AlphaEpsilonPi", views.AlphaEpsilonPi, name="AlphaEpsilonPi"),
    path("chapters/AlphaSigmaPhi", views.AlphaSigmaPhi, name="AlphaSigmaPhi"),
    path("chapters/AlphaChiRho", views.AlphaChiRho, name="AlphaChiRho"),
    path("chapters/ChiPhi", views.ChiPhi, name="ChiPhi"),
    path("chapters/DeltaKappaEpsilon", views.DeltaKappaEpsilon, name="DeltaKappaEpsilon"),
    path("chapters/DeltaPhi", views.DeltaPhi, name="DeltaPhi"),
    path("chapters/DeltaTauDelta", views.DeltaTauDelta, name="DeltaTauDelta"),
    path("chapters/LambdaChiAlpha", views.LambdaChiAlpha, name="LambdaChiAlpha"),
    path("chapters/PhiGammaDelta", views.PhiGammaDelta, name="PhiGammaDelta"),
    path("chapters/PhiKappaTheta", views.PhiKappaTheta, name="PhiKappaTheta"),
    path("chapters/PhiMuDelta", views.PhiMuDelta, name="PhiMuDelta"),
    path("chapters/PhiSigmaKappa", views.PhiSigmaKappa, name="PhiSigmaKappa"),
    path("chapters/PiKappaAlpha", views.PiKappaAlpha, name="PiKappaAlpha"),
    path("chapters/PiLambdaPhi", views.PiLambdaPhi, name="PiLambdaPhi"),
    path("chapters/PsiUpsilon", views.PsiUpsilon, name="PsiUpsilon"),
    path("chapters/SigmaAlphaEpsilon", views.SigmaAlphaEpsilon, name="SigmaAlphaEpsilon"),
    path("chapters/SigmaChi", views.SigmaChi, name="SigmaChi"),
    path("chapters/SigmaPhiEpsilon", views.SigmaPhiEpsilon, name="SigmaPhiEpsilon"),
    path("chapters/TauEpsilonPhi", views.TauEpsilonPhi, name="TauEpsilonPhi"),
    path("chapters/TauKappaEpsilon", views.TauKappaEpsilon, name="TauKappaEpsilon"),
    path("chapters/ThetaXi", views.ThetaXi, name="ThetaXi"),
    path("chapters/ZetaPsi", views.ZetaPsi, name="ZetaPsi"),
    path("editChapterInfo", views.editChapterInfo, name="editChapterInfo"),
]
