# 🚀 Selenium Automation Testing Framework

## 📌 Project Overview

This project is an **end-to-end automation testing framework** built using Python and Selenium to validate user workflows on a web application.

The application is deployed as a live website using GitHub Pages, and automated tests simulate real user interactions such as login and logout.

---

## 🌐 Live Application

🔗 https://balashanmugam-rathinam.github.io/selenium-project/

---

## 🎯 Features

* ✅ Automated login functionality testing
* ✅ Logout flow validation
* ✅ Data-driven testing using multiple user inputs
* ✅ Page Object Model (POM) architecture
* ✅ Explicit waits for stable test execution
* ✅ Headless execution support for CI/CD
* ✅ Automated test execution using GitHub Actions

---

## 🧱 Tech Stack

* Python
* Selenium
* Pytest
* HTML, CSS, JavaScript
* GitHub Pages (Deployment)

---

## 📁 Project Structure

```id="f2qz1s"
selenium_project/
│
├── index.html
├── dashboard.html
├── style.css
├── script.js
│
├── automation/
│   ├── tests/
│   │   └── test_login.py
│   │
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   └── dashboard_page.py
│   │
│   ├── utils/
│   │   └── driver_setup.py
│   │
│   ├── conftest.py
│   ├── screenshots/
│   └── reports/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🧪 Test Scenarios

### 🔹 Valid Login

* Enter correct credentials
* Verify redirection to dashboard

### 🔹 Invalid Login

* Enter incorrect credentials
* Verify error message

### 🔹 Logout

* Login successfully
* Click logout
* Verify return to login page

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash id="c8t0x3"
git clone https://github.com/balashanmugam-rathinam/selenium-project.git
cd selenium-project
```

---

### 2️⃣ Create virtual environment

```bash id="y7i6rj"
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash id="m3c9yz"
pip install -r requirements.txt
```

---

### 4️⃣ Run tests

```bash id="y6e0cd"
pytest -v
```

---

## ⚙️ CI/CD Pipeline

This project uses GitHub Actions to:

* Automatically run tests on every push
* Execute tests in headless browser mode
* Ensure code quality and reliability

---

## 📊 Test Reports

* HTML reports generated using Pytest
* Screenshots captured on test failure

---

## 🧠 Key Concepts Used

* Selenium WebDriver automation
* Page Object Model (POM)
* Explicit waits (synchronization)
* Data-driven testing
* Continuous Integration (CI/CD)

---

## 🚀 Future Improvements

* Add API testing integration
* Parallel test execution
* Docker-based test environment
* Backend integration using Django

---

## 👨‍💻 Author

Balashanmugam R

---

## 📜 License

This project is for educational and portfolio purposes.
