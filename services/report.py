from .filter import filtered_item
from matplotlib import pyplot as plt # type: ignore
import numpy as np # type: ignore


def get_report(self, time_frame, category_selected):
    total_income = 0
    income_count = 0
    total_expenses = 0
    expenses_count = 0
    average_daily_spending = 0
    savings_percentage = 0
    total_expenses_for_category = 0

    result = filtered_item(self, time_frame)

    if len(result) == 0:
        print("📭 No transactions found for the selected period.")
        return False

    print("\n" + "🔍 Transactions Found")
    print("—" * 50)
    for i, item in enumerate(result, 1):
        emoji = "🟢" if item.type == 'income' else "🔴"
        print(f"{emoji} {i}. {item}")
        if item.type == 'income':
            income_count += 1
            total_income += int(item.amount)
        else:
            expenses_count += 1
            total_expenses += int(item.amount)
            if category_selected != 'all' and item.category == category_selected:
                total_expenses_for_category += int(item.amount)  

    if len(result) > 0:
        average_daily_spending = total_expenses / len(result)
    if total_income > 0:
        savings_percentage = (total_income - total_expenses) / total_income * 100 
    else:
        savings_percentage = 0

    print("\n" + "📊 Financial Summary")
    print("—" * 50)
    print(f"💼 Total Income:      {total_income:,} Toman")
    print(f"💸 Total Expenses:    {total_expenses:,} Toman")
    print(f"✅ Net Savings:       {total_income - total_expenses:+,} Toman")
    print(f"📅 Avg Daily Spending: {average_daily_spending:,.0f} Toman")
    print(f"📈 Savings Rate:      {savings_percentage:.1f}%")

    if category_selected != 'all':
        print(f"🏷️  Total in '{category_selected}': {total_expenses_for_category:,} Toman")

    if income_count > 0 or expenses_count > 0:
        print("\n" + "🎨 Pie Chart: Income vs Expenses")
        plt.figure(figsize=(6, 6))
        sizes = [income_count, expenses_count]
        labels = [f"Income ({income_count})", f"Expenses ({expenses_count})"]
        colors = ['#4CAF50', '#F44336']
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        plt.title(f"Transaction Count: {time_frame.replace('_', ' ').title()}")
        plt.axis('equal')
        plt.show()

    return total_income, total_expenses, average_daily_spending, savings_percentage, total_expenses_for_category