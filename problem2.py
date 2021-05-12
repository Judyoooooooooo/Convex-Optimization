import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

#generate data
print("-----Problem 2(b)-----")
n = 5
p = 3
np.random.seed(1)
optim_val = []

a = np.array(range(1, n+1))
x = cp.Variable(n)
objective_fn = cp.pnorm(x,p) + (a @ x)
objective = cp.Minimize(objective_fn)
constraints = [cp.harmonic_mean(x) >= n]
problem = cp.Problem(objective, constraints)
problem.solve()

print("Optimal value: ", problem.value)
for i in range(len(a)):   
    print("Optimal point of ", "x",[i+1], ":", x.value[i])


print("-----Problem 2(c)-----")
n = 5
np.random.seed(1)
optim_val = []

a = np.array(range(1, n+1))
x = cp.Variable(n)

P = np.linspace(start=1, stop=100, num=100)
for p in P:   
    objective_fn = cp.pnorm(x,p) + (a @ x)
    objective = cp.Minimize(objective_fn)
    constraints = [cp.harmonic_mean(x) >= n]
    problem = cp.Problem(objective, constraints)
    problem.solve()
    optim_val.append(problem.value)
plt.scatter(P, optim_val)
plt.plot(P, optim_val)
plt.xlabel('p')
plt.ylabel('optimal value')
plt.show()
