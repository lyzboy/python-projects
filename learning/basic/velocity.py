import math

def time(height):
    gravity = 9.8
    return math.sqrt((2*height)/gravity)

def velocity(distance, time):
    return distance / time


drop_height = 0.5
distance = 2.38
time_of_flight = (time(drop_height))
initial_velocity = velocity(distance, time_of_flight)

print(f'Drop height = {drop_height} | Distance = {distance}\nTime of Flight = {time_of_flight}\nInitial Velocity={initial_velocity}')

drop_height = 0.9
distance = 2.98
time_of_flight = (time(drop_height))
initial_velocity = velocity(distance, time_of_flight)

print(f'Drop height = {drop_height} | Distance = {distance}\nTime of Flight = {time_of_flight}\nInitial Velocity={initial_velocity}')