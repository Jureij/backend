from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here. 
class Customer(models.Model):
    GENDER_CHOICES = {
        'MALE':'MALE',
        'FEMALE':'FEMALE',
    }
    name = models.CharField(max_length=20)
    address = models.TextField(max_length=20)
    mobile_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=8)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    

    def __str__(self):
        return f"{self.name}"
    

 
    
  
    

class Mason(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,  unique=True)
    password = models.CharField(max_length=8)
    mobile_number = models.CharField(max_length=10, unique=True)
    experience_years = models.PositiveIntegerField(default=0)
    specialty = models.CharField(max_length=50, blank= True)
   

    def __str__(self):
        return f"{self.name}" 


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name






    


class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('materials', 'Order for Materials'),
        ('mason', 'Request for Mason'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES, default='materials')
    mason = models.ForeignKey(Mason, on_delete=models.SET_NULL, blank=True, null=True, help_text="Select a mason if applicable")
    products = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, help_text="Select a mason if applicable")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Total price of the order")
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.id} - {self.get_order_type_display()}"

    def save(self, *args, **kwargs):
        if self.order_type != 'mason':
            self.mason = None
        super().save(*args, **kwargs)

    

    
    
 


 

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('mobile_money', 'Mobile Money'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments", help_text="Related order for this payment")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount paid for the order")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash', help_text="Method used for payment")
    payment_date = models.DateTimeField(default=timezone.now, help_text="Date and time when the payment was made")
    reference_number = models.CharField(max_length=100, blank=True, null=True, help_text="Optional payment reference number")

    def __str__(self):
        return f"Payment {self.id} - Order {self.order.id}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"