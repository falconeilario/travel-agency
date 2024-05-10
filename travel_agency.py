# Import libraries
import pandas as pd
from datetime import datetime

# Load csv files containing data about flights and create a corresponding Pandas DataFrame
df_flights = pd.read_csv("./Flights_info.csv")

# Variable needed from functions
user_selection = 999999
service_extra_baggage = 47
service_car_rental_per_day = 51
service_travel_insurance_per_day = 6
boolean_selection_list = ["Yes", "No"]
# Reusable function to show available unique values in a specific column of a file
def show_available_options(unique_values):
    for count, available_option in enumerate(unique_values):
        print(count, "-", available_option)
    print()

# Reusable function to let the user select one of the available options from a list
def selection_process(user_input, selection_list):
    while user_input >= len(selection_list):
        user_input = input(f"Enter the number corresponding to your selection\n(e.g. Enter 0 for {selection_list[0]}, etc.): ")
        if user_input.isdigit() and int(user_input) < len(selection_list):
            print("")
            print(f"You have selected {selection_list[int(user_input)]}.")
            print("")
            return(selection_list[int(user_input)])
        else:
            user_input = 999999
            print("")
            print("Unrecognized option.")
            print("")
            print("Choose one of the available options:")
            show_available_options(selection_list)

# Reusable function to show available flights corresponding to the selection
def show_available_flights(filtered_dataframe):
    for count, (index, available_flight) in enumerate(filtered_dataframe.iterrows()):
        print(f"""{count} - Flight number: {available_flight['flight_number']}
    Air company: {available_flight['flight_company']}
    Departing at: {available_flight['flight_time']}
    Duration: {available_flight['duration_minutes']} minutes
    Price: £ {available_flight['ticket_price']}
    """)

# Reusable function to retrieve single value from a column of the file corresponding to the selected flight
def retrieve_flight_info(searched_value, output_column):
    value = df_flights.loc[df_flights["flight_number"] == searched_value, output_column].values[0]
    return value

# Reusable function to transform boolean in integer
def transform_bool_to_int(input_value):
    return 1 if input_value == "Yes" else 0

# LAUNCH PROGRAM
print("Welcome to our Travel agency!\nWe will help you find a flight for your holiday by choosing from a series of available locations and services.\nLet's begin!")
print("")

# Ask the user from where they prefer to leave
print("Where do you want to start your trip from?")
# Look for available departure city in Flights file
unique_departure_cities = df_flights["departure_city"].unique()

# Call function to show available departure city for the selection
show_available_options(unique_departure_cities)

# Call function to let the user select one of the available departure city
selected_departure_city = selection_process(user_selection, unique_departure_cities)

# Ask the user where they want to go
print("Where do you want to go?")

# Filter dataframe to obtain only observations with the arrival cities for the selected departure city
df_arrival_cities = df_flights[df_flights["departure_city"] == selected_departure_city]
unique_arrival_cities = df_arrival_cities["arrival_city"].unique()

# Call function to show available arrival cities from the selected departure city
show_available_options(unique_arrival_cities)

# Call function to let the user select one of the available arrival cities
selected_arrival_city = selection_process(user_selection, unique_arrival_cities)

# Ask the user when they want to leave
print("When do you want to leave?")

# Filter dataframe to obtain only observations with the flight date for the selected arrival city from the selected departure city
df_departure_dates = df_arrival_cities[df_arrival_cities["arrival_city"] == selected_arrival_city]
unique_departure_dates = df_departure_dates["flight_date"].unique()
unique_departure_dates.sort()

# Call function to show available flights for the selected arrival city from the selected departure city
show_available_options(unique_departure_dates)

# Call function to let the user select one of the available departure dates for the selected arrival city from the selected departure city

selected_departure_date = selection_process(user_selection, unique_departure_dates)

# Filter dataframe to obtain only observations with the flights corresponding to the selected arrival city from the selected departure city on the selected departure date
filtered_departure_df_flights = df_flights.loc[(df_flights["departure_city"] == selected_departure_city) & (df_flights["arrival_city"] == selected_arrival_city) & (df_flights["flight_date"] == selected_departure_date)]

# Retrieve only the corresponding flight numbers
unique_departure_flight_numbers = filtered_departure_df_flights["flight_number"].unique()

# Show the available flights
print(f"These are the available flights from {selected_departure_city} to {selected_arrival_city} on {selected_departure_date}:")
show_available_flights(filtered_departure_df_flights)

# Call function to let the user select one of the available flights
print("Which flight do you prefer?\n")
selected_departure_flight = selection_process(user_selection, unique_departure_flight_numbers)

