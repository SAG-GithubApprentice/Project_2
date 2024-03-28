# Tech Stock Performance Prediction Project

## Overview

This project aims to predict the future performance of key semiconductor stocks - AMD, Intel, and Nvidia - and compare these predictions against the performance of the semiconductor ETF, SOXX. Our team, consisting of Sergio Garzon, Chris Alvarez, and Todd Snyder, leverages machine learning and feature extraction techniques to provide accurate forecasts and insightful analysis within a condensed timeframe. This endeavor is supported by edX Boot Camps LLC as our educational partner.

## Table of Contents

- [Installation](#installation)
- [Project Setup](#project-setup)
- [Data Collection](#data-collection)
- [Technologies Used](#technologies-used)
- [Model Development](#model-development)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip
- An environment that supports Jupyter Notebooks (e.g., JupyterLab, VSCode)

### Required Python Libraries

- `pandas`: For data manipulation and analysis.
- `hvplot`: For creating interactive plots.
- `prophet`: For time series forecasting.
- `yfinance`: For downloading historical market data.
- `matplotlib.pyplot`: For creating visualizations, graphs, and charts.
- `datetime`: For dtae and time manipulation.

### Setup

1. Clone the project repository:
2. Navigate to the project directory:
3. Install the required Python packages:

## Project Setup

This section details the project's structure and navigation.

- `data/`: Contains the raw and processed datasets for AMD, Intel, Nvidia, and SOXX.
- `Prophet_Predictions/`: Houses the trained machine learning models.
- `notebooks/`: Jupyter notebooks for exploratory data analysis, model training, and evaluation.
- `src/`: Source code for data collection, preprocessing, and model evaluation.
- `visualizations/`: Generated graphs and plots illustrating stock trends and model predictions.

## Data Collection

Historical stock price data for Intel, Nvidia, and AMD, alongside the SOXX ETF, were sourced through API requests using `yfinance`. The dataset includes over 1,000 records for each entity, ensuring a comprehensive analysis.

## Technologies Used

- **Python**: Serves as the primary programming language.
- **Pandas**: Utilized for data manipulation and cleaning.
- **Matplotlib/Pandas Plotting**: Employed for generating data visualizations.
- **Scikit-learn**: Applied for implementing and evaluating machine learning models.
- **API Requests (`yfinance`)**: Used to fetch historical stock data.

## Model Development

The project employs supervised machine learning models, focusing on time series forecasting techniques suitable for predicting stock prices. Models explored include linear regression, decision trees, random forests, and LSTM networks, with evaluations based on metrics such as MAE, RMSE, and R-squared.

## Usage

A step-by-step guide to running the project, from fetching historical data to forecasting future prices using `prophet`, is documented within the `notebooks/` directory.

## Visualizations

The `visualizations/` folder includes interactive charts and graphs that elucidate stock trends, model accuracy, and predictions, providing a visual representation of our analysis and findings.

## Contributing

We welcome contributions! If you have suggestions or improvements, please fork the repository and submit a pull request.

## Authors

- Sergio Garzon
- Chris Alvarez
- Todd Snyder

Supported by edX Boot Camps LLC.

## License

This project is available for educational and non-commercial use only. It is not licensed for other purposes.


