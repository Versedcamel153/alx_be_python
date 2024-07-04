from datetime import datetime, timedelta

def display_current_datetime():
    global current_date
    current_date = datetime.now()

    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")



def calculate_future_date():
    days = input("Enter number of days to add to current date: ")

    future_date = current_date + timedelta(days=int(days))
    format_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {format_date}")

display_current_datetime()
calculate_future_date()