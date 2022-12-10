import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import *

pizzas = Pizza.objects.all()
print(pizzas)

for p in pizzas:
    print(p.pizza_name)
    print(p.pizza_image)

'''
cheese = Pizza.objects.get( id = 1)
print(cheese)

toppings = Topping.objects.filter(pizza = cheese)
print(toppings)

for t in toppings:
    print(t.topping_name)


#get user info
from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username)
    print(user.last_login)
'''
print(p.pizza_comment)