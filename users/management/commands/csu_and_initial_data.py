from django.core.management import BaseCommand

from restaurant.models import Restaurant, Table
from users.models import User


class Command(BaseCommand):
    """
    Создание суперпользователя и начальных данных
    """

    help = "Создание суперпользователя с полными правами доступа"

    def handle(self, *args, **options):

        User.objects.all().delete()
        Restaurant.objects.all().delete()
        Table.objects.all().delete()

        user = User.objects.create(
            email="admin@mail.ru",
            first_name="admin",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password("123")
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Суперпользователь создан: {user.email}"))

        restaurant = Restaurant.objects.create(
            name="Курорт-рюмочная",
            address="г. Москва, ул. Пятницкая, д.31 с5",
            phone_number="+7 (915) 243 24 31",
        )
        restaurant.save()
        self.stdout.write(self.style.SUCCESS(f"Ресторан создан: {restaurant.name}"))

        rest_table = Restaurant.objects.all().first()
        table1 = Table.objects.create(number=1, seats=5, restaurant=rest_table)
        table1.save()
        self.stdout.write(
            self.style.SUCCESS(
                f'Ресторан "{table1.restaurant}" создан столик: {table1.number}'
            )
        )

        table2 = Table.objects.create(number=2, seats=4, restaurant=rest_table)
        table1.save()
        self.stdout.write(
            self.style.SUCCESS(
                f'Ресторан "{table2.restaurant}" создан столик: {table2.number}'
            )
        )
