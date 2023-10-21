from rest_framework import serializers
from stream.models import Movies, Streams

def name_length(value):
    if len(value)<2:
        raise serializers.ValidationError("Too Short name")

class MoviesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movies.object.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tagline = validated_data.get('description', instance.tagline)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance        


class StreamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Streams
        fields = "__all__"