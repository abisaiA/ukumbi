from django.shortcuts import render
from .models import *


# Create your views here.
def home_view(request):
    welcome = Welcome.objects.first()
    hallCategory = HallCategory.objects.all()
    categoryPhrase = HallCategoryPhrase.objects.all()
    servicePhrase = ServicePhrase.objects.all()
    service = Service.objects.all()
    recommendationPhrase = RecommendedPhrase.objects.all()
    recommendation = Recommendation.objects.all()
    latestPhrase = LatestPhrase.objects.all()
    latest = Latest.objects.all()

    context = {
        'welcome': welcome,
        'HallCategories': hallCategory,
        'HallCategoryPhrase': categoryPhrase,
        'ServicePhrase': servicePhrase,
        'Service': service,
        'RecommendedPhrase': recommendationPhrase,
        'Recommendation': recommendation,
        'LatestPhrase': latestPhrase,
        'Latest': latest,

    }

    return render(request, 'index.html', context)


def register(request):
    context = {

    }

    return render(request, 'reg_hall.html', context)
