from sklearn.linear_model import LinearRegression

x = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
]

y = [10, 15, 20, 25, 30]

model = LinearRegression()

model.fit(x, y)

prediction = model.predict([[6, 7]])

print("Prediction:", prediction[0])
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
