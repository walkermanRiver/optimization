import optuna
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
import numpy as np


# 定义目标函数，这里以一个简单的函数为例
def objective_function(x):
    return np.sin(x[0]) + np.cos(x[1])


# 定义 Optuna 优化的目标函数
def optuna_objective(trial):
    # 定义搜索空间
    x1 = trial.suggest_uniform('x1', -5, 5)
    x2 = trial.suggest_uniform('x2', -5, 5)
    x = np.array([x1, x2])

    # 获取目标函数值
    y = objective_function(x)

    return y


# 定义一个使用 GPR 作为代理模型的采样器
class GPRSampler(optuna.samplers.BaseSampler):
    def __init__(self):
        self.gpr = GaussianProcessRegressor(kernel=Matern(nu=2.5))
        self.X = []
        self.y = []

    def infer_relative_search_space(self, study, trial):
        return optuna.samplers.intersection_search_space(study)

    def sample_relative(self, study, trial, search_space):
        return {}

    def sample_independent(self, study, trial, param_name, param_distribution):
        if len(self.X) > 0:
            # 训练 GPR 模型
            self.gpr.fit(self.X, self.y)

            # 定义一个简单的采集函数（这里使用期望改进）
            def acquisition_function(x):
                mu, std = self.gpr.predict(np.array(x).reshape(1, -1), return_std=True)
                best_y = np.min(self.y)
                z = (best_y - mu) / std
                ei = (best_y - mu) * (1 + np.sign(z)) / 2 + std * np.exp(-z ** 2 / 2) / np.sqrt(2 * np.pi)
                return -ei

            # 随机生成一些候选点
            n_candidates = 100
            candidates = []
            if isinstance(param_distribution, optuna.distributions.UniformDistribution):
                low = param_distribution.low
                high = param_distribution.high
                for _ in range(n_candidates):
                    candidate = [np.random.uniform(low, high) for _ in range(len(self.X[0]))]
                    candidates.append(candidate)

            # 选择具有最大采集函数值的候选点
            best_candidate = None
            best_acquisition = float('-inf')
            for candidate in candidates:
                acq = acquisition_function(candidate)
                if acq > best_acquisition:
                    best_acquisition = acq
                    best_candidate = candidate

            if best_candidate is not None:
                if param_name == 'x1':
                    return best_candidate[0]
                elif param_name == 'x2':
                    return best_candidate[1]

        # 如果没有足够的数据，随机采样
        return param_distribution.single_sample()

    def after_trial(self, study, trial, state, values):
        if state == optuna.trial.TrialState.COMPLETE:
            x1 = trial.params['x1']
            x2 = trial.params['x2']
            self.X.append([x1, x2])
            self.y.append(values[0])


if __name__ == "__main__":
    # 创建 Optuna 研究对象
    study = optuna.create_study(sampler=GPRSampler())

    # 运行优化
    study.optimize(optuna_objective, n_trials=20)

    # 输出最优结果
    best_trial = study.best_trial
    print(f"Best value: {best_trial.value}")
    print(f"Best parameters: {best_trial.params}")    