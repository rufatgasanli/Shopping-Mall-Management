# User Guide - Shopping Mall Management System

## 1. Introduction
Welcome to the Shopping Mall Management System. This is a console-based application designed to help administrators manage **Shops**, **Rental Agreements**, and **Maintenance Records** efficiently. The system ensures data integrity using strict validation rules and saves all data automatically.

---

## 2. Prerequisites & Installation

### Requirements
* **Python 3.8** or higher installed on your computer.
* No external libraries are required (uses Python Standard Library).

### Setup
1. Download or extract the project folder `shopping_mall_management`.
2. Open your Terminal (Mac/Linux) or Command Prompt (Windows).
3. Navigate to the project directory:
    ```bash
    cd path/to/shopping_mall_management
    ```

---

## 3. How to Run the Application
To start the program, run the following command inside the project directory:

```bash
python src/main.py

Note: On some systems, you might need to use python3 src/main.py.

4. Features & Usage Guide

Upon starting, you will see the Main Menu:

=== SHOPPING MALL MANAGEMENT SYSTEM ===
1. Manage Shops
2. Manage Rentals
3. Manage Maintenance
0. Exit
Select:

### A. Managing Shops (Option 1)
Here you can register new physical shop units.

* **Add Shop:** Enter a unique ID, Name, Owner, Category, and Monthly Rent Price.  
  **Validation:** Price cannot be negative. Name cannot be empty.

* **List Shops:** Displays all shops with their status (AVAILABLE or RENTED).

* **Update Shop:** Enter the Shop ID. Press Enter to skip fields you don't want to change. Enter new values for fields you want to update. *




 **Delete Shop:** Removes a shop from the system.

---

### B. Managing Rentals (Option 2)
Here you can lease shops to tenants.

* **Create Rental:**
  * Enter a unique Rental ID.
  * Enter the Shop ID (Must be an existing shop).
  * Enter Tenant Name, Start Date, and End Date (Format: YYYY-MM-DD).  
    **Rule:** You cannot rent a shop that is already marked as RENTED.  
    **Automatic Calculation:** The system calculates Total Cost based on duration (months × shop price).

* **List Rentals:** View all active lease agreements.

* **Update Rental:** Change the Tenant name or Dates.  
  **Note:** If you change dates, the Total Cost will be automatically recalculated.

* **End Rental (Delete):** Terminates the contract and automatically marks the Shop as AVAILABLE again.

---

### C. Managing Maintenance (Option 3)
Here you can log repair or service costs.

* **Add Record:** Enter Record ID, Shop ID, Description, Date, and Cost.

* **List Records:** View history of maintenance.

* **Update Record:** Modify details of an existing maintenance record.

---

## 5. Important Rules & Error Handling
The system is designed to prevent errors:

* **Invalid Input:** If you enter a negative price (e.g., -500), the system will show a Validation Error and cancel the operation.

* **Business Rules:** If you try to rent a shop that is already occupied, the system will show a Business Rule Violation error.

* **Data Format:** Dates must be entered in YYYY-MM-DD format (e.g., 2024-05-20).

---

## 6. Data & Logs
* **Data Storage:** All your data is automatically saved in `data/data.json`. You do not need to save manually.

* **Logs:** All operations (creations, updates, errors) are recorded in `logs/system.log` with timestamps. Check this file if you encounter issues.

---

## 7. Troubleshooting
**Q:** The program crashes immediately.  
**A:** Ensure you are running the command from the root folder, not inside `src/`.

**Q:** I manually edited `data.json` and now it won't work.  
**A:** If the JSON file is corrupted, delete `data/data.json`. The program will create a fresh new one on the next start.

