from . models import *
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"


class MasonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mason
        fields = "__all__"



class PaymentSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all()) 

    class Meta:
        model = Payment
        fields =  "__all__"



   


