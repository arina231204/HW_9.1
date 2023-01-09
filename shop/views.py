from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins, generics, views, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .mygenerics import MYAPIView, ListMixinAPI, CreateMixinAPI

from shop.models import Category, Item, Order
from shop.serializers import CategorySerializer, ItemSerializer
from account.models import Profile
from .permissions import IsAuthorPermission, IsNotAuthorPermission


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthorPermission, ]


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthorPermission, ]

@api_view(['POST','GET'])
@permission_classes([AllowAny])
def view_items(request, category_id):
    if request.method == 'GET':
        items = Item.objects.filter(category=category_id)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class ItemDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, category_id, pk):
        item = get_object_or_404(Item, category=category_id, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, category_id, pk):
        item = get_object_or_404(Item, category=category_id, pk=pk)
        if request.user.id != item.profile.user.id:
            return Response({'message': 'У вас нет разрешения'}, status=401)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, category_id, pk):
        item = get_object_or_404(Item, category=category_id, pk=pk)
        if request.user.id != item.profile.user.id:
            return Response({'message': 'У вас нет разрешения'}, status=401)
        item.delete()
        return Response(status=204)


class OrderItemApiView(APIView):
    permission_classes = (IsNotAuthorPermission,)

    def post(self, request, category_id, pk):
        item = get_object_or_404(Item, pk=pk)
        order = Order.objects.create(profile=request.user, item=item)

        return Response({'message': 'успешно'})


class OrderApiView(APIView):
    def put(self, request, category_id, pk, order_id):
        order = get_object_or_404(Order, pk=order_id)
        if order.profile.user.id != request.user.id:
            return Response({'message': 'У вас нет разрешения'}, status=401)
        return Response({'message': 'успешно'})

    def delete(self, request, category_id, pk, order_id):
        order = get_object_or_404(Order, pk=order_id)
        if order.profile.user.id != request.user.id:
            return Response({'message': 'У вас нет разрешения'}, status=401)
        order.delete()
        return Response({'message': 'успешно'})