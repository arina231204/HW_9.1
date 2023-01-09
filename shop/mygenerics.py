from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework import status

# class MyListCreateAPIView(views.APIView):
#     serializer_class = None
#     model = None
#
#     def get_queryset(self):
#         return self.model.objects.all()
#     def get(self, request, *args, **kwargs):
#         serializer = self.serializer_class(instance=self.get_queryset(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args,**kwargs):
#         if request.method == 'POST':
#             serializer = self.serializer_class(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListMixinAPI:
    def list(self, request,*args, **kwargs):
        serializer = self.serializer_class(instance=self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateMixinAPI:
    def create(self, request, *args, **kwargs):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveMixinAPI:
    def retrieve(self, request,*args, **kwargs):
        serializer = self.serializer_class(instance=self.get_objects(kwargs['pk']))
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateMixinAPI:
    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_objects(kwargs['pk']), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_objects(kwargs['pk']), data=request.data,partial=True)


class DeleteMixinAPI:
    def destroy(self, request, *args, **kwargs):
        obj = self.get_objects(kwargs['pk'])
        obj.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class MYAPIView(views.APIView):
    serializer_class = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()

    def get_objects(self, pk):
        return generics.get_object_or_404(self.model, pk=pk)


