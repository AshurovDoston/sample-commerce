from django.contrib import admin
from .models import Category, Product, ProductImage
from django.utils.html import format_html

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["get_primary_image", "name", "category", "price", "stock_quantity", "is_available", "created_at", "updated_at"]
    list_filter = ["is_available", "category", "created_at"]
    search_fields = ["name", "description"]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["price", "stock_quantity", "is_available"]
    inlines = [ProductImageInline]

    ### This is an alternative implementation of get_primary_image method.
    ### Here we are using business logic inside Admin layer instead of model method.

    # def get_primary_image(self, obj):
    #     primary_image = obj.rasmlar.filter(is_primary=True).first()
    #     if not primary_image:
    #         primary_image = obj.rasmlar.first()
    #     if primary_image and primary_image.image:
    #         return format_html(
    #             '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
    #             primary_image.image.url,
    #         )
    #     return "(No Image)"


    ### Move business logic to model.
    def get_primary_image(self, obj):
        image = obj.primary_image()
        if image and image.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                image.image.url,
            )
        return "(No Image)"

    get_primary_image.short_description = "Image"



