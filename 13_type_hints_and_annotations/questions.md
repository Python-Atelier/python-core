# 🐍 Type Hints and Annotations - Questions

> **Master modern Python's type system for better code quality!** 🎯

---

## 🏷️ **Question Categories**

- 🟢 **🟢 Basic** - Foundational type hints
- 🟡 **🟡 Intermediate** - Advanced annotations
- 🟠 **🟠 Advanced** - Complex type scenarios
- 🔴 **🔴 Expert** - Real-world applications

---

## 🟢 **Basic Level Questions** (1-6)

### Question 1: Basic Type Annotations ⭐

**⏱️ Time Estimate:** 8 minutes  
**🎯 Category:** Basic Types  
**📝 Skills Tested:** Function annotations, basic types

**Task:** Add type hints to simple functions that work with basic data types.

**Real-life Scenario:** You're refactoring a legacy codebase to add type safety:

- Add type hints to a function that calculates area of a rectangle
- Add type hints to a function that concatenates user names
- Add type hints to a function that checks if a number is positive

**Think about:**

- What types should you use for numbers, strings, and booleans?
- How do you specify return types for functions?
- What happens when you don't specify types?

**Challenge yourself:**

- Can you add type hints to functions with multiple parameters?
- What if you need to handle optional parameters?

**If you can't solve this, review:** Python basic types, function definition syntax

**💡 Pro Tip:** Use `from typing import *` to access advanced type hints!

---

### Question 2: Type Hints for Collections ⭐

**⏱️ Time Estimate:** 10 minutes  
**🎯 Category:** Collections  
**📝 Skills Tested:** List, dict, tuple annotations

**Task:** Add type hints to functions that work with lists, dictionaries, and tuples.

**Real-life Scenario:** You're building a data processing pipeline:

- Function that processes a list of user IDs
- Function that creates a dictionary mapping names to ages
- Function that returns coordinates as a tuple

**Think about:**

- How do you specify the type of elements in a list?
- What's the difference between `List` and `list`?
- How do you type hint dictionaries with specific key/value types?

**Challenge yourself:**

- Can you create type hints for nested collections?
- What if you need to handle empty collections?

**If you can't solve this, review:** Python collections, typing module basics

**📝 Remember:** Use `List[int]` not `list[int]` for Python < 3.9!

---

### Question 3: Optional and Union Types ⭐⭐

**⏱️ Time Estimate:** 12 minutes  
**🎯 Category:** Advanced Types  
**📝 Skills Tested:** Optional, Union, None handling

**Task:** Use Optional and Union types to handle nullable values and multiple types.

**Real-life Scenario:** You're building an API that handles user data:

- Function that might return a user object or None
- Function that accepts either string or integer IDs
- Function that processes optional configuration parameters

**Think about:**

- When should you use `Optional[T]` vs `Union[T, None]`?
- How do you handle functions that can return different types?
- What's the relationship between Optional and Union?

**Challenge yourself:**

- Can you create a function that accepts multiple optional parameters?
- What if you need to handle more than two possible types?

**If you can't solve this, review:** Optional types, Union types, None handling

**🎯 Key Point:** `Optional[T]` is equivalent to `Union[T, None]`!

---

### Question 4: Type Aliases and NewType ⭐⭐

**⏱️ Time Estimate:** 15 minutes  
**🎯 Category:** Type Definitions  
**📝 Skills Tested:** Type aliases, NewType, custom types

**Task:** Create type aliases and NewType definitions for better code readability.

**Real-life Scenario:** You're building a financial application:

- Create type aliases for common financial types (Amount, Currency, etc.)
- Use NewType to create distinct types for different IDs
- Define custom types for domain-specific concepts

**Think about:**

- When should you use type aliases vs NewType?
- How do type aliases improve code readability?
- What's the difference between type aliases and inheritance?

**Challenge yourself:**

- Can you create a type alias for a complex nested structure?
- What if you need to create types that are distinct but compatible?

