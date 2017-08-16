price_per_kWh = float(input("Enter cents per kWh: "))
daily_kWh_use = float(input("Enter daily use in kWh: "))
billing_period_days = float(input("Enter number of billing days: "))
estimated_bill = (price_per_kWh / 100) * daily_kWh_use * billing_period_days
print("Estimated bill: ${:.2f}".format(estimated_bill))
