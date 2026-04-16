# Personal Finance Tracker

**Course Project - Task 1 (OOP-based Application Development)**  
**COMP2090SEF / COMP8090SEF**  
**Hong Kong Metropolitan University (HKMU)**  
**2026 Spring Semester**  

---

## Project Description

This is a **simple console-based Personal Finance Tracker**.  

It helps users manage daily income, expenses, and budgets.  
It solves a real-life problem: people often lose track of their spending and do not know how much money they have left in each category.

The program is built using **basic Object-Oriented Programming (OOP)** concepts taught in Lecture Note 2.

---

## Key Features

- Add Income and Expense transactions  
- Set monthly budget for each category  
- View financial report (total income, total expenses, net balance)  
- List all transactions  
- Check budget status with overspending alerts  
- Save and load data automatically (using JSON file)

---

## OOP Concepts Used (Following Lecture Note 2)

This project demonstrates **all the core OOP concepts** taught in the course:

| OOP Concept              | How It Is Used                                      | File         |
|--------------------------|-----------------------------------------------------|--------------|
| Class & Object           | `Transaction`, `Income`, `Expense`, `Budget`, `FinanceManager` | models.py, manager.py |
| `__init__` and `self`    | Used in every class to set attributes               | models.py    |
| Attributes               | `amount`, `category`, `limit`, `spent`, etc.       | models.py    |
| Methods                  | `get_description()`, `add_transaction()`, `generate_report()`, etc. | All files |
| Inheritance              | `Income` and `Expense` inherit from `Transaction`  | models.py    |
| Multiple Classes         | 5 classes across different files                    | All files    |
| Modular Programming      | 4 separate Python files                             | Whole project|

---
# How to Run (User Guide)

### Step-by-step Instructions

1. Download the `task1` folder.
2. Open a terminal / command prompt and go into the `task1` folder
