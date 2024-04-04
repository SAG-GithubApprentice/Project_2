# Tech Stock Performance Prediction Project

## Overview

The Tech Stock Performance Prediction Project is at the forefront of financial technology, applying advanced machine learning techniques to forecast the performance of key semiconductor stocks: AMD, Intel, and Nvidia. By comparing these forecasts with the performance of the semiconductor ETF, SOXX, we aim to uncover actionable insights into the semiconductor industry's future trends and provide precise market forecasts. This project, spearheaded by Sergio Garzon, Chris Alvarez, and Todd Snyder, combines in-depth feature extraction with state-of-the-art predictive models within a compressed timeline supported by edX.

## Directory

- .DS_Store
- Portfolio_Predictions/.DS_Store
- Portfolio_Predictions/Portfolio_PyScript.py
- Portfolio_Predictions/Portfolio_X.ipynb
- Portfolio_Predictions/Portfolio_XX.ipynb
- Portfolio_Predictions/Portfolio_XXX.ipynb
- Portfolio_Predictions/Portfolio_Y.ipynb
- Portfolio_Predictions/Portfolio_Y_SOXX.ipynb
- Prophet_Predictions/PROPHET_PORTFOLIO.csv
- Prophet_Predictions/Portfolio_C.ipynb
- Prophet_Predictions/SIMP+EXTRACT_RF.txt
- Prophet_Predictions/SIMP_EXTRACT_LR.csv
- Prophet_Predictions/SIMP_EXTRACT_LR.txt
- Prophet_Predictions/SIMP_EXTRACT_RF.csv
- Prophet_Predictions/TSFRESH_GB.csv
- Prophet_Predictions/TSFRESH_RF.csv
- Prophet_Predictions/TSFRESH_RF.txt
- Prophet_Predictions/TSRESH_GB.txt
- Prophet_Predictions/combined_SOXX_predictions_A.csv
- Prophet_Predictions/combined_predictions_SOXX.csv
- Prophet_Predictions/portfolio_daily_return_pct.jpeg
- Prophet_Predictions/portfolio_unit_price.jpeg
- README.md

## Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- An environment that supports Jupyter Notebooks (e.g., JupyterLab, VSCode)

## Required Python Libraries

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

## Setup

1. Clone the project repository:
2. Navigate to the project directory:
3. Install the required Python packages:

## Data Collection

Historical stock price data for Intel, Nvidia, and AMD, alongside the SOXX ETF, were sourced through API requests using `yfinance`. The dataset includes over 1,000 records for each entity, ensuring a comprehensive analysis.

# Technologies Used

- **Python**: Serves as the primary programming language.
- **Pandas**: Utilized for data manipulation and cleaning.
- **Matplotlib/Pandas Plotting**: Employed for generating data visualizations.
- **Scikit-learn**: Applied for implementing and evaluating machine learning models.
- **API Requests (`yfinance`)**: Used to fetch historical stock data.

## Feature Engineering

To enhance the predictive power of our models, we employed the tsfresh library to extract relevant time series features from the raw data. These features capture intrinsic patterns and characteristics, enabling our models to learn and generalize more effectively.

## Model Development

The project employs supervised machine learning models, focusing on time series forecasting techniques suitable for predicting stock prices. Models explored include linear regression, decision trees, random forests, and LSTM networks, with evaluations based on MAE, RMSE, and R-squared metrics.

- **Linear Regression**: A baseline model for establishing performance benchmarks.
- **Decision Trees**: Capable of capturing complex, non-linear relationships in the data.
- **Random Forests**: Ensemble learning technique that combines multiple decision trees for improved accuracy and robustness.
- **Long Short-Term Memory (LSTM) Networks**: Recurrent neural networks adept at modeling sequential data and capturing long-term dependencies.

Model evaluation is based on industry-standard metrics, including Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared, ensuring a comprehensive assessment of predictive performance.

## Usage

To reproduce the analysis and predictions, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment (recommended for isolated dependencies).
3. Install the required Python packages listed in the requirements.txt file.
4. Launch Jupyter Notebook and open the main analysis notebook.
5. Run the notebook cells sequentially to execute the data collection, preprocessing, feature engineering, model training, and prediction steps.


## Visualizations

The graphs elucidate stock trends, model accuracy, and predictions and visually represent our analysis and findings.

![image](https://github.com/SAG-GithubApprentice/Project_2/assets/151570128/bb7dc682-5ecc-4fa2-a8c0-9a56badfd8bf)

![image](https://github.com/SAG-GithubApprentice/Project_2/assets/151570128/89020021-9854-434f-9454-b70f5b2c5087)

![image](https://github.com/SAG-GithubApprentice/Project_2/assets/151570128/3be3ec8b-b9ef-4f95-972f-6b8091ba5a27)

![image](https://github.com/SAG-GithubApprentice/Project_2/assets/151570128/cbfd8382-1570-4476-b247-48e8b8367866)

## Presentation Slides

https://www.canva.com/design/DAGBBX-OPKg/uRusxwQLk6WDPb-NisJX8g/edit?utm_content=DAGBBX-OPKg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Contributions

- edX Boot Camps LLC.
- Copilot
- ChatGPT
- Perplexity Labs
- We welcome contributions from the community to further enhance the project's capabilities and explore new avenues for stock performance prediction. Please submit pull requests or open issues on the project's GitHub repository

## Authors

- Sergio Garzon: Feature/data engineering, model evaluation, and visualization.
- Chris Alvarez: Data engineering, model evaluation, and model development
- Todd Snyder: Project lead, Data collection, preprocessing, and documentation

## License

This project is available for educational and non-commercial use only. It is not licensed for other purposes.


