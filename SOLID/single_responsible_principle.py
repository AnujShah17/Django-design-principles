# Single Responsible Principle


# Bad Example: A view class handling both database operations and response formatting
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()  # Handling database operation
        user_data = [
            {"id": user.id, "name": user.name} for user in users
        ]  # Handling response formatting
        return Response(user_data)


# Good Example: Separate responsibilities using services
# services.py
class UserService:
    @staticmethod
    def get_all_users():
        return User.objects.all()


# serializers.py
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name"]


# views.py
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = UserService.get_all_users()  # Only handling the view logic
        serializer = UserSerializer(users, many=True)  # Handling serialization
        return Response(serializer.data)
