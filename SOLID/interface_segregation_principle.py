# Interface Segregation Principle


# Bad Example: A large interface (serializer) forces clients to implement unused fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "address", "phone", "date_of_birth"]


# Good Example: Smaller, focused interfaces (serializers)
class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name"]


class DetailedUserSerializer(BasicUserSerializer):
    email = serializers.EmailField()
    address = serializers.CharField()
    phone = serializers.CharField()
    date_of_birth = serializers.DateField()


# Now clients can use either BasicUserSerializer or DetailedUserSerializer based on their needs
