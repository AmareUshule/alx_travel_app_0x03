# ALX Travel App - Phase 0x00

## Project Overview
This project demonstrates **Database Modeling and Data Seeding in Django**. It includes defining models, creating serializers for API representation, and implementing a management command to seed the database with sample data.

---

## Tasks

### 0. Database Modeling and Data Seeding in Django
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

#### Objective
- Define database models.
- Create serializers for API data representation.
- Implement a management command to seed the database with sample data.

#### Instructions

1. **Duplicate Project**
   - Duplicate the original project `alx_travel_app` to `alx_travel_app_0x00`.

2. **Create Models**
   - File: `listings/models.py`
   - Define the following models:
     - `Listing`
     - `Booking`
     - `Review`
   - Each model should include:
     - Appropriate fields
     - Relationships (e.g., `ForeignKey`)
     - Constraints

3. **Set Up Serializers**
   - File: `listings/serializers.py`
   - Create serializers for `Listing` and `Booking` models to represent data in JSON format for API responses.

4. **Implement Seeders**
   - File: `listings/management/commands/seed.py`
   - Implement a management command to populate the database with sample listings data.

5. **Run Seed Command**
   - Test the seeder by running the command to populate the database with sample data.

---

## File Structure


