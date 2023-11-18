from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializer import CategorySerializer, ProductSerializer
from .models import Category, Product


class CategoryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):  # noqa
        category = Category.object.all().order_by('-created_at') # noqa
        category_serializer = CategorySerializer(category, many=True)
        return Response(category_serializer.data)


class AddProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['POST'])
    def add_product(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

