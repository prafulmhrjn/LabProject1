''' If temperature is greater than 30, it's a hot day otherwise if it's less than 10, it's a cold day,
otherwise it's neither hot neither cold.
'''

temperature_today = float(input("Enter the temperature:"))
if temperature_today>30:
    print(f"It's a hot day")
if temperature_today<10:
    print(f"It's a cold day.")
if temperature_today>10<30:
    print(f"It's neither hot neither cold.")

