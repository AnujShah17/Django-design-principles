# KISS: Keep It Simple, Stupid!


# Bad Practice: Overly complex structure for managing blog posts
class BlogPostHandler:
    def __init__(self, data):
        self.data = data

    def validate(self):
        # Simulated complex validation logic
        if "title" not in self.data or "content" not in self.data:
            return False
        return True

    def save(self):
        # Simulate saving to the database
        return BlogPost.objects.create(**self.data)


class CreateBlogPostView(generics.CreateAPIView):
    serializer_class = BlogPostSerializer

    def create(self, request, *args, **kwargs):
        blog_post_handler = BlogPostHandler(request.data)

        # Unnecessarily complex validation and save process
        if blog_post_handler.validate():
            blog_post = blog_post_handler.save()
            return Response(
                self.serializer_class(blog_post).data, status=status.HTTP_201_CREATED
            )

        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


# Good Practice: Simple and direct blog post management
class CreateBlogPostView(generics.CreateAPIView):
    serializer_class = BlogPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Validate and save blog post data directly
        if serializer.is_valid():
            blog_post = serializer.save()
            return Response(
                self.serializer_class(blog_post).data, status=status.HTTP_201_CREATED
            )

        # Return validation errors if any
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