# Ask the user when they want to come back
print("When do you want to come back?")

# Filter dataframe to obtain only observations with the return flights from the selected arrival city to the selected departure city after the departure date
df_return_dates = df_flights.loc[(df_flights["departure_city"] == selected_arrival_city ) & (df_flights["arrival_city"] == selected_departure_city) & (df_flights["flight_date"] > selected_departure_date)]
unique_return_dates = df_return_dates["flight_date"].unique()
unique_return_dates.sort()

# Call function to show available dates to come back
show_available_options(unique_return_dates)

# Call function to let the user select the date to come back
selected_return_date = selection_process(user_selection, unique_return_dates)

# Filter dataframe to obtain flights to come back in the selected date
filtered_return_df_flights = df_return_dates[df_return_dates["flight_date"] == selected_return_date]

# Retrieve only the corresponding flight numbers
unique_return_flight_numbers = filtered_return_df_flights["flight_number"].unique()

# Show the available flights
print(f"These are the available flights from {selected_arrival_city} to {selected_departure_city} on {selected_return_date}:")
show_available_flights(filtered_departure_df_flights)

# Call function to let the user select one of the available flights
print("Which flight do you prefer?\n")
selected_return_flight = selection_process(user_selection, unique_return_flight_numbers)

# Ask the user if they want an extra baggage
print("Do you want to add an additional baggage for £ 47?")
show_available_options(boolean_selection_list)

# Call function to let the user select if they want the service
selected_extra_baggage = selection_process(user_selection, boolean_selection_list)

# Ask the user if they want to rent a car
print("Do you want to rent a car for £ 51 per day?")
show_available_options(boolean_selection_list)

# Call function to let the user select if they want the service
selected_rental_car = selection_process(user_selection, boolean_selection_list)

# Ask the user if they want a travel insurance
print("Do you want to add a travel insurance to your trip for £ 6 per day?")
show_available_options(boolean_selection_list)

# Call function to let the user select if they want the service
selected_travel_insurance = selection_process(user_selection, boolean_selection_list)

# Retrieve all the needed values from the file corresponding to the user selection
selected_departure_time = retrieve_flight_info(selected_departure_flight, "flight_time")
selected_departure_company = retrieve_flight_info(selected_departure_flight, "flight_company")
selected_departure_duration = retrieve_flight_info(selected_departure_flight, "duration_minutes")
selected_departure_price = retrieve_flight_info(selected_departure_flight, "ticket_price")
selected_return_time = retrieve_flight_info(selected_return_flight, "flight_time")
selected_return_company = retrieve_flight_info(selected_return_flight, "flight_company")
selected_return_duration = retrieve_flight_info(selected_return_flight, "duration_minutes")
selected_return_price = retrieve_flight_info(selected_return_flight, "ticket_price")

# Calculate number of trip days
date_format = "%d/%m/%y"
departure_day = datetime.strptime(selected_departure_date, date_format)
return_day = datetime.strptime(selected_return_date, date_format)
trip_days = return_day - departure_day


# Calculated costs
cost_extra_baggage = service_extra_baggage * transform_bool_to_int(selected_extra_baggage)
print("-----")
print(cost_extra_baggage)
print("-----")
cost_car_rental = service_car_rental_per_day * trip_days.days * transform_bool_to_int(selected_rental_car)
cost_travel_insurance = service_travel_insurance_per_day * trip_days.days * transform_bool_to_int(selected_travel_insurance)
total_cost = float(selected_departure_price) + float(selected_return_price) + int(cost_extra_baggage) + float(cost_car_rental) + float(cost_travel_insurance)

# Show the user all the costs per single service and the total cost of the flight
print(f"""Great! Here's your trip summary:
      
DEPARTURE: {selected_departure_date} at {selected_departure_time} | {selected_departure_city} \u2b95 {selected_arrival_city}
Flight number: {selected_departure_flight} | {selected_departure_company} | Duration: {selected_departure_duration} minutes
Ticket price: £ {selected_departure_price}
---
DEPARTURE: {selected_return_date} at {selected_return_time} | {selected_arrival_city} \u2b95 {selected_departure_city}
Flight number: {selected_return_flight} | {selected_return_company} | Duration: {selected_return_duration} minutes
Ticket price: £ {selected_return_price}
---
EXTRA LUGGAGE: {selected_extra_baggage}
Cost: £ {cost_extra_baggage}
---
CAR RENTAL: {selected_rental_car}
Cost: £ {cost_car_rental}
---
TRAVEL INSURANCE: {selected_travel_insurance}
Cost: £ {cost_travel_insurance}
---
Total cost of the trip: £ {total_cost}

Enjoy your trip!
""")
