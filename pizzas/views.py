from django.shortcuts import render, redirect 
from .models import *
from .forms import *


# Create your views here.

def index(request):    
    '''The Home page for Pizzeria'''
    context = {}
    return render(request, 'pizzas/index.html',context) 



def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name')
     
     
    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html',context)



def pizza(request,pizza_id):
    p = Pizza.objects.get(id = pizza_id)

    toppings = Topping.objects.filter(pizza = p)
    
    
    context = {'pizza': p, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html',context)


def pizza_comment(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = PizzaForm()
    else:
        print(request.POST)
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            pizza_comment = form.save(commit = False)
            pizza_comment.pizza = pizza
            pizza_comment.save()
            return redirect('pizzas:pizza', pizza_id = pizza_id)

    context = {'form':form, 'pizza': pizza}
    return render(request,'pizzas/pizza_comment.html',context)


