from django.db.models import F
from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.auth.models import User

from paragliding_shop.equipment.models import Wings
from paragliding_shop.order.models import UserItem


# Comment thing are original from tutorial uncomment are my they are over the original. Where have Wings it's my
# Have to remove unicorn button ifdon't work.


class EquipmentView(UnicornView):
    # user_products: QuerySetType[Wings] = None
    user_products: QuerySetType[UserItem] = None
    user_pk: int
    total: float = 0

    def __int__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        # self.user_products = Wings.objects.filter(user=self.user_pk)
        self.user_products = UserItem.objects.filter(user=self.user_pk)
        self.get_total()

    def add_item(self, product_pk):
        # item, created = Wings.objects.get_or_create(
        item, created = UserItem.objects.get_or_create(
            user_id=self.user_pk, product_id=product_pk
        )

        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        # self.user_products = Wings.objects.filter(user=self.user_pk)
        self.user_products = UserItem.objects.filter(user=self.user_pk)
        self.get_total()

    def delete_item(self, product_pk):
        item = UserItem.objects.filter(pk=product_pk)
        item.delete()
        self.user_products = self.user_products.exclude(pk=product_pk)
        self.get_total()

    def get_total(self):
        self.total = sum(
            product.total_price for product in self.user_products
        )
