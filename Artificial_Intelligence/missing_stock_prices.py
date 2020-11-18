# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import pandas as pd
# from sklearn.linear_model import LinearRegression
from scipy.interpolate import UnivariateSpline


n = int(input())
prices = []
# reading in data
for _ in range(n):
    date, price = input().split('\t')
    prices.append(price)

x = []  # indices of valid prices
x_miss = []  # indices of missing data

y = []  # valid prices
for i in range(n):
    if 'Missing' in prices[i]:
        x_miss.append(i)
    else:
        x.append(i)
        y.append(prices[i])

spline = UnivariateSpline(np.array(x), np.array(y))
for i in x_miss:
    print(spline(i))
