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