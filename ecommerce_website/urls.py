from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from account import views as a_views
from shop import views as s_views, views
from rest_framework.authtoken import views as auth_views



a_router = routers.DefaultRouter()
a_router.register('sender', a_views.ProfileSenderViewSet, basename='sender')
a_router.register('buyer', a_views.ProfileBuyerViewSet, basename='buyer')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/register/', include(a_router.urls)),
    path('api/shop/category/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/token/', auth_views.obtain_auth_token),
    path('api/shop/category/<category_id>/item/', views.view_items),
    path('api/shop/category/<int:category_id>/item/<int:pk>/', views.ItemDetailView.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:pk>/order/<int:order_id>/', views.OrderApiView.as_view()),
]

