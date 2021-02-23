#This is a first python program.

no_of_initial_flights=int(input('enter initial no of flights in airport='))
no_of_flights_landed=int(input('enter no of flightslanded='))
no_of_flights_tookof=int(input('enter no of flights tokoff='))

#calculate the current of flights

current_no_of_flights=no_of_initial_flights + no_of_flights_landed - no_of_flights_tookof
print('The current no of flights :',current_no_of_flights)