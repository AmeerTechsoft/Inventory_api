from rest_framework import serializers
from .models import Supplier,Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())

    class Meta:
        model = Supplier
        fields = '__all__'