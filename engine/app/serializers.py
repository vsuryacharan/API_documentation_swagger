from rest_framework import serializers
class datafun(serializers.Serializer):
    name=serializers.CharField(max_length=100)

from .models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__' 