import numpy as np 
from scipy.stats import norm 
from scipy.optimize import brentq

def cast_array(K, T):
    n_T = len(T)
    n_K = len(K)
    K_new = np.tile(K, n_T)
    T_new = np.repeat(T, n_K)

    return K_new, T_new

def European_options_pricer(S, K, T, r, vol, t=0):
    "cast S and T using cast_arrays first if you want to create prices at varying K and T"
    expiry = T-t 
    d1_denom = vol * np.sqrt(expiry)
    d1_num = np.log(S/K) + (r + 0.5 * vol**2)* expiry
    d1 = d1_num/d1_denom
    d2 = d1 - vol * np.sqrt(expiry)
    return d1, d2

def European_call_price(S, K, T, r, vol, t=0):
    expiry = T-t
    d1, d2 = European_options_pricer(S, K, T, r, vol, t)
    return S * norm.cdf(d1) - K*np.exp(-r * expiry)*norm.cdf(d2)

def European_put_price(S, K, T, r, vol, t=0):
    expiry = T-t
    d1, d2 = European_options_pricer(S, K, T, r, vol, t)
    return K * np.exp(-r * expiry) * norm.cdf(-d2) - S*norm.cdf(-d1)

def implied_vol(S, K, T, r, vol, C_market t=0):
    # Function whose root is the implied volatility
    def f(vol, S, K, T, r, C_market, t=0):
        return European_call_price(S, K, T, r, vol, t) - C_market
    
    # Brent's method to find implied volatility
    IV_list = []
    for i in range(len(C_market)):
        K_i, T_i, C_market_i = K[i], T[i], C_market[i]
        iv = brentq(f, 0.001, 3, args=(S, K_i, T_i, r, C_market_i))
        IV_list.append(iv)
    
    return IV_list





