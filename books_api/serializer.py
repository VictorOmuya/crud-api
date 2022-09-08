from rest_framework import serializers
from books_api.models import Book
from django.forms import ValidationError

"""
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    published_date = serializers.DateField()
    quantity = serializers.IntegerField()
    
    def create(self, data):
        return Book.objects.create(**data)
    
    def update(self, instance, data):
        instance.title = data.get('title',  instance.title)
        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
        instance.published_date = data.get('published_date', instance.published_date)
        instance.quantity = data.get('quantity', instance.quantity)
        
        instance.save()
        
        return instance    
"""
class BookSerializer(serializers.ModelSerializer):
    description  = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = "__all__"
        

    def validate_title(self, value):  #validating the value
        if value == "Diet Coke":
            raise ValidationError("No diet coke please!")
        return value
    
    
    def validate(Self, data):   #validating data
        if data["number_of_pages"] > 200 and data["quantity"] > 200:
            raise ValidationError("Too heavy please!")
        return data
    
    
    def get_description(self, data):  #Creating a description field
        return "This book is titled " + data.title + " and it is " + str(data.number_of_pages) + " pages long."