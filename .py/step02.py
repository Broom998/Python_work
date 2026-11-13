# A
SLICES_PER_PIZZA = 8
PIZZA_PRICE = 12.99
SLICE_PRICE = 2.25

host_name = input("Enter the host's name: ")
people = int(input("Enter the number of people: "))
slices_per_person = int(input("Enter the number of slices per person: "))

total_slices = people * slices_per_person
whole_pizzas = total_slices // SLICES_PER_PIZZA
extra_slices = total_slices % SLICES_PER_PIZZA
total_cost = whole_pizzas * PIZZA_PRICE + extra_slices * SLICE_PRICE
cost_per_person = total_cost / people

print(f"\nHost: {host_name}")
print(f"Number of people: {people}")
print(f"Slices per person: {slices_per_person}")

print(f"=== Pizza Plan for {host_name}'s Party ===")
print(f"Total slices needed: {total_slices}")
print(f"Whole pizzas to order: {whole_pizzas}")
print(f"Extra slices to buy individually: {extra_slices}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# B
AVERAGE_SPEED = 55
destination = input("Destination: ")
miles = float(input("Trip distance (miles): "))
mpg = float(input("Car's miles per gallon: "))
gas_price = float(input("Gas price per gallon: "))
people = int(input("Number of people splitting the cost: "))
gallons = miles / mpg
gas_cost = gallons * gas_price
cost_per_person = gas_cost / people
total_minutes = int((miles / AVERAGE_SPEED) * 60)
hours = total_minutes // 60
leftover_minutes = total_minutes % 60
round_trip_gas = gas_cost * 2
print()
print(f"--- Trip to {destination} ---")
print(f"Gallons of gas:   {gallons:.1f}")
print(f"Gas cost:         ${gas_cost:.2f}")
print(f"Cost per person:  ${cost_per_person:.2f}")
print(f"Driving time:     {hours} hr {leftover_minutes} min (at {AVERAGE_SPEED} mph)")
print(f"Round trip gas:   ${round_trip_gas:.2f}")

# C
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52
employee_name = input("Employee name: ")
hourly_rate = float(input("Hourly pay rate: "))
hours_worked = float(input("Hours worked this week: "))
gross_pay = hourly_rate * hours_worked
federal_tax = gross_pay * FEDERAL_TAX_RATE
state_tax = gross_pay * STATE_TAX_RATE
social_security_tax = gross_pay * SOCIAL_SECURITY_RATE
medicare_tax = gross_pay * MEDICARE_RATE
total_deductions = federal_tax + state_tax + social_security_tax + medicare_tax
net_pay = gross_pay - total_deductions
percent_kept = (net_pay / gross_pay) * 100
yearly_gross = gross_pay * WEEKS_PER_YEAR
yearly_net = net_pay * WEEKS_PER_YEAR
print()
print("=" * 32)
print(f"PAY STUB: {employee_name}")
print("=" * 32)
print(f"Hours worked:      {hours_worked:.1f}")
print(f"Hourly rate:       ${hourly_rate:.2f}")
print(f"Gross pay:         ${gross_pay:.2f}")
print("-" * 32)
print(f"Federal tax (10%): ${federal_tax:.2f}")
print(f"State tax (3.5%):  ${state_tax:.2f}")
print(f"Social Security:   ${social_security_tax:.2f}")
print(f"Medicare:          ${medicare_tax:.2f}")
print(f"Total taken out:   ${total_deductions:.2f}")
print("-" * 32)
print(f"NET PAY:           ${net_pay:.2f}")
print("=" * 32)
print(f"You keep {percent_kept:.1f}% of what you earn.")
print(f"Yearly gross: ${yearly_gross:.2f}")
print(f"Yearly net:   ${yearly_net:.2f}")