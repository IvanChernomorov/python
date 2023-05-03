from django.db import models

class Artists(models.Model):
    pseudonym = models.CharField("Псевдоним исполнителя", max_length=50)
    genre = models.CharField("Жанр", max_length=50)
    formed_in = models.DateField("Дата начала карьеры")
    country = models.CharField("Страна", max_length=50)

    def __str__(self):
        return format(self.pseudonym)

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

class Albums(models.Model):
    title = models.CharField("Название альбома", max_length=50)
    id_ar = models.ForeignKey(Artists,on_delete=models.CASCADE)
    release_date = models.DateField("Дата выпуска")
    label = models.CharField("Лейбл", max_length=50)

    def __str__(self):
        return format(self.title)

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

class Songs(models.Model):
    title = models.CharField("Название песни",max_length=50)
    id_al = models.ForeignKey(Albums,on_delete=models.CASCADE)
    id_ar = models.ForeignKey(Artists,on_delete=models.CASCADE)
    length = models.IntegerField("Продолжительность песни в секундах")

    def __str__(self):
        return format(self.title)


    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"