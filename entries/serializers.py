from rest_framework.serializers import Serializer

from models import Photo

class MyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'name', 'image')