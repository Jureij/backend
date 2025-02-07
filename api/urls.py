from django.urls import path
from MSystem import views
# Import the views for JWT token generation (if needed)
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # SignUp and Login routes using JWT
    path('signup/', views.customer_signup, name='customer_signup'),
    path('customer_login/', views.customer_login, name='customer_login'),

    # Other routes for managing data (e.g., customers, orders, masons, items)
    path('customer/', views.manage_customer),
    path('customer/<int:id>', views.manage_customer),
    path('order/', views.manage_order),
    path('order/<int:id>', views.manage_order),
    path('mason/', views.manage_mason),
    path('mason/<int:id>', views.manage_mason),
    path('product/', views.manage_product),
    path('product/<int:id>', views.manage_product),
    path('payment/', views.manage_payment),
    path('payment/<int:id>', views.manage_payment),

    # JWT Authentication routes (optional, can be used for token-based login)
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
