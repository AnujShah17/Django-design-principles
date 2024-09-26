# Open-Closed Principle


# Bad Example: Modifying existing code to add new functionality
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name"]


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        # Adding new feature by modifying existing function
        user_data = [
            {"id": user.id, "name": user.name, "extra_info": "new"} for user in users
        ]
        return Response(user_data)


# Good Example: Extending functionality by subclassing or composing existing classes
class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name"]


# Extending functionality by subclassing
class ExtendedUserSerializer(BaseUserSerializer):
    extra_info = serializers.SerializerMethodField()

    def get_extra_info(self, obj):
        return "new"


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = ExtendedUserSerializer(
            users, many=True
        )  # Use the extended serializer
        return Response(serializer.data)
