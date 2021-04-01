# Compositon
- One-to-one: One composite object is associated with one component object
- One-to-many: One composite object is associated with a collection of component objects.

## Initializing Components as Attributes in the Constructor

We can set attributes of composite class to component instances. 

Example:
```python
class ExampleComponent:

    def __init__(self, name):
        self.name = name

class ExampleComposite:

    def __init__(self, name, component):
        self.name = name
        self.my_favorite_component = component

apple = ExampleComponent("apple")

orange = ExampleComposite("orange", apple)

print("Orange has an attr named my_favorite_component:", orange.my_favorite_component)
print("We can read the name from Orange's fav component using dot notation:", orange.my_favorite_component.name)
```

If we have a list of instances (which expresses a one-to-many composition relationship): 
```python
class ExampleComponent:

    def __init__(self, name):
        self.name = name


class ExampleComposite:

    def __init__(self, name, components):
        self.name = name
        self.components = components

apple = ExampleComponent("apple")
banana = ExampleComponent("banana")
mango = ExampleComponent("mango")

orange = ExampleComposite("orange", [apple, banana, mango])

print("Orange has an attr named components:", orange.components)
print("We can read the name from Orange's components:")

for fruit in orange.components:
    print(fruit.name)

```

## Composition Lets Us Read Component Properties

```python

import random

class ExampleComponent:

    def __init__(self, name):
        self.name = name

    def get_random_num(self):
        print("***************************************************")
        print("I'm inside Component's instance method get_random_num")
        random_num = random.randint(0, 999)
        print("Now, I'm going to leave Component's instance method")
        print("***************************************************")
        return random_num

class ExampleComposite:

    def __init__(self, name, component):
        self.name = name
        self.component = component

    def read_fruits(self):
        print("I'm inside Composite's instance method read_fruits")
        print("I can read self.component here:", self.component)
        print("Now, I'm going to call self.component's instance method")

        result_from_component = self.component.get_random_num()

        print("This is what Component's method returned:", result_from_component)

mango = ExampleComponent("mango")
orange = ExampleComposite("orange", mango)

orange.read_fruits()
```

We should observe:

ExampleComposite...
- has an attribute component
- has an instance method read_fruits. Inside read_fruits:
- we print that we're inside it, and we read the component attr
- we call the component attr's instance method, get_random_num with the line self.component.get_random_num()
- we print the return value from that instance method

ExampleComponent...
- has an instance method get_random_num. Inside get_random_num:
- we print that we're inside it
- we produce and return a random number

## One-to-One and One-to-Many Composition Relationships

A one-to-one relationship is a relationship in which a composite class has an attribute representing a single instance of a component class:
```python
class ExampleComponent:

    def __init__(self, name):
        self.name = name

class ExampleComposite:

    def __init__(self, name, component):
        self.name = name
        self.component = component
```

A one-to-many relationship is a relationship in which a composite class has an attribute representing a list of instances of a component class as in this example:

```python
class ExampleComposite:

    def __init__(self, name, components):
        self.name = name
        self.components = components
```
^^ Components would be a list of components. 

