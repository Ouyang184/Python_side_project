import yfinance as yf
import matplotlib.pyplot as plt
import sklearn 
import pandas as pd

Home_Depot = yf.Ticker("HD")
Home_Depot = Home_Depot.history(period = "max")
print(Home_Depot)

Home_Depot.index
Home_Depot.plot.line(y = "Close", use_index = True)

del Home_Depot["Dividends"]
del Home_Depot["Stock Splits"]

Home_Depot["Tomorrow"] = Home_Depot["Close"].shift(-1)
Home_Depot["Target"] = (Home_Depot["Tomorrow"] > Home_Depot["Close"]).astype(int)

Home_Depot = Home_Depot.loc["1990-01-01":].copy()

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators= 100, min_samples_split=100, random_state=1)

train = Home_Depot.iloc[:-100]
test = Home_Depot.iloc[-100:]

predictors = ["Close", "Volume", "Open", "High", "Low"]
model.fit(train[predictors], train["Target"])

from sklearn.metrics import precision_score
preds = model.predict(test[predictors])
preds = pd.Series(preds, index=test.index, name="Predictions")

precision_score(test["Target"], preds)

combined = pd.concat([test["Target"], preds], axis = 1)
combined.plot()

def predict(train, test, predictors, model):
    model.fit(train[predictors], train["Target"])
    preds = model.predict(test[predictors])
    preds = pd.Series(preds, index= test.index, name = "Predictions")
    combined = pd.concat([test["Target"], preds], axis=1)
    return combined

def backtest(data, model, predictors, start = 2500, step = 250):
    all_predictions = []
    
    for i in range(start, data.shape[0], step):
        train = data.iloc[0:i].copy()
        test = data.iloc[i:(i + step)].copy()
        predictions = predict(train, test, predictors, model)
        all_predictions.append(predictions)
    return pd.concat(all_predictions)

predictions = backtest(Home_Depot, model, predictors)

predictions["Predictions"].value_counts()

precision_score(predictions["Target"], predictions["Predictions"])

predictions["Target"].value_counts()/predictions.shape[0]

horizons = [2,5,60,250,1000]
new_predictors = []

for horizon in horizons:
    rolling_averages = Home_Depot.rolling(horizon).mean()

    ration_column = f"Close_Ratio_{horizon}"
    Home_Depot[ration_column] = Home_Depot["Close"]/ rolling_averages["Close"]

    trend_column = f"Trend_{horizon}"
    Home_Depot[trend_column] = Home_Depot["Target"].shift(1).rolling(horizon).sum()


    new_predictors += [ration_column, trend_column]

Home_Depot = Home_Depot.dropna()
Home_Depot

model = RandomForestClassifier(n_estimators=200, min_samples_split= 50, random_state=1)

def predict(train, test, predictors, model):
    model.fit(train[predictors], train["Target"])
    preds = model.predict_proba(test[predictors])[:,1]
    preds[preds >= .6] = 1
    preds[preds < .6] = 0
    preds = pd.Series(preds, index= test.index, name = "Predictions")
    combined = pd.concat([test["Target"], preds], axis=1)
    return combined

predictions = backtest(Home_Depot, model, new_predictors)
predictions["Predictions"].value_counts()

precision_score(predictions["Target"], predictions["Predictios"])
