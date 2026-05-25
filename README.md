**Ecommerce QA Automation Project
Overview**

**This project is a complete QA Automation framework for testing an e-commerce web application using:**

UI Automation with Selenium
API Testing with Requests
Database Testing with SQLite
Test Execution with Pytest
Continuous Integration with GitHub Actions

**The framework demonstrates real-world automation testing practices including:**

Login validation
Form validation
Product search testing
Cart functionality testing
Logout testing
API response validation
Database query validation

**Technologies Used:**
Python
Selenium WebDriver
Pytest
Requests
SQLite3
GitHub Actions
ChromeDriver
WebDriver Manager

**Project Structure**
Ecommerce-QA-Project/
│
├── Automation/
│   ├── Tests/
│   │   ├── test_login.py
│   │   ├── test_logout.py
│   │   ├── test_search.py
│   │   ├── test_cart.py
│   │   └── test_form_validation.py
│   │
│   ├── api_tests/
│   │   └── test_users_api.py
│   │
│   ├── database/
│   │   ├── ecommerce.db
│   │   └── test_database.py
│   │
│   ├── Pages/
│   └── Utilities/
│
├── conftest.py
├── requirements.txt
├── pytest.ini
└── .github/
    └── workflows/
        └── tests.yml

Features:
**UI Automation Tests**
Invalid login testing
Form validation testing
Product search testing
Add to cart testing
Logout functionality testing
**API Testing**
Validate API status codes
Validate JSON response data
Validate API user data
**Database Testing**
Database connection validation
Product data validation
SQL query testing
**CI/CD Integration**
Automated GitHub Actions workflow
Runs tests automatically on push
Displays pass/fail results

**Installation**
**Clone the repository:**
git clone https://github.com/your-username/Ecommerce-QA-Project.git

**Navigate into the project:**
cd Ecommerce-QA-Project

**Install dependencies:**
pip install -r requirements.txt

**Running Tests:**
**Run all tests:**
pytest

**Run UI tests only:**
pytest Automation/Tests

**Run API tests only:**
pytest Automation/api_tests

**Run Database tests only:**
pytest Automation/database

**GitHub Actions:**
This project includes a GitHub Actions workflow that automatically runs tests whenever code is pushed to the repository.

**Workflow file location:** .github/workflows/tests.yml

**Sample Test Coverage:**
Test Type	Description
Login Tests	Validate invalid login scenarios
Form Validation	Required email/password fields
Search Tests	Product search functionality
Cart Tests	Add product to cart
Logout Tests	User logout functionality
API Tests	API response validation
Database Tests	SQLite query validation

**Future Improvements:**
Add Page Object Model enhancements
Add test reporting with Allure
Add Jenkins pipeline integration
Add Docker support
Add cross-browser testing
Add performance testing

**Author:**
Francisco Morales Jr

**License:**
This project is for educational and portfolio purposes.