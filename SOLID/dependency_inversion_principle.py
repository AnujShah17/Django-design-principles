# Dependency Inversion Principle (DIP)


# Bad Example: OrderService directly depends on a concrete implementation of a payment processor
# NOTE: Here The OrderService is tightly coupled with PayPalProcessor, making it difficult to switch to another payment processor (like Stripe) without modifying the OrderService code.


# payment.py
class PayPalProcessor:
    def process_payment(self, amount):
        # Logic to process payment with PayPal
        print(f"Processing payment of {amount} with PayPal")


# services.py
class OrderService:
    def __init__(self):
        self.payment_processor = PayPalProcessor()

    def place_order(self, amount):
        self.payment_processor.process_payment(amount)
        print("Order placed successfully")


# views.py
class OrderView(APIView):
    def post(self, request):
        amount = request.data.get("amount")
        order_service = OrderService()
        order_service.place_order(amount)
        return Response({"message": "Order placed successfully"})


# Good Example: we create an abstraction for the payment processor, allowing for better decoupling
# NOTE: OrderService now depends on the PaymentProcessorInterface, not a concrete implementation. This allows any payment processor implementation to be used without changing the service logic.


# payment.py
class PaymentProcessorInterface(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class PayPalProcessor(PaymentProcessorInterface):
    def process_payment(self, amount):
        # Logic to process payment with PayPal
        print(f"Processing payment of {amount} with PayPal")


class StripeProcessor(PaymentProcessorInterface):
    def process_payment(self, amount):
        # Logic to process payment with Stripe
        print(f"Processing payment of {amount} with Stripe")


# services.py
class OrderService:
    def __init__(self, payment_processor: PaymentProcessorInterface):
        self.payment_processor = payment_processor

    def place_order(self, amount):
        self.payment_processor.process_payment(amount)
        print("Order placed successfully")


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import OrderService
from .payment import PayPalProcessor  # or import StripeProcessor for Stripe


class OrderView(APIView):
    def post(self, request):
        amount = request.data.get("amount")
        payment_processor = PayPalProcessor()  # Can switch to StripeProcessor as needed
        order_service = OrderService(payment_processor)
        order_service.place_order(amount)
        return Response({"message": "Order placed successfully"})
