import numpy as np 
from scipy.stats import norm 


def European_options_pricer(S, K, T, t, r, vol):
    "T can be an array"
    expiry = T-t 
    d1_denom = vol * np.sqrt(expiry)
    d1_num = np.log(S/K) + (r + 0.5 * vol**2 * expiry)
    d1 = d1_num/d1_denom
    d2 = d1 - vol * np.sqrt(expiry)
    
    #call and put price
    c = S * norm.cdf(d1) - K*np.exp(-r * expiry)*norm.cdf(d2)
    p = K * np.exp(-r * expiry) * norm.cdf(-d2) - S*norm.cdf(-d1)

    return c, p

