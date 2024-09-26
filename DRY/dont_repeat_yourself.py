# DRY: Don't Repeat Yourself


# Bad Example: Separate views with duplicated logic for user registration and profile update
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Validate and save user data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Create new user
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        # Return validation errors if any
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()  # Get the user object to update
        # Validate and save updated user data
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()  # Update existing user
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Return validation errors if any
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Good Example: Use a mixin to encapsulate common logic for user handling
class UserViewMixin:
    serializer_class = UserSerializer

    def handle_user(self, request, user=None):
        # Validate and save user data (new or updated)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()  # Create or update user
            # Return serialized user data with appropriate status
            return Response(
                serializer.data,
                status=status.HTTP_200_OK if user else status.HTTP_201_CREATED,
            )
        # Return validation errors if any
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterUserView(UserViewMixin, generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        # Delegate to handle_user for registration
        return self.handle_user(request)


class UpdateUserProfileView(UserViewMixin, generics.UpdateAPIView):
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        user = self.get_object()  # Get the user object to update
        # Delegate to handle_user for profile update
        return self.handle_user(request, user)