**If you can't solve this, review:** Type aliases, NewType, domain modeling

**💡 Pro Tip:** Use NewType when you want distinct types that can't be mixed up!

---

### Question 5: Generic Types ⭐⭐⭐

**⏱️ Time Estimate:** 18 minutes  
**🎯 Category:** Generics  
**📝 Skills Tested:** Generic functions, type variables

**Task:** Create generic functions and classes that work with multiple types.

**Real-life Scenario:** You're building a data processing library:

- Generic function that finds the maximum element in any sequence
- Generic class that represents a container of any type
- Generic function that transforms data of any type

**Think about:**

- How do you define type variables for generics?
- What are the different kinds of type variables (T, K, V)?
- How do you constrain generic types?

**Challenge yourself:**

- Can you create a generic function with multiple type parameters?
- What if you need to constrain types to specific base classes?

**If you can't solve this, review:** Generic programming, type variables, constraints

**⚡ Remember:** Use `TypeVar` to create type variables for generics!

---

### Question 6: Callable and Protocol Types ⭐⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** Advanced Types  
**📝 Skills Tested:** Callable, Protocol, structural typing

**Task:** Use Callable and Protocol types for function signatures and structural typing.

**Real-life Scenario:** You're building a plugin system:

- Define callable types for different plugin functions
- Use Protocol to define interfaces for plugin objects
- Create structural types for configuration objects

**Think about:**

- How do you specify function signatures with Callable?
- What's the difference between Protocol and abstract base classes?
- When should you use structural vs nominal typing?

**Challenge yourself:**

- Can you create a Protocol that defines a complete interface?
- What if you need to handle functions with complex signatures?

**If you can't solve this, review:** Callable types, Protocol, structural typing

**🎯 Key Concept:** Protocols enable structural typing - "duck typing" with type safety!

---

## 🟡 **Intermediate Level Questions** (7-12)

### Question 7: Type Hints for Classes ⭐⭐

**⏱️ Time Estimate:** 15 minutes  
**🎯 Category:** OOP  
**📝 Skills Tested:** Class annotations, method types

**Task:** Add type hints to class attributes, methods, and properties.

**Real-life Scenario:** You're refactoring a class-based API:

- Add type hints to class attributes and methods
- Type hint class properties and getters/setters
- Handle inheritance with proper type annotations

**Think about:**

- How do you type hint class attributes?
- What's the difference between instance and class methods?
- How do you handle self and cls parameters?

**Challenge yourself:**

- Can you create a generic base class with type hints?
- What if you need to handle abstract methods?

**If you can't solve this, review:** Class definition, method types, inheritance

**🏗️ Remember:** Use `ClassVar` for class-level attributes!

---

### Question 8: Type Hints for Exceptions ⭐⭐

**⏱️ Time Estimate:** 12 minutes  
**🎯 Category:** Error Handling  
**📝 Skills Tested:** Exception types, error handling

**Task:** Add type hints to functions that raise or handle exceptions.

**Real-life Scenario:** You're building a robust error handling system:

- Type hint functions that raise specific exceptions
- Handle functions that might raise different exception types
- Create custom exception types with proper annotations

**Think about:**

- How do you indicate that a function might raise an exception?
- What's the difference between `NoReturn` and `None`?
- How do you type hint exception handlers?

**Challenge yourself:**

- Can you create a function that raises different exceptions based on conditions?
- What if you need to handle exception hierarchies?

**If you can't solve this, review:** Exception handling, NoReturn type

**⚠️ Note:** Python doesn't have checked exceptions, but you can document them!

---

### Question 9: Type Hints for Context Managers ⭐⭐

**⏱️ Time Estimate:** 15 minutes  
**🎯 Category:** Context Managers  
**📝 Skills Tested:** Context manager types, with statements

**Task:** Add type hints to context manager classes and functions.

**Real-life Scenario:** You're building resource management utilities:

- Type hint a context manager for database connections
- Create a generic context manager for any resource
- Handle context managers that return values

