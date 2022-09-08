"""
from django.shortcuts import render
from books_api import serializer
from books_api.models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from books_api.serializer import BookSerializer
from rest_framework import status
# Create your views here.

@api_view(["GET"])
def book_list(request):
    books = Book.objects.all() # complex data
    output_data = BookSerializer(books, many=True)
    return Response(output_data.data)

@api_view(["POST"])
def book_create(request):
    input_data = BookSerializer(data = request.data)
    if input_data.is_valid():
        input_data.save()
        return Response(input_data.data)
    else:
        return Response(input_data.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    try: 
        
        book =  Book.objects.get(pk=pk)
    except:
        return Response({
            'error': 'book not available!'
        }, status = status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':  
        output_data = BookSerializer(book)
        return Response(output_data.data)
    
    if request.method == 'PUT':
        input_data = BookSerializer(book, request.data)
        if input_data.is_valid():
            input_data.save()
            return Response(input_data.data)
      
        return Response (input_data.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        book.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
"""

from rest_framework.views import APIView
from books_api import serializer
from books_api.models import Book
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        output_data = serializer.BookSerializer(books, many=True)
        return Response(output_data.data)
    
    
class BookCreate(APIView):
    def post(self, request):
        input_data = serializer.BookSerializer(data = request.data)
        if input_data.is_valid():
            input_data.save()
            return Response(input_data.data)
        
        return Response(input_data.errors, status = status.HTTP_400_BAD_REQUEST)
    
class BookActions(APIView):
    def get_by_pk(self, pk):
        try: 
            book = Book.objects.get(pk=pk)
            return book
        except:
            return Response({
                'error' : 'book does not exist'
            }, status = status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, pk):
        book = self.get_by_pk(pk)
        output_data = serializer.BookSerializer(book)
        return Response(output_data.data)
    
    def put(self, request, pk):
        book = self.get_by_pk(pk)
        input_data = serializer.BookSerializer(book, request.data)
        if input_data.is_valid():
            input_data.save()
            return Response(input_data.data)
        
        return Response(input_data.errors, status =status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)