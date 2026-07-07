from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


@api_view(['POST'])
def add_product(request):
    """Add a new product to the inventory."""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Product Added Successfully",
                "product": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_products(request):
    """Retrieve all products in the inventory."""
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_product(request, id):
    """Update an existing product's details by ID."""
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Product Updated Successfully",
                "product": serializer.data
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request, id):
    """Delete a product from the inventory by ID."""
    product = get_object_or_404(Product, id=id)
    product.delete()
    return Response(
        {"message": "Product Deleted Successfully"},
        status=status.HTTP_200_OK
    )
