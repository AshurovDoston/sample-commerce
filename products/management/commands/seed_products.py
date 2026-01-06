from django.core.management.base import BaseCommand
from django.db import transaction
from products.models import Product, Category

class Command(BaseCommand):
    help = "Seed database with sample products"

    category, _ = Category.objects.get_or_create(name="Garden", defaults={
        "description": "Electronic gadgets and devices",
        "is_active": True,
    })

    PRODUCTS = [
    {"name": "iPhone 13", "description": "Latest iPhone model", "price": 12000000, "category": category, "stock_quantity": 50},
    {"name": "Samsung Galaxy S23", "description": "Latest Samsung Galaxy model", "price": 9500000, "category": category, "stock_quantity": 30},
    {"name": "MacBook Air M1", "description": "Lightweight laptop with M1 chip", "price": 14500000, "category": category, "stock_quantity": 25},
    {"name": "AirPods Pro", "description": "Wireless earbuds with noise cancellation", "price": 3200000, "category": category, "stock_quantity": 100},
]
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Seeding products..."))

        products_created = 0
        with transaction.atomic():
            for data in Command.PRODUCTS:
                product, created = Product.objects.get_or_create(
                    name=data["name"],
                    defaults={
                        "description": data["description"],
                        "price": data["price"],
                        "stock_quantity": data["stock_quantity"],
                        "category": data["category"],
                    },
                )
                if created:
                    products_created += 1
                    self.stdout.write(
                        self.style.SUCCESS(f"Created product: {product.name}")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Product already exists: {product.name}")
                    )

        self.stdout.write(
            self.style.SUCCESS(f"Seeding complete! {products_created} products created.")
        )