**Think about:**

- What methods do context managers need?
- How do you type hint the `__enter__` and `__exit__` methods?
- What's the return type of a context manager?

**Challenge yourself:**

- Can you create an async context manager with type hints?
- What if you need to handle context managers with complex state?

**If you can't solve this, review:** Context managers, Protocol types

**🔄 Remember:** Context managers implement the context manager protocol!

---

### Question 10: Type Hints for Decorators ⭐⭐⭐

**⏱️ Time Estimate:** 18 minutes  
**🎯 Category:** Decorators  
**📝 Skills Tested:** Decorator types, function wrapping

**Task:** Add type hints to decorator functions and classes.

**Real-life Scenario:** You're building a decorator library:

- Type hint a simple function decorator
- Create a decorator that accepts parameters
- Handle decorators that modify function signatures

**Think about:**

- How do you preserve the original function's type signature?
- What's the difference between function and class decorators?
- How do you handle decorators with parameters?

**Challenge yourself:**

- Can you create a generic decorator that works with any function?
- What if you need to handle decorators that change return types?

**If you can't solve this, review:** Decorators, Callable types, type preservation

**🎨 Pro Tip:** Use `Callable` and `TypeVar` to preserve function signatures!

---

### Question 11: Type Hints for Async Functions ⭐⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** Async Programming  
**📝 Skills Tested:** Async types, coroutines

**Task:** Add type hints to async functions and coroutines.

**Real-life Scenario:** You're building an async web API:

- Type hint async functions that return data
- Handle async functions that yield values
- Create type hints for async context managers

**Think about:**

- How do you type hint async functions?
- What's the difference between `Awaitable` and `Coroutine`?
- How do you handle async generators?

**Challenge yourself:**

- Can you create a generic async function with type hints?
- What if you need to handle complex async workflows?

**If you can't solve this, review:** Async programming, coroutines, awaitables

**⚡ Remember:** Use `Awaitable[T]` for async functions that return T!

---

### Question 12: Type Hints for Dataclasses ⭐⭐⭐

**⏱️ Time Estimate:** 15 minutes  
**🎯 Category:** Modern OOP  
**📝 Skills Tested:** Dataclass types, field annotations

**Task:** Create dataclasses with proper type hints and field annotations.

**Real-life Scenario:** You're building a data model for a web application:

- Create dataclasses for user data with type hints
- Use field annotations for default values and validation
- Handle inheritance with dataclasses

**Think about:**

- How do dataclasses automatically generate type hints?
- What's the difference between `field()` and direct assignment?
- How do you handle optional fields in dataclasses?

**Challenge yourself:**

- Can you create a generic dataclass that works with different types?
- What if you need to add custom methods to dataclasses?

**If you can't solve this, review:** Dataclasses, field annotations, type hints

**🏗️ Pro Tip:** Dataclasses automatically generate `__init__`, `__repr__`, and more!

---

## 🟠 **Advanced Level Questions** (13-17)

### Question 13: Type Hints for Complex Data Structures ⭐⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Advanced Types  
**📝 Skills Tested:** Nested types, complex structures

**Task:** Create type hints for complex nested data structures.

**Real-life Scenario:** You're building a configuration system:

- Type hint deeply nested dictionaries and lists
- Create types for JSON-like data structures
- Handle recursive data structures

**Think about:**

- How do you handle deeply nested types?
- What's the difference between `Dict` and `TypedDict`?
- How do you handle recursive types?

**Challenge yourself:**

- Can you create a type for a complex API response structure?
- What if you need to handle dynamic data structures?

**If you can't solve this, review:** TypedDict, recursive types, complex structures

**📊 Remember:** Use `TypedDict` for dictionary-like structures with known keys!

---

### Question 14: Type Hints for Metaclasses ⭐⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Metaclasses  
**📝 Skills Tested:** Metaclass types, class creation

**Task:** Add type hints to metaclasses and class creation functions.

