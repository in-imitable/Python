import os
import sys

class Application():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.expense_list = []
        self.expense_name = []
        self.income_name = []
        self.income_list = []
        self.prompt_income()

    def income_ask(self):
        add_income = input('Add income? [y/n]: ')
        return add_income

    def income_sum(self):
        self.income = sum(self.income_list)

    def expense_ask(self):
        add_expense = input('Add expense? [y/n]: ')
        return add_expense

    def expense_sum(self):
        self.expenses = sum(self.expense_list)

    def income_check(self):
        if not self.income_list:
            print('Please enter atleast one source of income. ')
            self.prompt_income()
        else:
            return

    def expense_check(self):
        if not self.expense_list:
            print('Please enter atleast one expense. ')
            self.prompt_expense()
        else:
            return

    def prompt_income(self):
        x = False
        while not x:
            result = self.income_ask()
            if result == 'y':
                income_input = int(input('Enter source of income. [Numbers Only]: '))
                self.income_list.append(income_input)
                income_name = input('Enter income name. [Name Only]: ')
                self.income_name.append(income_name)
            else:
                self.income_check()
                x = True
        self.income_sum()
        name = [name for name in self.income_name]
        income = [income for income in self.income_list]
        incomedict = dict(zip(name, income))
        for k in incomedict:
            print(k + ': ', '$' + str(incomedict[k]))
        print('Total user income: ', '$' + str(self.income))
        self.prompt_expense()

    def prompt_expense(self):
        x = False
        while not x:
            result = self.expense_ask()
            if result == 'y':
                expense_input = int(input('Enter expense amount. [Numbers Only]: '))
                self.expense_list.append(expense_input)
                expense_name = input('Enter expense name. [Name Only]: ')
                self.expense_name.append(expense_name)
            else:
                self.expense_check()
                x = True
        self.expense_sum()
        name = [name for name in self.expense_name]
        expense = [income for income in self.expense_list]
        expensedict = dict(zip(name, expense))
        for k in expensedict:
            print(k + ': ', '$' + str(expensedict[k]))
        print('Total user expenses: ', '$' + str(self.expenses))
        self.uservalue()

    def uservalue(self):
        valoutput = self.income - self.expenses
        if valoutput < 0:
            print('You are in the negative, you have a deficit of ' + '$' + str(valoutput))
        if valoutput == 0:
            print('You have broken even, you are spending exactly as much as you make.')
        if valoutput > 0:
            print('You are in the positive, you have a surplus of ' + '$' + str(valoutput))
        another = input('Would you like to run another analysis? [y/n]: ')
        if another == 'y':
            self.reset_program()
        else:
            self.close_program()

    def reset_program(self):
        self.income = 0
        self.expenses = 0
        del self.expense_list[0:]
        del self.expense_name[0:]
        del self.income_name[0:]
        del self.income_list[0:]
        self.prompt_income()

    def close_program(self):
        print('Exiting Program.')
        sys.exit(0)

if __name__ == '__main__':
    Application()