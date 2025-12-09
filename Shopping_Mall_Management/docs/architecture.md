# Shopping Mall Management System - Architecture Document

## 1. Project Overview
This project is a console-based backend application designed for managing a Shopping Mall. The system handles Shops, Rentals, and Maintenance operations. The project strictly follows **OOP (Object-Oriented Programming)** and **SOLID** principles.

## 2. Layered Architecture
The project is divided into 4 main layers according to the "Separation of Concerns" principle:

### 1. Presentation Layer
*   **File:** `src/main.py`
*   **Function:** Handles user interaction (CLI Menu), receives input, and displays output. No business logic is implemented here.

### 2. Service Layer
*   **Folder:** `src/services/`
*   **Function:** Acts as the "brain" of the application. Responsible for data validation and applying business rules (e.g., a shop already rented cannot be rented again).

### 3. Data Access Layer
*   **Folder:** `src/repositories/`
*   **Function:** Uses the `Repository Pattern` to interact with the database (JSON file).
*   **Main Component:** `BaseRepository` for generic CRUD operations.

### 4. Domain Layer
*   **Folder:** `src/models/`
*   **Function:** Defines the main entities of the system (`Shop`, `Rental`, `Maintenance`) and their behaviors.

---

## 3. Implemented OOP Principles

### 3.1. Encapsulation
All models store internal variables as private (`self.__price`) and provide controlled access through `@property` getter/setter methods. Setters include validation (e.g., preventing negative prices).

### 3.2. Inheritance
*   **Models:** `Shop`, `Rental`, and `Maintenance` classes inherit from the abstract `BaseModel` class.
*   **Repositories:** `ShopRepository` and others inherit from `BaseRepository`.
*   **Exceptions:** All custom exceptions inherit from `BaseAppException`.

### 3.3. Polymorphism
The `add(item)` method in `BaseRepository` is polymorphic. It calls the `to_dict()` method regardless of whether the item is a Shop or Rental.

### 3.4. Abstraction
`BaseModel` (ABC - Abstract Base Class) enforces all models to implement `to_dict` and `from_dict` methods.

---

## 4. SOLID Principles

*   **SRP (Single Responsibility):** Each class has a single responsibility. For example, `Logger` only writes logs, `DataManager` only handles file reading/writing.
*   **OCP (Open/Closed):** The system is open for extension (new models can be added) but `BaseRepository` code does not need modification.
*   **LSP (Liskov Substitution):** Derived classes (`ShopRepository`) can replace their base class (`BaseRepository`) without issues.
*   **DIP (Dependency Inversion):** Services interact with abstract `Repository` objects, not directly with files (`open()`).

---

## 5. Data Storage

Data is stored in `data/data.json` in JSON format.  
Structure:

```json
{
  "shops": [ ... ],
  "rentals": [ ... ],
  "maintenance": [ ... ]
}

---

##  6. Exception Handling
The system implements a "Custom Exceptions" approach for error management. All exceptions inherit from the `BaseAppException` class:

* **`ValidationException`**: Raised when user input is invalid (e.g., negative price, empty name).  
* **`NotFoundException`**: Raised when the requested data is not found in the database (e.g., the ID to delete does not exist).  
* **`BusinessRuleException`**: Raised when business rules are violated (e.g., attempting to rent a shop that is already rented).

These exceptions are raised in the `src/services` layer and caught centrally in `src/main.py` using try-except blocks to display readable messages to the user.