**Real-life Scenario:** You're building a framework with custom class creation:

- Type hint a metaclass that modifies class creation
- Create type hints for class factory functions
- Handle metaclasses with complex type parameters

**Think about:**

- How do you type hint metaclasses?
- What's the relationship between metaclasses and generic types?
- How do you handle class creation hooks?

**Challenge yourself:**

- Can you create a generic metaclass with type hints?
- What if you need to handle multiple inheritance with metaclasses?

**If you can't solve this, review:** Metaclasses, class creation, type system

**🔧 Pro Tip:** Metaclasses are classes that create classes!

---

### Question 15: Type Hints for Descriptors ⭐⭐⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Descriptors  
**📝 Skills Tested:** Descriptor types, property-like objects

**Task:** Add type hints to descriptor classes and property-like objects.

**Real-life Scenario:** You're building a validation framework:

- Type hint descriptor classes for data validation
- Create type hints for computed properties
- Handle descriptors with complex logic

**Think about:**

- How do you type hint descriptor methods?
- What's the difference between data and non-data descriptors?
- How do you handle descriptors with parameters?

**Challenge yourself:**

- Can you create a generic descriptor that works with different types?
- What if you need to handle descriptors with side effects?

**If you can't solve this, review:** Descriptors, property types, validation

**🎯 Remember:** Descriptors control attribute access and modification!

---

### Question 16: Type Hints for Abstract Base Classes ⭐⭐⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** ABCs  
**📝 Skills Tested:** Abstract types, interface definitions

**Task:** Create abstract base classes with proper type hints.

**Real-life Scenario:** You're building a plugin architecture:

- Create abstract base classes for plugin interfaces
- Type hint abstract methods and properties
- Handle multiple inheritance with ABCs

**Think about:**

- How do you type hint abstract methods?
- What's the difference between ABCs and Protocols?
- How do you handle abstract properties?

**Challenge yourself:**

- Can you create a generic abstract base class?
- What if you need to handle abstract class methods?

**If you can't solve this, review:** Abstract base classes, interface design

**🏗️ Pro Tip:** Use ABCs when you need to enforce interface contracts!

---

### Question 17: Type Hints for Performance Optimization ⭐⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Performance  
**📝 Skills Tested:** Performance types, optimization

**Task:** Use type hints to optimize code performance and catch errors early.

**Real-life Scenario:** You're optimizing a high-performance application:

- Use type hints to enable compiler optimizations
- Create type hints for memory-efficient data structures
- Handle performance-critical code paths

**Think about:**

- How do type hints affect runtime performance?
- What's the relationship between types and memory usage?
- How do you handle performance-critical type checking?

**Challenge yourself:**

- Can you create type hints that enable specific optimizations?
- What if you need to balance type safety with performance?

**If you can't solve this, review:** Performance optimization, type checking overhead

**⚡ Remember:** Type hints are removed at runtime but help with static analysis!

---

## 🔴 **Expert Level Questions** (18-20)

### Question 18: Type Hints for Machine Learning Pipelines ⭐⭐⭐⭐⭐

**⏱️ Time Estimate:** 45 minutes  
**🎯 Category:** ML/AI  
**📝 Skills Tested:** Complex ML types, pipeline design

**Task:** Create comprehensive type hints for a machine learning pipeline.

**Real-life Scenario:** You're building a production ML system:

- Type hint data preprocessing functions
- Create types for model inputs and outputs
- Handle complex ML data structures (tensors, arrays)

**Think about:**

- How do you type hint numpy arrays and pandas DataFrames?
- What types should you use for model predictions?
- How do you handle different data formats?

**Challenge yourself:**

- Can you create a generic ML pipeline that works with different models?
- What if you need to handle streaming data processing?

**If you can't solve this, review:** ML libraries, data types, pipeline design

**🤖 Pro Tip:** Use `numpy.typing` and `pandas-stubs` for better ML type support!

---

