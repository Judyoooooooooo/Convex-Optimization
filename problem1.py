import cvxpy as cp

x = cp.Variable(pos=True) 
y = cp.Variable(pos=True)
objective_fn = 2 * x + y
objective = cp.Minimize(objective_fn)
constraints = [(1/x + 1/y) <= 1]
problem = cp.Problem(objective, constraints)
problem.solve(gp=True)
print("Optimal value: ", problem.value)
print("x: ", x.value)
print("y: ", y.value)
print("Verify constraint: " ,(1/x.value)+(1/y.value), "<=" , "1")
