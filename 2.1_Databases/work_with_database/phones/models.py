from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.FloatField()
    image = models.URLField(max_length=200)
    release_date  = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f"{self.name}: {self.price}"

    class Meta:
        ordering = ['-release_date']
        indexes = [
            models.Index(fields=['-release_date']),
            models.Index(fields=['name'])
        ]