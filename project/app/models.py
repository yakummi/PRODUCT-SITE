from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Барахолка
# Модели:
# Категория
# Товар (его продавец)
# Покупатель (он может писать отзывы товару, ставить оценку)


class Category(models.Model): # Категория
    name = models.CharField(max_length=30)
    image = models.URLField(null=False)
    slug = models.SlugField(max_length=50)

class Product(models.Model): # Публикация своего продукта
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.URLField(null=True)

class Comment(models.Model): # Оставляем комментарий и комментарий
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    evaluation = models.IntegerField()
    text = models.TextField()
    photos = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def validate(self, exclude=None):
        super().validate(exclude=exclude)
        if self.evaluation not in [1, 2, 3, 4, 5]:
            raise ValidationError("Можно оценивать только от 1 до 5!")





