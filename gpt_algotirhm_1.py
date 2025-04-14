you are one AI algorithm engineer, you need consider how to solve the issue below:
there are 3 investment targets, each investment target has one return rate range below
invest_rate1: [-0.2, 0.3]
invest_rate2: [0.1, 0.4]
invest_rate3: [-0.3, 0.5]

there is one investment to the 3 investment targets, the restricition are following:
1. each investment target has one investment amount, the sum of the 3 investment amounts is 100.
2. each investment target need be invested at least 5%.
3. the invest_retrun = invest_amount1 * invest_rate1 + invest_amount2 * invest_rate2 + invest_amount3 * invest_rate3

how to invest the 3 investment targets, and get the max invest return, and the invest risk of loss less than 10%.

please provide the process and algorithm, and also provide the python code to implement the algorithm.


To tackle this problem, we can frame it as a **constrained optimization problem**. Considering the given return rate ranges and minimum investment constraints, we will utilize optimization techniques, specifically stochastic programming or robust optimization due to the uncertainty in returns. Here’s a structured approach to solving this problem:

### Step-by-Step Process:

1. **Define Variables:**
- Let \( w_1, w_2, w_3 \) be the portfolio weights for target1, target2, and target3 respectively.
- Ensure the weights sum up to 1, i.e., \( w_1 + w_2 + w_3 = 1 \).
- Each weight \( w_i \) must be at least 5%, i.e., \( w_i \geq 0.05 \).

2. **Define Return Distributions:**
- Assume the returns for each target follow a uniform distribution based on the given ranges.
- Let \( r_1 \sim \text{Uniform}(-0.2, 0.3) \), \( r_2 \sim \text{Uniform}(0.1, 0.4) \), \( r_3 \sim \text{Uniform}(-0.3, 0.5) \).

3. **Define Objective and Constraints:**
- Our objective is to maximize the expected return \( \mathbb{E}[R_p] \).
- The total portfolio return is \( R_p = w_1 r_1 + w_2 r_2 + w_3 r_3 \).
- The constraint is that the probability of the portfolio return being less than zero should be less than or equal to 10%.

4. **Optimization Model:**

Formulate the optimization problem:

\[
\text{maximize } \mathbb{E}[R_p] = w_1 \mathbb{E}[r_1] + w_2 \mathbb{E}[r_2] + w_3 \mathbb{E}[r_3]
\]

Subject to:

\[
P(R_p < 0) \leq 0.1
\]

\[
w_1 + w_2 + w_3 = 1
\]

\[
w_1 \geq 0.05, \quad w_2 \