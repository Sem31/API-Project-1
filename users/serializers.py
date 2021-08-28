from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='user-detail')

    class Meta:
        model = Profile
        fields = ('url', 'id', 'user', 'image')



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required=False)
    old_password = serializers.CharField(write_only = True, required=False)
    username = serializers.CharField(read_only = True, required=False)
    profile = ProfileSerializer(read_only = True)

    # logic to valid password
    def validate(self, data):
        request_method = self.context['request'].method
        password = data.get('password', None)
        if request_method == 'POST':
            if password == None:
                raise serializers.ValidationError({"info":"Please provide a PASSWORD!"})
        elif request_method == 'PUT' or request_method == 'PATCH':
            old_password = data.get('old_password', None)
            if password != None and old_password == None:
                raise serializers.ValidationError({"info":"Please provide the old password!"})
        return data


    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'password', 'old_password', 'profile']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_obj = User.objects.create(
            **validated_data
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

    def update(self, instance, validated_data):
        try:
            user  = instance
            if 'password' in validated_data:
                password = validated_data.pop('password')
                old_password = validated_data.pop('old_password')
                if user.check_password(old_password):
                    user.set_password(password)
                else:
                    raise Exception("Old Password is incorrect!")
                user.save()
        except Exception as err :
            raise serializers.ValidationError({'info': err})
        # re-call built in update method to update  --> email, first_name, last_name
        return super(UserSerializer, self).update(instance, validated_data)

        