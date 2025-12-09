# Database Schema (JSON Structure)

## 1. Overview
The application uses a flat file database system implemented via a JSON file.
*   **File Path:** `data/data.json`
*   **Format:** Standard JSON (JavaScript Object Notation)
*   **Encoding:** UTF-8

## 2. Root Structure
The database consists of a single root object containing three main arrays (collections):

```json
{
  "shops": [ ... ],
  "rentals": [ ... ],
  "maintenance": [ ... ]
}

3. Data Models & Fields

A. Shops Collection ("shops")

Stores information about physical shop units in the mall.

Field Name   	Data Type	        Description	                            Constraints
shop_id	        String (PK)	        Unique identifier for the shop	        Unique, Not Null
name	        String	            Name of the shop	                    Not Null
owner	        String	            Name of the shop owner	                -
category	    String	            Type of business (Clothing, Food, etc.)	-
price	        Float	            Monthly rental price	                Must be >= 0
is_rented	    Boolean	            Current rental status	                True / False


B. Rentals Collection ("rentals")

Stores active lease agreements between the mall and tenants.

Field Name	        Data Type	        Description	                                Constraints
rental_id	        String (PK)	        Unique identifier for the rental agreement	Unique, Not Null
shop_id	            String (FK)	        Reference to the shops collection	        Must exist in shops
tenant	            String	            Name of the tenant leasing the shop	        Not Null
start_date	        String	            Lease start date (ISO 8601)	                Format: YYYY-MM-DD
end_date	        String	            Lease end date (ISO 8601)	                Format: YYYY-MM-DD
monthly_price	    Float	            Locked price per month at time of rental	Must be >= 0
total_cost	        Float	            Calculated total (Months × Price)	        Auto-calculated


C. Maintenance Collection ("maintenance")

Stores records of repairs and maintenance work performed on shops.

Field Name	        Data Type	        Description	                                    Constraints
main_id	            String (PK)	        Unique identifier for the maintenance record	Unique, Not Null
shop_id	            String (FK)	        Reference to the shops collection	            Must exist in shops
description	        String	            Details of the work done	                    Not Null
date	            String	            Date of the maintenance work	                Format: YYYY-MM-DD
cost	            Float	            Cost of the service	                            Must be >= 0

4. Entity Relationships (ER)

Although this is a NoSQL (JSON) structure, relational concepts are applied logically:

Shop ↔ Rental (One-to-One / One-to-None):
A Shop can have only one active Rental at a time.
This is enforced by the is_rented flag in the Shop model and business logic in RentalService.
Relationship: rentals.shop_id references shops.shop_id.

Shop ↔ Maintenance (One-to-Many):
A Shop can have multiple Maintenance records over time.
Relationship: maintenance.shop_id references shops.shop_id.