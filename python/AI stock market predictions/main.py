import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as ppl
#reading data
data = pd.read_csv('SPY.csv')
#spliting data to train and test dataset
train_data = data.iloc[:int(.99*len(data)), :]
test_data = data.iloc[int(.99*len(data)):, :]
#def of features and target variable
features = ['Open', 'Volume']
target = 'Close'
#model itself
model = xgb.XGBRegressor()
model.fit(train_data[features], train_data[target])
#Makeing predictions 
predictions = model.predict(test_data[features])
print('Model Predictions:')
print(predictions)
#Actual Values
print('Actual values:')
print(test_data[target])
#testing accuracy 
accuracy = model.score(test_data[features], test_data[target])
print('Accuracy:')
print(accuracy)
#plot predictions and close price
ppl.plot(data['Close'], label = 'Close Price')
ppl.plot(test_data[target].index, predictions, label = 'Prediction Price')
ppl.legend()
ppl.show()