# Django-design-principles
This repository serves as a comprehensive guide to the core design principles and best practices when developing with Django.

# Table of Contents
- [S - Single Responsibility Principle (SRP)](#s---single-responsibility-principle-srp)
- [O - Open/Closed Principle (OCP)](#o---openclosed-principle-ocp)
- [L - Liskov Substitution Principle (LSP)](#l---liskov-substitution-principle-lsp)
- [I - Interface Segregation Principle (ISP)](#i---interface-segregation-principle-isp)
- [D - Dependency Inversion Principle (DIP)](#d---dependency-inversion-principle-dip)
- [DRY: Don't Repeat Yourself](#dry-dont-repeat-yourself)
- [KISS: Keep It Simple, Stupid](#kiss-keep-it-simple-stupid)

# SOLID Principles in Django Rest Framework

The **SOLID** principles, coined by Robert C. Martin, provide a blueprint for better object-oriented design. When working with Django, particularly the Django Rest Framework (DRF), adhering to these principles helps in managing large, scalable applications.


## S - Single Responsibility Principle (SRP)
Every class should have only one job.  
In DRF, think of views, serializers, and models as playing distinct roles. A common pitfall is cramming too much logic into a view, which can make it hard to maintain. Following SRP ensures that your views handle requests, serializers deal with data transformation, and models manage the database layer.

**Key Example:** Instead of embedding business logic in your views, create services or utility functions to keep them slim. Your views should only be concerned with HTTP requests and responses.

## O - Open/Closed Principle (OCP)
Software entities should be open for extension, but closed for modification.  
This principle suggests that the behavior of a module should be extendable without altering its source code. In DRF, you might implement this with class-based views (CBVs), which can be extended and customized easily.

**Key Example:** Use CBVs like `ListAPIView` and `RetrieveAPIView`. If you need custom functionality, subclass them and override only the methods you need without modifying the core behavior.

## L - Liskov Substitution Principle (LSP)
Objects of a superclass should be replaceable with objects of a subclass.  
In DRF, LSP is about ensuring that your subclass views or serializers can stand in for their parent classes without breaking anything. If you're overriding a method, it should follow the contract of the base class.

**Key Example:** When subclassing `ModelSerializer`, ensure your custom serializer still works with all methods provided by `Serializer`, like `save()` and `validate()`, so it can substitute the original without causing issues.

## I - Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they don’t use.  
In Django Rest Framework, this principle could be translated into avoiding monolithic views or serializers that try to do too much. If different clients (say mobile vs web) need different data, create specific serializers and views tailored to those needs instead of bloated, one-size-fits-all ones.

## D - Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules.  
Instead of tightly coupling views to certain implementations, rely on abstractions. Dependency injection and using Django’s built-in generic functionality can help you avoid locking yourself into one specific way of doing things.

**Key Example:** In DRF, you can inject dependencies like third-party services or repositories via constructor or method parameters instead of hardcoding them inside your views or models.

## DRY: Don't Repeat Yourself
**DRY** is an essential principle for any Django developer. In DRF, this means avoiding duplicating code across serializers, views, or models.

### How to Keep Things DRY in DRF:
- **Use mixins:** DRF provides reusable mixins like `CreateModelMixin`, `UpdateModelMixin`, and `DestroyModelMixin`. These can be combined with generic views to avoid rewriting the same CRUD operations.
- **Reusable serializers:** Instead of creating a new serializer for every model, reuse a base serializer where applicable and add only necessary custom fields.
- **Signals:** If multiple views need to trigger the same event (like sending an email after object creation), avoid duplicating the logic in every view. Instead, use Django signals to handle this centrally.

**Note:** DRY isn’t just about reducing lines of code; it’s about making your code more maintainable. When you change something in one place, it should update across your application without hunting down duplicate logic.

## KISS: Keep It Simple, Stupid
In software development, KISS advocates for simplicity over complexity. Just because something can be done in a fancy way doesn’t mean it should be. DRF encourages simplicity with its out-of-the-box features, allowing developers to focus on what matters most: delivering functionality.

### Applying KISS in DRF:
- **Leverage DRF’s built-in classes:** Before you write custom logic, check if DRF already provides a solution. Features like `GenericAPIView`, `ModelViewSet`, and permission classes handle many common tasks.
- **Avoid over-engineering:** Don’t create complex inheritance chains for serializers or views when a simple function or method override will do. For example, use DRF’s `@action` decorator for custom routes instead of building a whole new view.

**Conclusion:** KISS keeps your codebase clean and easy to work with, especially for new developers joining the project.
