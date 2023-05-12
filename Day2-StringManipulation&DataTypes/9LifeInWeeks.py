age = int(input("What is your current age?\n"))
expectancy = 90
days = (expectancy - age) * 365
months = (expectancy - age) * 12
weeks = (expectancy - age) * 52
print(f"You have {days} days, {weeks} weeks and {months} months left.")
