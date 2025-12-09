# 🏬 Shopping Mall Management System

A simple **console-based management application** for Shopping Malls built with **pure Python**, without external libraries.
The system provides full CRUD operations for Shops, Rental Agreements, and Maintenance Records while ensuring validation and data integrity.

---

## 🚀 Features

### 🏢 Shop Management

* Create shop
* List shops
* Update shop information
* Delete shop
* Validation rules (no negative prices, empty names, etc.)

### 📄 Rental Management

* Create rental for shop
* Auto-check availability
* Auto-calculate rental price (monthly × duration)
* Recalculate cost on date update
* End rental & auto mark shop AVAILABLE

### 🛠 Maintenance Records

* Add maintenance record
* Update cost/description/date
* View maintenance history

---

## 🔐 Business Rules

✔ shops cannot be rented if already RENTED
✔ prices can’t be negative
✔ dates must follow format YYYY-MM-DD
✔ rental cost auto-calculated
✔ update automatically recalculates total

---

## 📁 Project Structure

```
shopping_mall_management/
 │
 ├── src/
 │   ├── models/
 │   ├── services/
 │   ├── repositories/
 │   ├── exceptions/
 │   ├── main.py
 │
 ├── data/data.json
 ├── logs/system.log
 ├── tests/
 ├── README.md
 └── requirements.txt
```

---

## 💾 Data Storage

All system data is stored in:

```
data/data.json
```

and updated automatically without manual saving.

Logs are written into:

```
logs/system.log
```

---

## 🧪 Unit Tests

Project includes unittest test files:

```
tests/
  test_shop.py
  test_rental.py
  test_maintenance.py
```

---

## ⚙ Installation

Requirements:

* Python 3.8+
* No external dependencies

Install:

```bash
git clone <repository>
cd shopping_mall_management
```

Run:

```bash
python src/main.py
```

---

## 📦 Requirements

```txt
Python standard library only.
No external packages required.
```

---

## 📝 Technology Stack

| Component  | Technology         |
| ---------- | ------------------ |
| Language   | Python             |
| Storage    | JSON file          |
| UI         | Console            |
| Database   | None               |
| Frameworks | None (only stdlib) |

---

## 📚 What I learned building this

* Python OOP
* Clean folder organization
* Repository pattern
* Custom Exceptions
* Logging
* Data validation
* Using JSON as simple DB
* Unit testing with unittest

---

## 🔎 Example Console UI

```
=== SHOPPING MALL MANAGEMENT SYSTEM ===
1. Manage Shops
2. Manage Rentals
3. Manage Maintenance
0. Exit
```

---

## 👨‍💻 Who is this project for?

✔ beginner Python developers
✔ OOP learning projects
✔ University assignments
✔ JSON-based apps
✔ CRUD design practice

---

## 🏁 Future Improvements

* GUI version
* SQLite database
* Django REST API
* Web dashboard

---

## 📜 License

This project is free to use for learning purposes only.

---

## 📌 Author

Rufat and Ulvi
