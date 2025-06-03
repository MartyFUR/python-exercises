import matplotlib.pyplot as plt

expenses = {
    'Rent': 800,
    'Groceries': 300,
    'Utilities': 100,
    'Transport': 150,
    'Entertainment': 120,
    'Savings': 200
}


labels = list(expenses.keys())
values = list(expenses.values())

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Monthly Expense Breakdown")
plt.axis('equal')  # Make it a perfect circle
plt.show()