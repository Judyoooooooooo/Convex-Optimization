import cvxpy as cp
import numpy as np
import math as m
import matplotlib.pyplot as plt

print("-----Problem 3(c)-----")
x = cp.Variable(2, pos=True)  
c = 2

objective_fn = x[0] * x[1]
objective = cp.Maximize(objective_fn)
constraints = [x[0] + c * x[1] <= 1, cp.norm(x) <= 1/m.sqrt(2)]
problem = cp.Problem(objective, constraints)
problem.solve(qcp=True)
print("Optimal value: ", problem.value)
print("Optimal point x1: ", x[0].value)
print("Optimal point x2: ", x[1].value)
###Verify###
print("-----Verify-----")
print("Verify constraint 1 :", (x[0].value + c * x[1].value))
print("Verify constraint 2 :", cp.norm(x).value - 1/m.sqrt(2))

print("  ")
print("  ")
print("  ")
print("-----Problem 3(d)、3(e)-----")
x = cp.Variable(2, pos=True)  
c = np.array([0.5, 1, 2, 3, 4])
optim_val = []

objective_fn = x[0] * x[1]
objective = cp.Maximize(objective_fn)
print("---Determine active or inactive---")
for i in range(len(c)):
    constraints = [x[0] + c[i] * x[1] <= 1, cp.norm(x) <= 1/m.sqrt(2)]
    problem = cp.Problem(objective, constraints)
    problem.solve(qcp=True)
    optim_val.append(problem.value)
    #print("Optimal value: ", problem.value)
    print("Optimal point x when c", [i], ":",  x[0].value, x[1].value)

    print("Verify constraint 1 :", x[0].value + c[i] * x[1].value - 1)
    #print("Verify constraint 2 :", (x[0].value**2 + x[1].value**2)  - 0.5)
    print("Verify constraint 2 :",(cp.norm(x) - 1/m.sqrt(2)).value)
    print("  ")
plt.plot(c, optim_val)
plt.scatter(c, optim_val)
plt.xlabel('c')
plt.ylabel('optimal value')
plt.show()

