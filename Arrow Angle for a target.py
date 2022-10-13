import math
#Sets initial values
time = 0
t_step = 0.1
x_old = 0
y_old = 1.5
g = 9.8
angle = 0
vy_old=65*math.sin(angle*math.pi/180)
vx_old = 65*math.cos(angle*math.pi/180)

# Asks the user the distance
objective = int(input("How many meters do you want your arrow to reach?: "))

#Update options
x_new = x_old + vx_old * t_step
y_new = y_old + vy_old * t_step
vy_new = vy_old - g*t_step
time+=t_step

# Loop until the arrow hits the ground
while y_new>0:
    #Update old values from new values
    x_old = x_new
    y_old = y_new
    vy_old = vy_new
    #Update positions and velocities
    x_new = x_old + vx_old * t_step
    y_new = y_old + vy_old * t_step
    vy_new = vy_old - g*t_step
    time+=t_step
    # Breaks the loop if the objective is reached when the arrow is at least 0.01 meters off the ground
    if x_new>objective and y_new<0.01:
        # Prints out the angle needed to reach the objective and breaks the loop
        print(f"Shooting the arrow at {angle} degrees will just about reach {objective} meters")
        break
    # If the arrow reaches the ground, but hasn't reached the objective, the y_new, x_new and time variables are reset, and the angle increases
    elif y_new<0:
        time = 0
        t_step = 0.1
        x_old = 0
        y_old = 1.5
        g = 9.8
        vy_old=65*math.sin(angle*math.pi/180)
        vx_old = 65*math.cos(angle*math.pi/180)
        #Update options
        x_new = x_old + vx_old * t_step
        y_new = y_old + vy_old * t_step
        vy_new = vy_old - g*t_step
        time+=t_step
        # Increases the angle by 1
        angle+=1
        # If the angle is above 90, it's impossible for the arrow to reach the target, so this stops the loop.
        if angle>90:
            print("Your objective is unreachable at the current speed")
            break
