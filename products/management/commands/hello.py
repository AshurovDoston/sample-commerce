from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Displays a hello message"

    def add_arguments(self, parser):
        parser.add_argument(
            "--products",
            type=int,
            default=10,
            help="Number of products to display",
        )

    def handle(self, *args, **kwargs):
        num_products = kwargs["products"]
        self.stdout.write(self.style.SUCCESS(f"Creating {num_products} products"))