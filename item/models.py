from django.db import models

# Create your models here.
# TODO: Добавить значение default 0 в базу данных для поля quantity


class Item(models.Model):
    objects = None
    title = models.CharField(max_length=255, unique=True)
    article = models.CharField(max_length=16, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    group = models.ForeignKey('item.Group', on_delete=models.PROTECT, null=True)
    tag = models.ManyToManyField('item.Tag')

    def __str__(self):
        if self.article is None:
            return '{1} (---) {0}'.format(self.title, self.pk)
        else:
            return '({2} {0}) {1}'.format(self.article, self.title, self.pk)


class Group(models.Model):
    objects = None
    title = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=16, unique=True)
    perishable = models.BooleanField()

    def full_title(self):
        return '({0}) {1}'.format(self.code, self.title)

    def __str__(self):
        return self.full_title()


class Tag(models.Model):
    title = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.title



