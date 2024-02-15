#Electricity Bill Calculation 
def calculate_electricity_bill(customer_id, customer_name, units_consumed):

  # Define the charging rates and fuel surcharge
  charges_per_unit = {
    "Upto 199": 1.20,
    "200-399": 1.50,
    "400-499": 1.80,
    "600+": 2.00,
  }
  fuel_surcharge_rate = 0.10

  # Calculate the total charge based on the charging rates
  if units_consumed <= 199:
    total_charge = units_consumed * charges_per_unit["Upto 199"]
  elif units_consumed <= 399:
    total_charge = units_consumed * charges_per_unit["200-399"]
  elif units_consumed <= 499:
    total_charge = units_consumed * charges_per_unit["400-499"]
  else:
    total_charge = units_consumed * charges_per_unit["600+"]

  # Calculate the fuel surcharge
  fuel_surcharge = total_charge * fuel_surcharge_rate

  # Calculate the total bill
  total_bill = total_charge + fuel_surcharge

  # Return the results as a dictionary
  return {
    "customer_id": customer_id,
    "customer_name": customer_name,
    "units_consumed": units_consumed,
    "total_charge": total_charge,
    "fuel_surcharge": fuel_surcharge,
    "total_bill": total_bill,
  }

# Get input from the user
customer_id = input("Enter customer ID: ")
customer_name = input("Enter customer name: ")

while True:
  try:
    units_consumed = int(input("Enter units consumed: "))
    if units_consumed >= 0:
      break
    else:
      print("Units consumed cannot be negative. Please enter a valid number.")
  except ValueError:
    print("Invalid input. Please enter an integer for units consumed.")

# Calculate and display the bill details
bill_details = calculate_electricity_bill(customer_id, customer_name, units_consumed)

print("Electricity Bill Details:")
print(f"Customer ID: {bill_details['customer_id']}")
print(f"Customer Name: {bill_details['customer_name']}")
print(f"Units Consumed: {bill_details['units_consumed']}")
print(f"Total Charge: KSH {bill_details['total_charge']:.2f}")
print(f"Fuel Surcharge: KSH {bill_details['fuel_surcharge']:.2f}")
print(f"Total Bill: KSH {bill_details['total_bill']:.2f}")

  
  