### Question 19: Type Hints for Web Framework Integration ⭐⭐⭐⭐⭐

**⏱️ Time Estimate:** 40 minutes  
**🎯 Category:** Web Development  
**📝 Skills Tested:** Web types, framework integration

**Task:** Create type hints for a web application with FastAPI/Django.

**Real-life Scenario:** You're building a type-safe web API:

- Type hint API endpoints and request/response models
- Create types for database models and serialization
- Handle authentication and authorization types

**Think about:**

- How do you type hint HTTP requests and responses?
- What types should you use for database queries?
- How do you handle API versioning with types?

**Challenge yourself:**

- Can you create a generic API client with type hints?
- What if you need to handle complex API workflows?

**If you can't solve this, review:** Web frameworks, API design, database types

**🌐 Remember:** Modern web frameworks have excellent type hint support!

---

### Question 20: Type Hints for Distributed Systems ⭐⭐⭐⭐⭐

**⏱️ Time Estimate:** 50 minutes  
**🎯 Category:** Distributed Systems  
**📝 Skills Tested:** Distributed types, message passing

**Task:** Create type hints for a distributed system with message passing.

**Real-life Scenario:** You're building a microservices architecture:

- Type hint message formats and protocols
- Create types for service discovery and communication
- Handle distributed state and consistency

**Think about:**

- How do you type hint network messages?
- What types should you use for distributed state?
- How do you handle serialization and deserialization?

**Challenge yourself:**

- Can you create a type-safe RPC system?
- What if you need to handle complex distributed workflows?

**If you can't solve this, review:** Distributed systems, message passing, serialization

**🌍 Pro Tip:** Use Protocol Buffers or similar for type-safe message serialization!

---

## 🎯 **Learning Path Summary**

### **Week 1: Foundation** 🟢

- Basic type annotations
- Collection types
- Optional and Union types

### **Week 2: Intermediate** 🟡

- Type aliases and NewType
- Generic types
- Callable and Protocol types

### **Week 3: Advanced** 🟠

- Complex data structures
- Metaclasses and descriptors
- Performance optimization

### **Week 4: Expert** 🔴

- Real-world applications
- Framework integration
- Distributed systems

---

## 🛠️ **Essential Tools & Resources**

### **Type Checking Tools**

- **mypy** - Static type checker
- **pyright** - Microsoft's type checker
- **pyre** - Facebook's type checker

### **IDE Support**

- **PyCharm** - Excellent type hint support
- **VS Code** - Great with Python extension
- **Jupyter** - Type hints in notebooks

### **Documentation**

