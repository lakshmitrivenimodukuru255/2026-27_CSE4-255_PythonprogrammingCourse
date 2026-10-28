adult_fare=200
child_fare=50

print(f"Ticket Prices -- Adult: Rs.{adult_fare} | Child: Rs.{child_fare}")

adult_count = int(input("Enter number of adults traveled: "))
child_count = int(input("Enter number of children traveled: "))

Adult_revenue = adult_count * adult_fare
Child_revenue = child_count * child_fare
total_expected = Adult_revenue + Child_revenue

actual_collected = float(input("Enter total actual money collected (Rs.): "))
difference = actual_collected - total_expected

print("Total Expected Revenue: Rs.", total_expected)
print("Total Actual Collected: Rs.", actual_collected)

if difference == 0:
    print("Status: Perfect! Revenue matches completely (No difference).")
elif difference > 0:
    print("Status: Extra money collected by: Rs.", difference)
else:
    print("Status: Shortage! Revenue is missing by: Rs.", difference)
