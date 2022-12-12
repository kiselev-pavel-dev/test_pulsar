from django.db import models

from .fields import WEBPField

STATUSES = (
    ("1", "В наличии"),
    ("2", "Под заказ"),
    ("3", "Ожидается поступление"),
    ("4", "Нет в наличии"),
    ("5", "Не производится")
)


class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    articul = models.CharField("Артикул", max_length=150)
    price = models.IntegerField("Цена")
    status = models.CharField("Статус", choices=STATUSES, max_length=20)
    image = WEBPField(
        "Изображение", upload_to="media/")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name}"