- [PEP 484](https://peps.python.org/pep-0484/) - Type hints specification
- [mypy documentation](https://mypy.readthedocs.io/)
- [typing module docs](https://docs.python.org/3/library/typing.html)

---

## 🆕 **Additional Practice Questions** (31-35)

### Question 31: Modern Type System Features and Advanced Annotations ⭐⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Modern Type System  
**📝 Skills Tested:** Modern type features, advanced annotations, type system

**Task:** Use modern type system features and advanced type annotations.

**Real-life Scenario:** You're building a type-safe data processing library:
- Use modern type features like Literal and Final
- Implement advanced type annotations
- Handle complex type relationships
- Build type-safe APIs

**Think about:**
- How do modern type features improve code quality?
- When should you use advanced type annotations?
- How do you handle complex type relationships?

**Challenge yourself:**
- Can you implement a type-safe configuration system?
- What if you need to handle complex type hierarchies?

**If you can't solve this, review:** Modern type features, advanced annotations, type system

**🎯 Modern Types:** Use advanced type features for better code quality!

---

### Question 32: Type Parameters and Generic Programming ⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Generic Programming  
**📝 Skills Tested:** Type parameters, generics, type constraints

**Task:** Use type parameters and generics to create reusable, type-safe code.

**Real-life Scenario:** You're building a generic data structure library:
- Create generic data structures
- Implement type constraints and bounds
- Handle complex type relationships
- Build reusable components

**Think about:**
- How do type parameters improve code reusability?
- When should you use generics vs specific types?
- How do you handle type constraints?

**Challenge yourself:**
- Can you implement a generic database ORM?
- What if you need to handle complex type relationships?

**If you can't solve this, review:** Type parameters, generics, type constraints

**🔧 Generic Programming:** Write reusable code with type parameters!

---

### Question 33: Type Guards and Runtime Type Checking ⭐⭐⭐

**⏱️ Time Estimate:** 35 minutes  
**🎯 Category:** Runtime Type Checking  
**📝 Skills Tested:** Type guards, runtime checking, type validation

**Task:** Implement type guards and runtime type checking for dynamic data.

**Real-life Scenario:** You're building a data validation system:
- Implement type guards for runtime checking
- Handle dynamic data validation
- Create type-safe data processing
- Build comprehensive validation systems

**Think about:**
- How do you implement effective type guards?
- When should you use runtime type checking?
- How do you handle dynamic data validation?

**Challenge yourself:**
- Can you implement a dynamic type system?
- What if you need to handle complex data schemas?

**If you can't solve this, review:** Type guards, runtime checking, type validation

**🛡️ Type Safety:** Ensure type safety at runtime with type guards!

---

### Question 34: Advanced Type Patterns and Metaprogramming ⭐⭐⭐⭐

**⏱️ Time Estimate:** 40 minutes  
**🎯 Category:** Advanced Patterns  
**📝 Skills Tested:** Advanced patterns, metaprogramming, type generation

**Task:** Implement advanced type patterns and metaprogramming with types.

**Real-life Scenario:** You're building a code generation framework:
- Generate types dynamically
- Implement advanced type patterns
- Handle complex type transformations
- Build domain-specific type systems

**Think about:**
- How do you generate types dynamically?
- What are the advanced patterns for type metaprogramming?
- How do you handle complex type transformations?

**Challenge yourself:**
- Can you implement a type generator?
- What if you need to handle types across different languages?

**If you can't solve this, review:** Advanced patterns, metaprogramming, type generation

**🔮 Metaprogramming:** Generate types dynamically with metaprogramming!

---

### Question 35: Type System Integration and Tooling ⭐⭐⭐⭐

**⏱️ Time Estimate:** 45 minutes  
**🎯 Category:** Tooling and Integration  
**📝 Skills Tested:** Type system integration, tooling, IDE support

**Task:** Integrate type systems with development tools and build systems.

**Real-life Scenario:** You're building a development environment:
- Integrate type checking with build systems
- Implement IDE support for types
- Handle type system tooling
- Build comprehensive development workflows

**Think about:**
- How do you integrate type systems with tools?
- What are the best practices for type system tooling?
- How do you handle type system integration?

**Challenge yourself:**
- Can you implement a custom type checker?
- What if you need to handle types across different tools?

**If you can't solve this, review:** Type system integration, tooling, IDE support

**🛠️ Tooling:** Integrate type systems with development tools!

---

## 🎯 **Updated Study Progress Summary**

### 📈 **Completion Status:**

- 🟢 **Basic Level:** 0/6 completed
- 🟡 **Intermediate Level:** 0/6 completed
- 🟠 **Advanced Level:** 0/5 completed
- 🔴 **Expert Level:** 0/3 completed
- 🆕 **Additional Practice:** 0/10 completed

### ⏱️ **Total Estimated Time:** 25 hours 15 minutes

### 🎓 **Next Steps:**

1. Start with Basic Level questions (1-6)
2. Move to Intermediate when comfortable
3. Challenge yourself with Advanced concepts
4. Master Expert level for real-world scenarios
5. Practice with Additional Questions (21-35) featuring modern Python features

---

> **💡 Pro Tip:** Modern Python features like type parameters and advanced type patterns make type systems more powerful and flexible!

---

**Ready to master Python's type system? Start with the basic questions and work your way up!** 🚀
