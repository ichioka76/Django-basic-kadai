from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    myText = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, default='noImage.png')

     # 商品詳細の説明フィールドを追加
    description = models.TextField(
        blank=True,  # フィールドが空でも許可
        null=True,   # データベースにnullを許可
    )
    
    def __str__(self):
        return self.name
    
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')