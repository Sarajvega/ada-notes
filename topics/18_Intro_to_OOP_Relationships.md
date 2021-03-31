
# OOP Relationships
  - Inheritance: A class relationship in which one class inherits attributes and behavior from another class. 
  - Parent Class: A class that contains variables and methods that can be inherited to other classes
  - Child Class: A class that contains its own variables and methods but also inherits the variables and methods from a parent class
    - A Child class can override parental behavior/states
  - Composition: A class relationship in which a class references other classes as instance variables and makes use of their methods and attributes.

Python has a special class named object. object is a class that defines the methods __init__, __str__, and a dozen other things. Every class and object eventually inherits from object.

## Composition: Instances Holding Instances

Composition means that one class is expected to have objects of another class stored or referenced inside of it. Composition between two classes describes a **composite class**sand a **component class**. The composite class contains at least one object of type **component class.**

In short: Composite class "has a" component class.

Example:
Angela wants to mimic other e-commerce sites. Angela's made a ShoppingCart class. As she builds the checkout method, she needs to calculate the total cost.  Products are complex objects, and they have their own class! Angela then wants to set up composition between these two classes. The ShoppingCart is the composite class, and it will have an attribute named products. products will be a list of Product instances, and Product is the component class.

## Inheritance
```python
# import ExampleParentClass <- that might be optional
class ExampleChildClass(ExampleParentClass):
    pass
```

## Replacing Inheritance

If a child class needs to replace the implementation of an inherited method, the child class can override the method by redefining it with the same name.

```python
class ExampleParentClass:
    def example_instance_method(self):
        print("I'm inside of ExampleParentClass!")

class ExampleChildClass(ExampleParentClass):
    def example_instance_method(self):
        print("I'm inside of ExampleChildClass!")
```

## super()
Calling super() returns a temp object of the parent class (also known as the superclass!). With this superclass, we can call all of the superclass's methods.

When to use?
1. The parent class has already implemented a behavior, and the child class wants to do that and more
2. The relationship between the child class and parent class is such that the child should always copy a behavior from the parent


