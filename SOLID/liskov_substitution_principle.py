# Liskov Substitution Principle


# Bad Example: violates LSP by changing return types or method signatures, which breaks the client's expectations.
class BaseView(View):
    def get(self, request):
        return HttpResponse("Base view response")


class CustomView(BaseView):
    # Violating LSP by returning a non-HttpResponse object
    def get(self, request):
        return {"message": "Custom view response"}


# Good Example: respects LSP by maintaining consistency in behavior between the superclass and subclass, allowing them to be substituted without issues.
class BaseView(View):
    def get(self, request):
        return HttpResponse("Base view response")


class CustomView(BaseView):
    # Correctly following LSP by returning the expected response type
    def get(self, request):
        return HttpResponse("Custom view response")
