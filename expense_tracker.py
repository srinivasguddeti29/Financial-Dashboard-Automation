# Financial Dashboard Automation
# Company Expense Tracker

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('expenses.csv')

# Show basic information
print("Company Expense Data:")
print(data)

# Total expenses
total_expense = data['Amount'].sum()
print(f"\nTotal Company Expenses: {total_expense}")

# Expenses by department
department_expense = data.groupby('Department')['Amount'].sum()
print("\nExpenses by Department:")
print(department_expense)

# Plot expenses by department
department_expense.plot(kind='bar', title='Company Expenses by Department')
plt.ylabel('Amount')
plt.show()
