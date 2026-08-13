import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error


df = pd.read_csv("/ride_fare_trip_delay_dataset - ride_fare_trip_delay_dataset.csv")


X = df[["Distance_KM", "Driver_Experience_Yrs",
        "Traffic_Score", "Passenger_Count"]]

y = df["Is_Delayed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = LogisticRegression()
model.fit(X_train, y_train)

result = model.predict(X_test)

print("Trip Delay Prediction")
print("Accuracy:", accuracy_score(y_test, result))

y = df["Fare_INR"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = LinearRegression()
model.fit(X_train, y_train)

result = model.predict(X_test)

print("Fare Prediction")
print("Mean Squared Error:", mean_squared_error(y_test, result))
