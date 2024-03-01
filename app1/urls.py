from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.home, name='home'),
    path('second/<str:cat>/<int:id>/', views.second, name="second"),
    path('price/<str:price>', views.priceSort, name="price"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('addCart/<int:id>/<str:color>', views.addCart, name="addCart"),
    path('logoutBtn', views.logoutBtn, name="logoutBtn"),
    path('loginBtn', views.loginBtn, name="loginBtn"),
    path('signup', views.signUp, name="signup"),
    path('cart', views.cart, name="cart"),
    path('order', views.order, name="order"),
    path('cartDelit/<int:id>', views.cartDelit, name="cartDelit"),
    path('payment/<int:id>', views.Payment, name="payment"),
    path('addInOrder/<int:id>', views.addInOrder, name="addInOrder"),
    path('cartModify/<int:id>', views.cartModify, name="cartModify"),
    path('qtyUpdate/<int:id>/<int:mode>', views.qtyUpdate, name="qtyUpdate"),
    path('search/<value>', views.search, name='search_view'),
]
