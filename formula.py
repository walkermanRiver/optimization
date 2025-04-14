variable
    invest_rate1
    invest_rate2
    invest_rate3

    invest_amount1
    invest_amount2
    invest_amount3

restriction
    invest_rate1: [-0.2, 0.3]
    invest_rate2: [0.1, 0.4]
    invest_rate3: [-0.3, 0.5]

    invest_amount1 + invest_amount2 + invest_amount3 = 100

    risk of loss(possibility of invest_return < 15) < 10%

target
    invest_retrun = invest_amount1 * invest_rate1 + invest_amount2 * invest_rate2 + invest_amount3 * invest_rate3

calculation
    portfolio_collection = []
    loop each invest_amount portfolio
        do Monte Carlo calculation, 
        check the possibility of invest_return < 15 
        if( possibility < 10%){
            add invet_amount into portfolio_collection
        }
    end loop

    get the biggest invest return in portfolio_collection






# invest_rate
# invest_amount
# 两个高斯分布乘积的理论推导:https://blog.csdn.net/chaosir1991/article/details/106910668

ir1 = f(u1,σ1)
ir2 = f(u2,σ2)
ir3 = f(u3,σ3)
invest_retrun = ia1 * ir1 + ia2 * ir2 + ia3 * ir3 = f(ia1*u1+ia2*u2+ia3*u3,ia1^2*σ1^2+ia2^2*σ2^2+ia3^2*σ3^2)

calculation
best_invest_return = optimie(invest_return)

# 目标是在一个预期收益水平下降低投资组合的风险，或者是在一个可以接受的风险水平下实现最大的投资回报。
# 最大化预期回报并最小化风险




optimization rule
target = fn(x1, x2,...xn)

1. 线性/非线性
2. 连续/离散
3. 
