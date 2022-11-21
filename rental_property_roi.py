class Calculator():
    def __init__(self):
        
        self.income_input()
        self.expenses_input()
        self.cash_flow()
        self.cash_on_cash_Roi()



    def income_input(self):
       self.total_monthly_income = float(input('What is your rental property total monthly income?'))
       print(self.total_monthly_income)


    def expenses_input(self):
        self.monthly_tax_expense = float(input('What is your rental property total monthly tax expense?'))
        self.monthly_insurance_expense = float(input('What is your renal property total monthly insurance expense?'))
        self.monthly_vacancy_expense = float(input('What is your renal property total monthly vacany expense?'))
        self.monthly_repairs_expense = float(input('What is your renal property total monthly repairs expense?'))
        self.monthly_capEx_expense = float(input('What is your renal property total monthly capEx expense?'))
        self.monthly_mortgage_expense = float(input('What is your renal property total monthly mortgage expense?'))
        self.monthly_property_manager_expense = float(input('What is your renal property total monthly property manager expense?'))


        self.total_monthly_expenses = (self.monthly_tax_expense + self.monthly_insurance_expense + self.monthly_vacancy_expense + self.monthly_repairs_expense + self.monthly_capEx_expense + self.monthly_mortgage_expense + self.monthly_property_manager_expense)
        print(self.total_monthly_expenses)


    def cash_flow(self):
        self.total_monthly_cash_flow = (self.total_monthly_income - self.total_monthly_expenses)
        print(self.total_monthly_cash_flow)


    def cash_on_cash_Roi(self):
        self.down_payment = float(input('How much is your down payment for this property?'))
        self.closing_cost = float(input('How much are your closing cost?'))
        self.property_rehab = float(input('How much did the rehab of the property cost?'))

        self.total_investment = (self.down_payment + self.closing_cost + self.property_rehab)

        self.annual_cashflow = (self.total_monthly_cash_flow * 12)

        self.c_on_c_roi = ((self.annual_cashflow/self.total_investment)*100)

        print(self.c_on_c_roi)



my_calculator = Calculator()