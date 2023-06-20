temp=float(input("Enter the temperature:"))
if temp>35:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif temp>25: #temp=(25,35]
    print("It's a nice day.")
elif temp>10:#temp=(10,25]
    print("It's a bit cold.")
else:
    print("It's cold.2")
print("Pray to your god.")
