from . import filter
from matplotlib import pyplot as plt
import numpy as np


def get_report(self, time_frame, category_selected):
    total_income = 0
    income_count = 0
    total_expenses = 0
    expenses_count = 0
    average_daily_spending = 0
    savings_percentage = 0
    total_expenses_for_category = 0
    result = filter.filtered_item(self, time_frame)
    if len(result) == 0:
        print('\nNot Found !!!')
        return False
    print('\nItems found :\n')
    for i, item in enumerate(result):
        print(f"{i}. {item}")
        if item.type == 'income':
            income_count += 1
            total_income += int(item.amount)
        else:
            expenses_count += 1
            total_expenses += int(item.amount)
            if category_selected != 'all' and item.category == category_selected:
                total_expenses_for_category = int(item.amount)
    average_daily_spending = total_expenses / len(result)
    if total_income > 0:
        savings_percentage = (total_income - total_expenses) / total_income
    else:
        savings_percentage = 0
    print(f"\nTotal Income: {total_income}")
    print(f"\nTotal Expenses: {total_expenses}")
    print(f"\nAverage Daily Spending: {average_daily_spending}")
    print(f"\nSavings Percentage: {savings_percentage:.2f}%")
    if category_selected != 'all':
        print(f"\nTotal Expenses for Category {category_selected} is : {total_expenses_for_category}")
    if income_count != 0 or expenses_count != 0:
        print("\nPie Chart :\n")
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.axis('equal')
        langs = ['income', 'expenses']
        count = [income_count, expenses_count]
        ax.pie(count, labels = langs,autopct='%1.2f%%')
        plt.show()
    return total_income, total_expenses, average_daily_spending, savings_percentage, total_expenses_for_category
        
        