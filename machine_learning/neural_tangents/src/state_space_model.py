import numpy as np
import matplotlib
import matplotlib.pylab as plt
 
y = np.cumsum(np.random.normal(size=100))
plt.plot(y)
plt.show()

import statsmodels.api as sm

model = sm.tsa.UnobservedComponents(y, 'local level')
result = model.fit()
result.plot_components()
plt.show()

import pystan
 
model = """
    data {
        int n; # サンプルサイズ
        vector[n] y; # 時系列の値
    }
    parameters {
        real muZero; # 左端
        vector[n] mu; # 確率的レベル
        real<lower=0> sigmaV; # 観測誤差の大きさ
        real<lower=0> sigmaW; # 過程誤差の大きさ
    }
    model {
        # 状態方程式
        mu[1] ~ normal(muZero, sqrt(sigmaW));
        for(i in 2:n) {
            mu[i] ~ normal(mu[i-1], sqrt(sigmaW));
        }
        
        # 観測方程式
        for(i in 1:n) {
            y[i] ~ normal(mu[i], sqrt(sigmaV));
        }
    }
"""
fit = pystan.stan(model_code=model, data={'n': 100, 'y': y}, iter=1000, chains=1)
fit

la = fit.extract()
 
pred = la['mu'].mean(axis=0)
mu_lower, mu_upper = np.percentile(la['mu'], q=[2.5, 97.5], axis=0)
 
plt.plot(list(range(len(y)+1)), list(y)+[None], color='black')
plt.plot(list(range(1, len(y)+1)), pred)
plt.fill_between(list(range(1, len(y)+1)), mu_lower, mu_upper, alpha=0.3)
plt.show()


import pymc as pm
N = len(y)
T = 1000
 
with pm.Model() as model:
    
    muZero = pm.Normal(name='muZero', mu=0.0, tau=1.0)
    sigmaW = pm.InverseGamma(name='sigmaW', alpha=1.0, beta=1.0)
    
    mu = [0]*N
    mu[0] = pm.Normal(name='mu0', mu=muZero, tau=1/sigmaW)
    for n in range(1, N):
        mu[n] = pm.Normal(name='mu'+str(n), mu=mu[n-1], tau=1/sigmaW)
    
    sigmaV = pm.InverseGamma(name='sigmaV', alpha=1.0, beta=1.0)
    y_pre = pm.Normal('y_pre', mu=mu, tau=1/sigmaV, observed=y)
    
    start = pm.find_MAP()
    step = pm.NUTS()
    trace = pm.sample(T, step, start=start)

mu_samples = np.array([trace['mu'+str(i)] for i in range(N)])
pred = mu_samples.mean(axis=1)
mu_lower, mu_upper = np.percentile(mu_samples, q=[2.5, 97.5], axis=1)
 
plt.plot(list(range(len(y)+1)), list(y)+[None], color='black')
plt.plot(list(range(1, len(y)+1)), pred)
plt.fill_between(list(range(1, len(y)+1)), mu_lower, mu_upper, alpha=0.3)
plt.show()
