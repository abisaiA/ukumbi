from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class Welcome(models.Model):
    upperPhrase = models.TextField()
    welcomePhrase = models.TextField()
    lowerPhrase = models.TextField()

    def save(self, *args, **kwargs):
        if Welcome.objects.exists() and not self.pk:
            raise ValidationError('There can only be one instance of this class')
        return super(Welcome, self).save(*args, **kwargs)

    def __str__(self):
        return self.upperPhrase

    class Meta:
        verbose_name_plural = "Welcome"
        verbose_name = "Welcome"


class HallCategoryPhrase(models.Model):
    hall_categories_phrase = models.TextField()

    def __str__(self):
        return self.hall_categories_phrase

    class Meta:
        verbose_name = "CategoryPhrase"


class HallCategory(models.Model):
    sample_image = models.ImageField()
    sample_name = models.CharField(max_length=150)
    sample_description = models.TextField()

    def __str__(self):
        return self.sample_name

    class Meta:
        verbose_name_plural = "HallCategories"
        verbose_name = "HallCategories"


class ServicePhrase(models.Model):
    service_phrase = models.TextField()

    def __str__(self):
        return self.service_phrase

    class Meta:
        verbose_name = "service Phrase"


class Service(models.Model):
    service_name = models.CharField(max_length=150)
    service_description = models.TextField()

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "service"


class RecommendedPhrase(models.Model):
    recommended_phrase = models.TextField()

    def __str__(self):
        return self.recommended_phrase

    class Meta:
        verbose_name = "recommendation phrase"


class Recommendation(models.Model):
    recommendation_image = models.ImageField()
    recommendation_name = models.CharField(max_length=150)
    recommendation_description = models.TextField()

    def __str__(self):
        return self.recommendation_name

    class Meta:
        verbose_name = "recommendation"


class LatestPhrase(models.Model):
            latest_phrase = models.TextField()

            def __str__(self):
                return self.latest_phrase

            class Meta:
                verbose_name = "latest phrase"


class Latest(models.Model):
            latest_image = models.ImageField()
            latest_name = models.CharField(max_length=150)
            latest_description = models.TextField()

            def __str__(self):
                return self.latest_name

            class Meta:
                verbose_name = "latest"






