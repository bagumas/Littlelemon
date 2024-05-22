from django.test import TestCase
from restaurant.models import Menu
# Create your tests here.

class MenuViewtest(TestCase):
    def setUp(self):
        Menu.objects.create(title="coffee", price=80, inventory=100)
        Menu.objects.create(title="Tea", price=8, inventory=10)

    def test_getall(self):
        coffee = Menu.objects.get(title="coffee")
        tea = Menu.objects.get(title="tea")
        self.assertEqual(coffee.price, 80)
        self.assertEqual(tea.price, 8)






