from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image_preview')
    search_fields = ('name',)
    list_filter = ('category',)
 
    def image_preview(self, obj):
        if obj.img:  # 画像が存在する場合のみ表示
            return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.img.url))
        else:
            return "画像なし"
    
    image_preview.short_description = 'プレビュー'  # 管理画面での列名

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)