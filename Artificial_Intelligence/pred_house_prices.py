# HackerRank AI
# Intro to Statistics
# Day 6: Multiple Linear Regression
# Problem code: https://www.hackerrank.com/contests/intro-to-statistics/challenges/predicting-house-prices/problem

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

F, N = map(int, input().split())
X = []
y = []
for _ in range(N):
    a = list(map(float, input().split()))
    X.append(a[:F])
    y.append(a[F])

T = int(input())
o = []
for _ in range(T):
    o.append(list(map(float, input().split())))

model = LinearRegression()
model.fit(X, y)
pred = model.predict(o)
for i in range(T):
    print(pred[i])
