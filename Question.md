### **02 OOP Bank Account System + pandas Dataset Analysis** 
Stack: Python OOP, pandas, numpy (Week 2 skills) 

**Overview** 
Two-part project:

    - Part A: Object-oriented banking system using classes, inheritance, and encapsulation. 
    - Part B: Analyse a CSV dataset using pandas and numpy. Both parts in a single project folder. 

**Learning Objectives:**

    - Apply OOP: classes with __init__, methods, properties, and inheritance 
    - Use polymorphism across subclasses 
    - Read, clean, and analyse a CSV dataset with pandas groupby and merge 
    - Use numpy for descriptive statistics 
    - Demonstrate clean code: type hints, docstrings, separation of concerns 

**What to Build:** 

    8. Part A: Define BankAccount with: account_number, holder_name, _balance (private), deposit(amount), withdraw(amount), get_balance(). Raise ValueError for invalid operations. 
    9. Create SavingsAccount subclass adding interest_rate and apply_interest(). 
    10. Create CurrentAccount subclass adding overdraft_limit. 
    11. Add transaction_history storing all events as dicts. 
    12. Demonstrate: 2 savings + 1 current account, deposits, withdrawals, interest, print histories. 
    13. Part B: Download a public CSV (Titanic, Iris, etc.). Clean it: handle missing values, drop irrelevant columns. 
    14. pandas: groupby summary, top-10 ranking, filtered subset with 2+ conditions. 
    15. numpy: mean, std deviation, 25th/75th percentile, correlation between two columns. 
**Deliverables** 

    • bank_account.py with all 3 account classes 
    • main_bank.py demonstrating the banking system 
    • dataset_analysis.py with full pandas/numpy analysis 
    • The CSV file used (or a link in a README comment) Evaluation Criteria 
    • Inheritance used correctly 
    • Polymorphism demonstrated 
    • ValueError raised for invalid transactions 
    • pandas groupby and merge produce correct results 
    • numpy statistics match expected values