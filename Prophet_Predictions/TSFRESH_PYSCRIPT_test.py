import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

def fetch_stock_data(symbol):
    # Fetch stock data for the given symbol
    stock = yf.Ticker(symbol)
    
    # Get historical data for the previous 5 years
    stock_data = stock.history(period="5y")
    
    return stock_data

def preprocess_stock_data(stock_data):
    # Calculate the daily percentage change
    stock_data['Daily_Return_Percentage'] = stock_data['Close'].pct_change() * 100
    
    return stock_data

def train_linear_regression_model(data):
    # Drop any rows with missing values
    data.dropna(inplace=True)
    
    # Separate features (X) and target variable (y)
    X = data[['Open', 'High', 'Low', 'Volume']].values
    y = data['Daily_Return_Percentage'].values
    
    # Create a linear regression model
    model = LinearRegression()
    
    # Fit the model
    model.fit(X, y)
    
    return model

def main():
    # Get the stock symbol from user input
    stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")
    
    # Fetch stock data
    stock_data = fetch_stock_data(stock_symbol)
    
    if not stock_data.empty:
        # Preprocess stock data
        processed_stock_data = preprocess_stock_data(stock_data)
        
        # Train linear regression model
        model = train_linear_regression_model(processed_stock_data)
        
        # Predict next 30 days of 'Daily_Return_Percentage'
        last_30_days = processed_stock_data.iloc[-30:]
        X_next_30_days = last_30_days[['Open', 'High', 'Low', 'Volume']].values
        predicted_returns = model.predict(X_next_30_days)
        
        # Calculate R-squared score
        y_true = last_30_days['Daily_Return_Percentage'].values
        r2 = r2_score(y_true, predicted_returns)
        
        # Calculate RMSE
        rmse = np.sqrt(mean_squared_error(y_true, predicted_returns))
        
        # Calculate MAE
        mae = mean_absolute_error(y_true, predicted_returns)
        
        # Save metrics to a text file
        with open(f'{stock_symbol}_metrics.txt', 'w') as file:
            file.write(f'R-squared: {r2}\n')
            file.write(f'RMSE: {rmse}\n')
            file.write(f'MAE: {mae}\n')
        
        # Create a DataFrame with predictions
        predictions_df = pd.DataFrame({'Predicted_Returns': predicted_returns})
        
        # Save predictions to CSV
        predictions_df.to_csv(f'{stock_symbol}_predictions.csv', index=False)
        
        print("Predicted returns for the next 30 days saved to CSV.")
        print("Metrics saved to text file.")
        print(predictions_df)
    else:
        print("Error: Failed to fetch stock data. Please check the stock symbol.")

if __name__ == "__main__":
    main()
