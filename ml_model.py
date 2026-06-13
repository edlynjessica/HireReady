import pandas as pd

from sklearn.model_selection import train_test_split
# for splitting the dataset into training and testing sets
from sklearn.ensemble import RandomForestRegressor # ML Model
from sklearn.metrics import mean_absolute_error # for evaluating the model
import pickle

df=pd.read_csv("synthetic_students.csv")

# X -> features (inputs)
X = df[[
    "cgpa",
    "lc_easy",
    "lc_medium",
    "lc_hard",
    "contest_rating",
    "projects",
    "internships",
    "communication"
]]

# y -> target (output)
y = df["hire_ready_score"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# 80% training data, 20% testing data

model = RandomForestRegressor(random_state=42)

# train the model on the training data
model.fit(X_train,y_train)

# test the model on the testing data
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}") # smaller the better

pickle.dump(model,open("model.pkl","wb")) # save the trained model to a file

print("Model trained and saved successfully!")