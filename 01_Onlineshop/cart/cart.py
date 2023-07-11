# from decimal import Decimal
# from django.conf import settings
# from shop.models import Product
#
# class Cart(object):
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get(settings.CART_ID)
#         if not cart :
#             cart = self.session[settings.CART_ID] = {}
#         self.cart = cart
#
#     def __len__(self):
#         return sum(item['quantity'] for item in self.cat.values())
#
#     def __iter__(self):
#         product_ids = self.cart.keys()