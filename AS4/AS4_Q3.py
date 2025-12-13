import numpy as np
from scipy.optimize import minimize
#定义函数
def cost_function(P):
    P1, P2, P3 = P
    C1 = 0.02 * P1**2 + 10 * P1 + 100
    C2 = 0.03 * P2**2 + 8 * P2 + 120
    C3 = 0.025 * P3**2 + 9 * P3 + 150
    total = C1 + C2 + C3
    return total
#定义约束
def constraint(P):
    return np.sum(P) - 300
#加载约束，定义域，猜测值
constraints = ({'type': 'eq', 'fun':constraint})
bounds = [(50, 150),(50, 100),(50, 120)]
x0 = np.array([120, 100, 80])
#进行优化
result = minimize(fun=cost_function , x0=x0 ,method='SLSQP', bounds=bounds,constraints=constraints)
if result.success:
    P_optimal = result.x
    P1_opt, P2_opt, P3_opt = P_optimal
    C_total_opt = result.fun
    print("Optimal Power Outputs:")
    print(f"P1: <{int(round(P1_opt,0))} in MW>")
    print(f"P2: <{int(round(P2_opt,0))} in MW>")
    print(f"P3: <{int(round(P3_opt,0))} in MW>")
    print(f"Total Generation Cost: <${int(round(C_total_opt,0))}>")
