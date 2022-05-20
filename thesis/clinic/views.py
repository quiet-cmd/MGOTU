from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    context = {
        'CategoryServicesBD': CategoryServices.objects.all()[:6],
        'DoctorsBD': Doctors.objects.all()[:3],
        'ClinicDocumentsBD': ClinicDocuments.objects.all()[:3],
    }
    return render(request, 'clinic/index.html', context=context)


def services(request):
    context = {
        'CategoryServicesBD': CategoryServices.objects.all(),
        'ServicesBD': Services.objects.all(),
    }
    return render(request, 'clinic/all_services.html', context=context)


def doctors(request):
    context = {
        'DoctorsBD': Doctors.objects.all(),
    }
    return render(request, 'clinic/all_doctors.html', context=context)


def doctor(request, doctor_id):
    context = {
        'DoctorsBD': get_object_or_404(Doctors, pk=doctor_id),
    }
    return render(request, 'clinic/doctor.html', context=context)


def documents(request):
    context = {
        'ClinicDocumentsBD': ClinicDocuments.objects.all(),
        'CategoryClinicDocumentsBD': CategoryClinicDocuments.objects.all(),
    }
    return render(request, 'clinic/all_documents.html', context=context)


def articles(request):
    context = {
        'ArticleBD': Article.objects.all(),
        'CategoryArticleBD': CategoryArticle.objects.all(),
    }
    return render(request, 'clinic/all_articles.html', context=context)


def article(request, article_id):
    context = {
        'ArticleBD': get_object_or_404(Article, pk=article_id),
    }
    return render(request, 'clinic/article.html', context=context)
