import matplotlib.pyplot as plt
import math
import numpy as np

graphs = int(input("Enter the number of graphs: "))

for i in range(0, graphs):
    gravity = 9.81

    velocity = int(input("Enter the initial Velocity (m/s): "))
    angle = int(input("Enter the angle measured in degrees: "))
    radian = (math.pi/180)*angle
    time_flight = (2*velocity*(math.sin(radian)))/gravity
    height = ((velocity**2)*(math.sin(radian)**2))/(2*gravity)
    horizontal_range = ((velocity**2)*(math.sin(radian * 2)))/gravity

    numx = []
    numy = []

    for i in (np.arange(0, 1000, 0.001)):
        x_distance = velocity * i
        x_velocity = math.cos(radian) * velocity
        y_distance = ((math.sin(radian) * velocity) * i) - (gravity * (i**2))/2
        y_velocity = (math.sin(radian) * velocity) - (gravity * i)
        if y_distance >= 0:
            numx.append(x_distance)
            numy.append(y_distance)

    plt.plot(numx, numy)

plt.show()
