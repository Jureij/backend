from django.contrib import admin
from .models import *


admin.site.register(Customer)
admin.site.register(Mason)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Payment)

