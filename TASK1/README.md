Personal Finance Tracker

**Course Project - Task 1 (OOP-based Application Development)**  
**COMP2090SEF / COMP8090SEF / COMP S209W**  
**Hong Kong Metropolitan University (HKMU)**  
**2026 Spring Semester**  


Project Description

This is a **console-based Personal Finance Tracker** that helps users manage their daily income, expenses, and budgets.  

It solves a common real-life problem: **difficulty in tracking spending, overspending on certain categories, and lacking clear financial summaries**. Users can easily log transactions, set monthly budgets per category, view reports, and receive budget alerts — all in one simple Python application.

The application is built entirely with **Object-Oriented Programming (OOP)** concepts taught in the course and uses **modular programming** with 4 separate Python files.


Key Features

- Add Income and Expense transactions
- Set monthly budgets for different categories
- Automatic budget tracking and overspending alerts
- Generate financial reports (total income, expenses, net balance)
- View complete transaction history
- Data persistence (saved to `finance_data.json`)
- Clean, user-friendly console menu


OOP Concepts Demonstrated

This project uses **ALL** OOP concepts introduced in the course:

| OOP Concept       | How It Is Used in This Project                          | File          |
|-------------------|---------------------------------------------------------|---------------|
| **Abstraction**   | `Transaction` is an Abstract Base Class (ABC) with an abstract method | `models.py`   |
| **Encapsulation** | Private attribute `__amount` with `@property` getter   | `models.py`   |
| **Inheritance**   | `Income` and `Expense` inherit from `Transaction`      | `models.py`   |
| **Polymorphism**  | `get_description()` behaves differently in subclasses  | `models.py`   |
| **Composition**   | `FinanceManager` contains `Budget` objects             | `manager.py`  |
| **Modular Design**| 4 separate modules for better organization             | All files     |



 
---
🚀 How to Run (User Guide)

Prerequisites
- Python 3.8 or higher

 Step-by-step Instructions

1. **Download** the entire `task1` folder (or clone the repository).
2. Open a terminal/command prompt and navigate to the `task1` folder:
