from django.urls import path, include
from . import views

from django.contrib.auth.views import LogoutView
# from mango_seller.customer_details.views import RegisterPage


urlpatterns = [
    path('', views.Customer_List.as_view(), name='Customer_List'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views. RegisterPage.as_view(), name='register'),

    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),
    path('create/', views.Customer_Form.as_view(), name='Customer_Form'),
    path("delete/<str:pk>/", views.delete, name='delete'),
    path("update/<str:pk>/", views.updateOrder, name='update'),

    path("Excel/", views.Export_data_to_Excel, name='Excel'),

    path("contact", views.contact, name="contact"),

]
