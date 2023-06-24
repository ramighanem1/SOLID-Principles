# SOLID Principles 


SOLID Principles is a set of five design principles that help in creating software systems that are easy to maintain, understand, and extend. These principles were introduced by Robert C. Martin (also known as Uncle Bob) and are widely adopted in object-oriented programming.


## Single Responsibility Principle (SRP)

The Single Responsibility Principle states that a class should have only one reason to change. In other words, a class should have a single responsibility or be focused on doing one thing well. This principle encourages a class to have a clear and well-defined purpose, making it easier to understand, maintain, and test. By adhering to SRP, you can minimize the impact of changes and prevent cascading failures when modifying the code.

[ single responsibility principle code examples ](./Code/SingleResponsibilityPrinciple.py)

## Open-Closed Principle (OCP)
The Open-Closed Principle states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that you should design your code in a way that allows adding new functionality without modifying existing code. By using abstractions, interfaces, and inheritance, you can introduce new behavior through extension rather than modification. This principle promotes code reuse, maintainability, and the ability to adapt to changing requirements.

[ Open Closed Principle code examples ](./Code/OpenClosedPrinciple.py)

## Liskov Substitution Principle (LSP)
The Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. In simpler terms, if a class is a subtype of another class, it should be able to substitute the parent class without causing any issues. This principle ensures that inheritance hierarchies are well-designed and adhere to the "is-a" relationship. Violating the LSP can lead to unexpected behavior and errors when using polymorphism.

[ Liskov Substitution Principle code examples ](./Code/LiskovSubstitutionPrinciple.py)

## Interface Segregation Principle (ISP)
The Interface Segregation Principle states that clients should not be forced to depend on interfaces they do not use. It promotes the idea of creating smaller, cohesive interfaces tailored to the needs of the clients. This principle avoids "fat" interfaces that contain more methods than necessary, as it can lead to unnecessary dependencies and potential implementation issues. By segregating interfaces, you increase modularity, reduce coupling, and improve the maintainability of your code.

[ Interface Segregation Principle code examples ](./Code/InterfaceSegregationPrinciple.py)

## Dependency Inversion Principle (DIP)
The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. Additionally, abstractions should not depend on details; details should depend on abstractions. This principle promotes loose coupling between modules and allows for flexibility and extensibility in your code. By depending on abstractions, you can easily switch implementations, inject dependencies, and create modular systems that are easier to test and maintain.

[ Dependency Inversion Principle code examples ](./Code/DependencyInversionPrinciple.py)