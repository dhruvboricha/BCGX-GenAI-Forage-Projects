import pandas as pd

# Load data
try:
    final_report = pd.read_csv(r'C:\Users\Dhruv Boricha\Downloads\final_financial_data_report.csv')
    summary_report = pd.read_csv(r'c:\Users\Dhruv Boricha\Downloads\Summary_financial_report.csv')
except FileNotFoundError:
    print("Error: Data files not found. Please ensure 'final_data_report.csv' and 'Summary_final_report.csv' exist.")

# Predefined list of questions
questions = [
    "What is the total revenue?",
    "What is the Net Income?",
    "What is the sum of total assets?",
    "What is the sum of total liabilities?",
    "What is cash flow from operating activities?",
    "What is the revenue growth (%)?",
    "What is the net income growth (%)?",
    "What is the assets growth (%)?",
    "What is the liabilities growth (%)?",
    "What is the cash flow from operations growth (%)?",
    "What is the year-by-year average revenue growth rate (%)?",
    "What is the year-by-year average net income growth rate (%)?",
    "What is the year-by-year average assets growth rate (%)?",
    "What is the year-by-year average liabilities growth rate (%)?",
    "What is the year-by-year average cash flow from operations growth rate (%)?"
]

# Define the chatbot logic
def financial_chatbot(company_input, fiscal_year, user_query):
    try:
        company_input = company_input.capitalize()
        if user_query == "What is the total revenue?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Total Revenue'].values[0]
            return f"The Total Revenue for {company_input} in {fiscal_year} is ${value:,}."

        elif user_query == "What is the Net Income?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Net Income'].values[0]
            return f"The Net Income for {company_input} in {fiscal_year} is ${value:,}."

        elif user_query == "What is the sum of total assets?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Total Assets'].values[0]
            return f"The Total Assets for {company_input} in {fiscal_year} are ${value:,}."

        elif user_query == "What is the sum of total liabilities?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Total Liabilities'].values[0]
            return f"The Total Liabilities for {company_input} in {fiscal_year} are ${value:,}."

        elif user_query == "What is cash flow from operating activities?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Cash Flow from Operating Activities'].values[0]
            return f"The Cash Flow from Operating Activities for {company_input} in {fiscal_year} is ${value:,}."

        elif user_query == "What is the revenue growth (%)?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Revenue Growth (%)'].values[0]
            return f"The Revenue Growth for {company_input} in {fiscal_year} is {value:.2f}%."

        elif user_query == "What is the net income growth (%)?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Net Income Growth (%)'].values[0]
            return f"The Net Income Growth for {company_input} in {fiscal_year} is {value:.2f}%."

        elif user_query == "What is the assets growth (%)?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Assets Growth (%)'].values[0]
            return f"The Assets Growth for {company_input} in {fiscal_year} is {value:.2f}%."

        elif user_query == "What is the liabilities growth (%)?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Liabilities Growth (%)'].values[0]
            return f"The Liabilities Growth for {company_input} in {fiscal_year} is {value:.2f}%."

        elif user_query == "What is the cash flow from operations growth (%)?":
            value = final_report[(final_report['Company'] == company_input) & (final_report['Year'] == fiscal_year)]['Cash Flow from Operations Growth(%)'].values[0]
            return f"The Cash Flow from Operations Growth for {company_input} in {fiscal_year} is {value:.2f}%."

        elif user_query == "What is the year-by-year average revenue growth rate (%)?":
            value = summary_report[summary_report['Company'] == company_input]['Revenue Growth (%)'].values[0]
            return f"The Year-by-Year Average Revenue Growth for {company_input} is {value:.2f}%."

        elif user_query == "What is the year-by-year average net income growth rate (%)?":
            value = summary_report[summary_report['Company'] == company_input]['Net Income Growth (%)'].values[0]
            return f"The Year-by-Year Average Net Income Growth for {company_input} is {value:.2f}%."

        elif user_query == "What is the year-by-year average assets growth rate (%)?":
            value = summary_report[summary_report['Company'] == company_input]['Assets Growth (%)'].values[0]
            return f"The Year-by-Year Average Assets Growth for {company_input} is {value:.2f}%."

        elif user_query == "What is the year-by-year average liabilities growth rate (%)?":
            value = summary_report[summary_report['Company'] == company_input]['Liabilities Growth (%)'].values[0]
            return f"The Year-by-Year Average Liabilities Growth for {company_input} is {value:.2f}%."

        elif user_query == "What is the year-by-year average cash flow from operations growth rate (%)?":
            value = summary_report[summary_report['Company'] == company_input]['Cash Flow from Operations Growth(%)'].values[0]
            return f"The Year-by-Year Average Cash Flow from Operations Growth for {company_input} is {value:.2f}%."

        else:
            return "Sorry, I can only answer predefined financial questions."
    except:
        return "Error retrieving data. Please check your input or try again."

# Chatbot Conversation
print("💬 Welcome to the AI-Driven Financial Chatbot Prototype!")
while True:
    start = input("\nType 'hi' to start or 'exit' to quit: ").lower()
    if start == 'exit':
        print("👋 Goodbye!")
        break
    elif start == 'hi':
        print("\nAvailable Companies: Microsoft, Tesla, Apple")
        company_input = input("Enter the company name: ").capitalize()

        if company_input not in ['Microsoft', 'Tesla', 'Apple']:
            print("Invalid company name. Please try again.")
            continue

        try:
            fiscal_year = int(input("Enter the fiscal year (2021, 2022, 2023): "))
            if fiscal_year not in [2021, 2022, 2023]:
                print("Invalid year. Please enter 2021, 2022, or 2023.")
                continue
        except ValueError:
            print("Invalid input for year.")
            continue

        print("\nAvailable Questions:")
        for q in questions:
            print(f"- {q}")

        while True:
            user_query = input("\nEnter your question (or type 'back' to choose another company): ")
            if user_query.lower() == 'back':
                break
            response = financial_chatbot(company_input, fiscal_year, user_query)
            print(f"\n{response}")
    else:
        print("Please type 'hi' correctly to start.")

