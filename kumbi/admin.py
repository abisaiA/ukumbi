from django.contrib import admin

# Register your models here.
from .models import Welcome, HallCategoryPhrase, HallCategory, ServicePhrase, Service, RecommendedPhrase, Recommendation, LatestPhrase, Latest

admin.site.register(Welcome),
admin.site.register(HallCategoryPhrase),
admin.site.register(HallCategory),
admin.site.register(ServicePhrase),
admin.site.register(Service),
admin.site.register(RecommendedPhrase),
admin.site.register(Recommendation),
admin.site.register(LatestPhrase),
admin.site.register(Latest),

