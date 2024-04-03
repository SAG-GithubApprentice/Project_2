# This script utilizes historical stock data fetched from Yahoo Finance using the yfinance library 
# to predict the daily returns of a given stock for the next 30 days. It preprocesses the data by 
# calculating daily return percentages, creating lagged features, and computing rolling statistics. 
# Then, it trains a linear regression model using 80% of the data and evaluates its performance on 
# the remaining 20%. Next, it predicts the daily returns for the next 30 days based on the last 30 
# rows of the data, calculates evaluation metrics (R-squared, RMSE, MAE), and saves both the metrics 
# and the predictions to separate files. Finally, it prints out the metrics and the predicted returns 
# for verification and analysis.

import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        stock_data = stock.history(period="5y")
        return stock_data
    except Exception as e:
        print("Error fetching stock data:", e)
        return None

def preprocess_stock_data(stock_data):
    stock_data['Daily_Return_Percentage'] = stock_data['Close'].pct_change() * 100
    stock_data['Previous_Return'] = stock_data['Daily_Return_Percentage'].shift(1)
    stock_data['Rolling_Mean'] = stock_data['Daily_Return_Percentage'].rolling(window=7).mean()
    stock_data['Rolling_Std'] = stock_data['Daily_Return_Percentage'].rolling(window=7).std()
    stock_data.dropna(inplace=True)
    return stock_data

def train_linear_regression_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(y_true, predicted_returns):
    r2 = r2_score(y_true, predicted_returns)
    rmse = np.sqrt(mean_squared_error(y_true, predicted_returns))
    mae = mean_absolute_error(y_true, predicted_returns)
    return r2, rmse, mae

def main():
    stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")
    stock_data = fetch_stock_data(stock_symbol)
    
    if stock_data is not None and not stock_data.empty:
        processed_stock_data = preprocess_stock_data(stock_data)
        
        X = processed_stock_data[['Previous_Return', 'Rolling_Mean', 'Rolling_Std']]
        y = processed_stock_data['Daily_Return_Percentage']
        
        # Split data into training and testing sets
        length_of_dataset = processed_stock_data.shape[0]
        X_train = X.iloc[:int(length_of_dataset * 0.8)]
        y_train = y.iloc[:int(length_of_dataset * 0.8)]
        
        model = train_linear_regression_model(X_train, y_train)
        
        last_30_days = processed_stock_data.tail(30)
        X_next_30_days = last_30_days[['Previous_Return', 'Rolling_Mean', 'Rolling_Std']]
        
        predicted_returns = model.predict(X_next_30_days)
        
        # Calculate metrics
        y_true = last_30_days['Daily_Return_Percentage']
        r2, rmse, mae = evaluate_model(y_true, predicted_returns)
        
        # Save metrics to a text file
        with open(f'{stock_symbol}_metrics.txt', 'w') as file:
            file.write(f'R-squared: {r2}\n')
            file.write(f'RMSE: {rmse}\n')
            file.write(f'MAE: {mae}\n')
        
        # Save predictions to CSV
        predictions_df = pd.DataFrame({'Actual_Returns': y_true, 'Predicted_Returns': predicted_returns})
        predictions_df.to_csv(f'{stock_symbol}_predictions.csv', index=False)
        
        print("Predicted returns for the next 30 days saved to CSV.")
        print("Metrics saved to text file.")
        print("R-squared:", r2)
        print("RMSE:", rmse)
        print("MAE:", mae)
        print(predictions_df)
    else:
        print("Error: Failed to fetch stock data or empty data returned. Please check the stock symbol.")

if __name__ == "__main__":
    main()
