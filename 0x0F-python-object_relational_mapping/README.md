Creating a README file for your repository is essential to provide clear instructions and context for users and collaborators. Below is a template for your README file based on the tasks you've shared:

---

# Python - Object Relational Mapping (ORM)

This repository contains Python scripts that demonstrate the use of Object Relational Mapping (ORM) techniques with MySQL databases using SQLAlchemy and MySQLdb modules.

## Description

The repository includes scripts that perform various tasks such as querying databases, filtering data, and interacting with tables using SQLAlchemy, a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/alx-higher_level_programming.git
   ```

2. **Navigate to the directory:**
   ```bash
   cd 0x0F-python-object_relational_mapping
   ```

3. **Install dependencies:**
   - Ensure you have Python 3.x installed.
   - Install MySQLdb using pip:
     ```bash
     pip install mysqlclient
     ```
   - Install SQLAlchemy:
     ```bash
     pip install SQLAlchemy
     ```

## Scripts and Usage

### 0. Select States
- **Description:** Lists all states from the database `hbtn_0e_0_usa`.
- **Script:** `0-select_states.py`
- **Usage:**
  ```bash
  ./0-select_states.py <mysql_username> <mysql_password> <database_name>
  ```
  
### 1. Filter States
- **Description:** Lists states with names starting with 'N' from the database `hbtn_0e_0_usa`.
- **Script:** `1-filter_states.py`
- **Usage:**
  ```bash
  ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
  ```

### 2. Filter States by User Input
- **Description:** Displays states from `hbtn_0e_0_usa` based on user input.
- **Script:** `2-my_filter_states.py`
- **Usage:**
  ```bash
  ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> '<state_name>'
  ```

### 3. Safe Filter States
- **Description:** Securely filters states by name to prevent SQL injection attacks.
- **Script:** `3-my_safe_filter_states.py`
- **Usage:**
  ```bash
  ./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> '<state_name>'
  ```

### 4. Cities by State
- **Description:** Lists all cities associated with their respective states.
- **Script:** `4-cities_by_state.py`
- **Usage:**
  ```bash
  ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
  ```

### 5. Filter Cities by State
- **Description:** Lists cities of a specific state based on user input.
- **Script:** `5-filter_cities.py`
- **Usage:**
  ```bash
  ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> '<state_name>'
  ```

### 6. First State Model
- **Description:** Defines a State class using SQLAlchemy and creates the `states` table in the database `hbtn_0e_6_usa`.
- **Script:** `model_state.py`
- **Usage:** Automatically executed when running scripts dependent on the State model.

### 7. All States via SQLAlchemy
- **Description:** Fetches and lists all State objects from `hbtn_0e_6_usa` using SQLAlchemy.
- **Script:** `7-model_state_fetch_all.py`
- **Usage:**
  ```bash
  ./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
  ```

### 8. First State via SQLAlchemy
- **Description:** Fetches and prints the first State object from `hbtn_0e_6_usa` using SQLAlchemy.
- **Script:** `8-model_state_fetch_first.py`
- **Usage:**
  ```bash
  ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
  ```

### 9. States Containing 'a' via SQLAlchemy
- **Description:** Lists State objects from `hbtn_0e_6_usa` containing the letter 'a' using SQLAlchemy.
- **Script:** `9-model_state_filter_a.py`
- **Usage:**
  ```bash
  ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>
  ```

### 10. Get a State via SQLAlchemy
- **Description:** Retrieves and prints the ID of a State object by its name from `hbtn_0e_6_usa` using SQLAlchemy.
- **Script:** `10-model_state_my_get.py`
- **Usage:**
  ```bash
  ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> '<state_name>'
  ```

### 11. Add a New State via SQLAlchemy
- **Description:** Adds a new State object "Louisiana" to `hbtn_0e_6_usa` using SQLAlchemy.
- **Script:** `11-model_state_insert.py`
- **Usage:**
  ```bash
  ./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>
  ```

### 12. Update a State via SQLAlchemy
- **Description:** Changes the name of a State object with ID 2 to "New Mexico" in `hbtn_0e_6_usa` using SQLAlchemy.
- **Script:** `12-model_state_update_id_2.py`
- **Usage:**
  ```bash
  ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>
  ```

### 13. Delete States via SQLAlchemy
- **Description:** Deletes State objects from `hbtn_0e_6_usa` containing the letter 'a' using SQLAlchemy.
- **Script:** `13-model_state_delete_a.py`
- **Usage:**
  ```bash
  ./13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>
  ```

### 14. Cities in State via SQLAlchemy
- **Description:** Lists all City objects from `hbtn_0e_14_usa` associated with their respective states using SQLAlchemy.
- **Script:** `14-model_city_fetch_by_state.py`
- **Usage:**
  ```bash
  ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>
  ```

