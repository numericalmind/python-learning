import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("expenses.csv")
print(df.head())
df["Amount"].sum()
print("Total_Expense:" ,df["Amount"].sum())
df["Amount"].mean()
print("Average_Expense:", df["Amount"].mean())
df.groupby("Category")["Amount"].sum
category_expenses = df.groupby("Category")["Amount"].sum()
print("Category_Expenses:", category_expenses)
highest_category = category_expenses.idxmax()
print("Highest Spending Category:" , highest_category)
highest_amount = category_expenses.max()
print("Highest Spending Amount: " , highest_amount)
category_expenses.plot(kind="bar")
plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()

plt.savefig("expense_chart.png")
