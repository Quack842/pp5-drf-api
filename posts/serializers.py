from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 11:
            raise serializers.ValidationError(
                'Image Size is Larger than 11MB'
            )
        if value.image.width > 6020:
            raise serializers.ValidationError(
                'Image width is Larger than 6020px'
            )
        if value.image.height > 4010:
            raise serializers.ValidationError(
                'Image height is Larger than 4010px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'camera_type',
            'photo_type'
        ]
