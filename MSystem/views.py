from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken  # For generating JWT tokens

# Generic API handler function
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'DELETE', 'PUT'])
    def api(request, id=None):
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many=True)
                return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
                
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'})
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
    return api

# CRUD endpoints for models
manage_customer = generic_api(Customer, CustomerSerializer)
manage_product = generic_api(Product, ProductSerializer)
manage_order = generic_api(Order, OrderSerializer)
manage_mason = generic_api(Mason, MasonSerializer)
manage_payment = generic_api(Payment, PaymentSerializer)

# Sign up endpoint
@api_view(['POST'])
def customer_signup(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            # Saving the new customer object
            customer = serializer.save()

            # Generate JWT token for the new user
            refresh = RefreshToken.for_user(customer)
            access_token = refresh.access_token

            return Response({
                'message': 'Account created successfully!',
                'access_token': str(access_token),  # Return the token
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login endpoint
@api_view(['POST'])
def customer_login(request):
    if request.method == 'POST':
        mobile_number = request.data.get('mobile_number')
        password = request.data.get('password')

        # Check if customer exists with this mobile_number and password
        try:
            customer = Customer.objects.get(mobile_number=mobile_number)
        except Customer.DoesNotExist:
            return Response({'message': 'Invalid credentials!'}, status=status.HTTP_400_BAD_REQUEST)

        if customer.password == password:
            # Generate JWT token for the customer
            refresh = RefreshToken.for_user(customer)
            access_token = refresh.access_token

            return Response({
                'message': 'Login successful!',
                'access_token': str(access_token),  # Return the token
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials!'}, status=status.HTTP_400_BAD_REQUEST)
