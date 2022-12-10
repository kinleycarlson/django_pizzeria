from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length = 100)
    pizza_image = models.ImageField(null = False, blank = True, upload_to = "images/")
    pizza_comment = models.CharField(null=True,max_length=500)
    
    def __str__(self):
        return self.pizza_name
        

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length= 200)
    

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.topping_name
