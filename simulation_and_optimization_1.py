### 1. 蒙特卡罗模拟风险

假设你有一个投资组合，包括三种资产：股票、债券和现金。你希望通过蒙特卡罗模拟来估算这个组合的风险。

#### 步骤：
1. **定义参数**：假设股票的年回报率为10%，年波动率为20%；债券的年回报率为5%，年波动率为7%；现金的年回报率为1%，年波动率为1%。
2. **生成随机样本**：使用正态分布生成未来一年每种资产的回报率。
3. **计算组合回报率**：根据不同的资产权重组合，计算每个组合的年回报率。
4. **重复模拟**：重复上述过程10000次，得到回报率的分布。
5. **估算风险**：计算组合回报率的标准差作为风险指标。

```python
import numpy as np

# 定义参数
n_simulations = 10000
weights = np.array([0.5, 0.3, 0.2])  # 股票、债券、现金的权重
mean_returns = np.array([0.10, 0.05, 0.01])
volatilities = np.array([0.20, 0.07, 0.01])

# 生成随机样本
simulated_returns = np.random.normal(mean_returns, volatilities, (n_simulations, len(weights)))

# 计算组合回报率
portfolio_returns = np.dot(simulated_returns, weights)

# 估算风险
portfolio_risk = np.std(portfolio_returns)

print(f"组合的估算风险（标准差）：{portfolio_risk:.4f}")

### 2. 运行优化

假设你希望在规定的风险水平下，找到最优的资产权重组合。

#### 步骤：
1. **定义目标函数**：最大化组合的夏普比率（回报率与风险的比率）。
2. **设定约束**：组合的风险不能超过某个阈值，比如0.12。
3. **使用优化算法**：使用SciPy库中的优化函数进行求解。

mport scipy.optimize as sco

# 定义目标函数：负的夏普比率（因为优化函数默认是最小化）
def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.01):
    portfolio_return = np.dot(weights, mean_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    return -sharpe_ratio

# 定义约束和边界
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1},  # 权重和为1
               {'type': 'ineq', 'fun': lambda x: 0.12 - np.sqrt(np.dot(x.T, np.dot(cov_matrix, x)))})  # 风险约束
bounds = tuple((0, 1) for _ in range(len(weights)))

# 初始猜测
initial_guess = len(weights) * [1. / len(weights)]

# 运行优化
result = sco.minimize(negative_sharpe_ratio, initial_guess, args=(mean_returns, cov_matrix),
                      method='SLSQP', bounds=bounds, constraints=constraints)

optimal_weights = result.x

print(f"最优的资产权重组合：{optimal_weights}")
```

### 总结
通过上述步骤，你可以使用蒙特卡罗模拟来估算投资组合的风险，然后在设定的风险水平下，使用优化算法找到最优的资产权重组合。这个例子展示了如何结合模拟和优化技术来进行投资决策。