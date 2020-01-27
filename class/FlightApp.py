from Flight import * 

flights = []

f1 = Flight("TK1234", "Ankara",	"Antalya", 250)
f2 = Flight("LH8686", "Munich",	"Tokyo", 290)
f3 = Flight("TK9897", "Tokyo",	"Paris", 195)

flights.append(f1)
flights.append(f2)
flights.append(f3)

flights.append(Flight("TK5432","Antalya","Tokyo",250))

print("Originally: ")
print(flights)

flights.sort()

print("\nSorted: ")
print(flights)

total = 0

for flight in flights:
    total += flight.calculateOperatingCost()

print("Total cost: ")
print(total)

for flight in flights:
    if flight.getDestination() == "Tokyo":
        print("\n" + str(flight))
