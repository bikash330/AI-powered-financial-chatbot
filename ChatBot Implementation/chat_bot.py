import pandas as pd

# Read the CSV files
final = pd.read_csv("Final_Data_Report.csv")

# Function to handle user queries
def chatbot():
    print('Enter your query')
    user_input = input().lower()  # Convert input to lowercase for easier comparison
    
    if "total revenue" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Total Revenue'].values
        if len(answer) > 0:  # Check if the query resulted in any data
            return f"Total Revenue for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    elif "net income" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Net Income'].values
        if len(answer) > 0:
            return f"Net Income for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    elif "total assets" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Total Assets'].values
        if len(answer) > 0:
            return f"Total Assets for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    elif "total liabilities" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Total Liabilities'].values
        if len(answer) > 0:
            return f"Total Liabilities for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    elif "cash flow" and "operating activities" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Cash Flow from Operating Activities'].values
        if len(answer) > 0:
            return f"Cash Flow from Operating Activities for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    elif "revenue growth" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Revenue Growth (%)'].values
        if len(answer) > 0:
            return f"Revenue Growth (%) for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    elif "net income growth" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Net Income Growth (%)'].values
        if len(answer) > 0:
            return f"Net Income Growth (%) for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    elif "assets growth" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Assets Growth (%)'].values
        if len(answer) > 0:
            return f"Assets Growth (%) for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    elif "liabilities growth" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Liabilities Growth (%)'].values
        if len(answer) > 0:
            return f"Liabilities Growth (%) for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    elif "cash flow" and "operations growth" in user_input:
        answer = final.loc[(final['Year'] == year) & (final['Company'] == company), 'Cash Flow from Operations Growth(%)'].values
        if len(answer) > 0:
            return f"Cash Flow from Operations Growth(%) for {company} in {year}: {answer[0]}"
        else:
            return "No data found for the specified year and company."
    else:
        return "Invalid query."

print("-------------------------------------------------------------------")
print("-----------------Welcome to financial chatbot----------------------")
print("-------------------------------------------------------------------")

while True:
    first_input = input("\nEnter 'go' to start the chatbot or type 'exit' to end: ").lower()
    if first_input == 'exit':
        print('\n\nThank you for using our Financial ChatBot! Have a great day!\n')
        break
    elif first_input == 'go':
        # Prompt user to input company name
        company = input("\nEnter Company Name: ").capitalize()
        if company not in final["Company"].unique():
            print("\nInvalid Entry, Please enter valid company name.")
            continue  # Restart the loop
        else:
            # Prompt user to input year
            print("\nWe have data of fiscal year 2023, 2022, and 2021")
            year = int(input(f"\nEnter a year you want to know the data of {company}: "))
            if year not in final["Year"].unique():
                print("\nInvalid Year Entered, Please try again with a valid year.")
                continue  # Restart the loop

        result = chatbot()  # Call the chatbot function to get the result
        print(result)  # Print the result
    else:
        print("You entered an invalid command, please try again.")