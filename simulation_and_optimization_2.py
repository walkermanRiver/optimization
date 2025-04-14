### Step 1: Define the Objective and Constraints
- **Objective:** Maximize the expected return of the portfolio.
- **Constraint:** Control the risk of loss to 10% (Value at Risk, VaR, or Conditional Value at Risk, CVaR).

### Step 2: Gather Data
- **Historical Returns:** Collect historical return data for the three assets.
- **Expected Returns:** Estimate the expected returns based on historical data or other financial models.
- **Covariance Matrix:** Calculate the covariance matrix of the returns to understand how the assets move relative to each other.

### Step 3: Formulate the Optimization Problem
- **Expected Return (ER):** \( ER = w_1 \mu_1 + w_2 \mu_2 + w_3 \mu_3 \)
  - \( w_1, w_2, w_3 \) are the weights of the assets in the portfolio.
  - \( \mu_1, \mu_2, \mu_3 \) are the expected returns of the assets.
- **Risk (Variance):** \( \sigma^2 = w^T \Sigma w \)
  - \( \Sigma \) is the covariance matrix of the asset returns.
- **Value at Risk (VaR):** Use historical simulation, parametric methods, or Monte Carlo simulation to estimate VaR.

### Step 4: Optimization Algorithm
To solve the optimization problem, you can use various algorithms. One common approach is using quadratic programming (QP) for mean-variance optimization. Another approach is using linear programming (LP) for CVaR optimization.

#### Mean-Variance Optimization (Quadratic Programming)
1. **Objective Function:** Maximize \( w^T \mu \)
2. **Constraints:**
   - \( w^T \Sigma w \leq \sigma^2 \) (Risk constraint)
   - \( \sum w_i = 1 \) (Weights sum to 1)
   - \( w_i \geq 0 \) (No short selling, if applicable)

#### CVaR Optimization (Linear Programming)
1. **Objective Function:** Minimize CVaR subject to expected return constraints.
2. **Constraints:**
   - Use linear programming to minimize CVaR at the 10% risk level.
   - Ensure the portfolio's expected return meets a certain threshold.

### Step 5: Implement the Algorithm
You can use various software tools and libraries to implement these algorithms, such as:
- **Python:** Libraries like `cvxpy`, `numpy`, and `pandas` for optimization and data handling.
- **R:** Packages like `quadprog` for quadratic programming.

### Step 6: Backtesting and Validation
- **Backtesting:** Test the optimized portfolio on historical data to validate its performance.
- **Stress Testing:** Assess how the portfolio performs under different market conditions.

### Example in Python (Quadratic Programming)
```python
import numpy as np
import cvxpy as cp

# Expected returns
mu = np.array([0.1, 0.12, 0.14])

# Covariance matrix
Sigma = np.array([[0.005, -0.010, 0.004],
                  [-0.010, 0.040, -0.002],
                  [0.004, -0.002, 0.023]])

# Portfolio weights
w = cp.Variable(3)

# Objective: Maximize expected return
objective = cp.Maximize(mu @ w)

# Constraints
constraints = [cp.quad_form(w, Sigma) <= 0.01,  # Variance constraint
               cp.sum(w) == 1,                  # Sum of weights is 1
               w >= 0]                          # No short selling

# Problem definition
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve()

# Optimal weights
optimal_weights = w.value
print("Optimal Weights:", optimal_weights)
```

This example demonstrates a simple mean-variance optimization using quadratic programming in Python. You can adapt this approach to include CVaR constraints or other risk measures as needed.