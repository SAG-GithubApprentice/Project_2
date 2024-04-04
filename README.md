# Tech Stock Performance Prediction Project

## Overview

The Tech Stock Performance Prediction Project is at the forefront of financial technology, applying advanced machine learning techniques to forecast the performance of key semiconductor stocks: AMD, Intel, and Nvidia. By comparing these forecasts with the performance of the semiconductor ETF, SOXX, we aim to uncover actionable insights into the semiconductor industry's future trends. This project, spearheaded by Sergio Garzon, Chris Alvarez, and Todd Snyder, combines in-depth feature extraction with state-of-the-art predictive models within a compressed timeline, supported by edX and IBM's digital learning platforms.

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- An environment that supports Jupyter Notebooks (e.g., JupyterLab, VSCode)

### Required Python Libraries

- `pandas`: for data manipulation and analysis.
- `yfinance`: for fetching historical market data from Yahoo Finance.
- `pandas_market_calendars`: for handling market calendars.
- `matplotlib`: for plotting and visualization.
- `tsfresh`: for extracting time series features.
- `sklearn` (`sklearn.linear_model`, `sklearn.metrics`, `sklearn.ensemble`, `sklearn.model_selection`): for various machine learning tasks such as linear regression, random forest regression, model evaluation, and splitting datasets.
- `numpy`: for numerical computing.
- `prophet`: for time series forecasting.

## Installation

Install the required dependencies:

\`\`\`bash
pip install -r requirements.txt
\`\`\`Clone the repository and navigate into it:

\`\`\`bash
git clone <repository-url>
cd <repository-name>
\`\`\`

Create and activate a virtual environment:

- **Unix/macOS**:

  \`\`\`bash
  python3 -m venv env
  source env/bin/activate
  \`\`\`

- **Windows**:

  \`\`\`bash
  python -m venv env
  .\env\Scripts\activate

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

To run the project, follow these steps:

1. Launch Jupyter Notebook:

\`\`\`bash
jupyter notebook
\`\`\`

2. Navigate to the project directory and open the main notebook.

3. Run the notebook cells sequentially to perform the analysis and view the predictions.


## Visualizations

The `visualizations/` folder includes interactive charts and graphs that elucidate stock trends, model accuracy, and predictions, providing a visual representation of our analysis and findings.

## Contributions

- edX Boot Camps LLC.
- Copilot
- ChatGPT
- We welcome contributions! If you have suggestions or improvements, please fork the repository and submit a pull request.

## Authors

- Sergio Garzon
- Chris Alvarez
- Todd Snyder

## License

This project is available for educational and non-commercial use only. It is not licensed for other purposes.


