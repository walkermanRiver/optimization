# example of bayesian optimization for a 1d function from scratch
from math import sin
from math import pi
from numpy import arange
from numpy import vstack
from numpy import argmax
from numpy import asarray
from numpy.random import normal
from numpy.random import random
from scipy.stats import norm
from sklearn.gaussian_process import GaussianProcessRegressor
from warnings import catch_warnings
from warnings import simplefilter
# from matplotlib import pyplot

import numpy as np
import scipy.stats as sps
from sklearn.datasets import load_iris
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern


from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# 创建形状为 (6, 2) 的 NumPy 数组 bounds
bounds = np.array([[1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100]])

# objective function
def objective(params):    
	global count  # Declare count as global   
	count = count + 1
	return sum(params)

# surrogate or approximation for the objective function
def surrogate(model, X):
	# catch any warning generated when making a prediction
	with catch_warnings():
		# ignore generated warnings
		simplefilter("ignore")
		return model.predict(X, return_std=True)

# probability of improvement acquisition function
def acquisition(Xsamples, model):
	# calculate the best surrogate score found so far
	mu, sigma = surrogate(model, X)
	f_best = np.max(mu)
	improvement = f_best - mu
	with np.errstate(divide='warn'):
		Z = improvement / sigma if sigma > 0 else 0
		ei = improvement * sps.norm.cdf(Z) + sigma * sps.norm.pdf(Z)
		ei[sigma == 0.0] == 0.0
	return ei





	# best = max(yhat)
	# # calculate mean and stdev via surrogate function
	# mu, std = surrogate(model, Xsamples)
	# # mu = mu[:, 0]
	# # calculate the probability of improvement
	# probs = norm.cdf((mu - best) / (std+1E-9))
	# return probs

# optimize the acquisition function
def opt_acquisition(X, y, model):
	global bounds
	# random search, generate random samples
	Xsamples = np.random.uniform(low=bounds[:, 0], high=bounds[:, 1], size=(100, 6))
	# Xsamples = random(100)
	# Xsamples = Xsamples.reshape(len(Xsamples), 1)
	# calculate the acquisition function for each sample
	scores = acquisition(Xsamples, model)
	# locate the index of the largest scores
	ix = argmax(scores)
	return Xsamples[ix, 0]

# plot real observations vs surrogate function
# def plot(X, y, model):
# 	# scatter plot of inputs and real objective function
# 	pyplot.scatter(X, y)
# 	# line plot of surrogate function across domain
# 	Xsamples = asarray(arange(0, 1, 0.001))
# 	Xsamples = Xsamples.reshape(len(Xsamples), 1)
# 	ysamples, _ = surrogate(model, Xsamples)
# 	pyplot.plot(Xsamples, ysamples)
# 	# show the plot
# 	pyplot.show()



# sample the domain sparsely with noise
# X = random(100)
X = np.random.uniform(low=bounds[:, 0], high=bounds[:, 1], size=(20, 6))
print(X)

y = np.random.uniform(6, 600, size=X.shape[0])  # Generate one value per row in X
print(y)
# y = asarray([objective(x) for x in X])
# reshape into rows and cols
# X = X.reshape(len(X), 1)
# y = y.reshape(len(y), 1)
# define the model
# 定义核函数
kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2))
# 创建高斯过程回归模型
model = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
# model = GaussianProcessRegressor()
# fit the model
model.fit(X, y)
# plot before hand
# plot(X, y, model)



# perform the optimization process
for i in range(10):
	# select the next point to sample
	x = opt_acquisition(X, y, model)
	# sample the point
	actual = objective(x)
	# summarize the finding
	est, _ = surrogate(model, [[x]])
	print('>x=%.3f, f()=%3f, actual=%.3f' % (x, est, actual))
	# add the data to the dataset
	X = vstack((X, [[x]]))
	y = vstack((y, [[actual]]))
	# update the model
	model.fit(X, y)

# plot all samples and the final surrogate function
# plot(X, y, model)
# best result
ix = argmax(y)
print('Best Result: x=%.3f, y=%.3f' % (X[ix], y[ix]))


print("count 的值:", count)