TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


traiff_used = float(input("Which tariff? 11 or 31: "))
if traiff_used == 11:
    price_per_kWh = TARIFF_11
elif traiff_used == 31:
    price_per_kWh = TARIFF_31
else:
    print("!!UNKNOWN TRAIFF!! CALCULATION WILL RESULT IN ZERO")
    price_per_kWh = 0
daily_kWh_use = float(input("Enter daily use in kWh: "))
billing_period_days = float(input("Enter number of billing days: "))
estimated_bill = price_per_kWh * daily_kWh_use * billing_period_days
print("Estimated bill: ${:.2f}".format(estimated_bill))
