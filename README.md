
🗂 Project Structure
bash
Copy
Edit
Oil-Price-Forecasting/
│
├── data/
│   └── oil_prices.csv           # Daily crude oil prices (May 1987 – April 2025)
│
├── notebooks/
│   └── analysis.ipynb           # Main notebook with EDA, ARIMA, and Prophet models
│
├── outputs/
│   └── oil_prices_trend.png     # Line plot of crude oil price over time
│
├── venv/                        # Python virtual environment (optional)
│
└── README.md                    # Project overview and instructions
📊 Dataset
Source: Daily historical crude oil prices.

Range: May 1987 to April 2025

Format: CSV

Columns:

Date: Daily timestamps

Price: Crude oil price in USD per barrel

🔍 Notebook Overview (notebooks/analysis.ipynb)
📥 Data Preparation

Load oil_prices.csv

Drop missing values

Parse Date column and set it as index

📈 Exploratory Data Analysis (EDA)

Visualize historical oil prices

Save oil_prices_trend.png to outputs/ folder

🤖 Time Series Modeling

Split data into training (80%) and testing (20%) sets

Fit two forecasting models:

ARIMA (AutoRegressive Integrated Moving Average)

Prophet (Facebook’s time series forecasting model)

📊 Model Evaluation

Compare ARIMA vs Prophet forecast accuracy using RMSE (Root Mean Squared Error)

Visual comparison of actual vs predicted values

Visualize performance of both models on the test set

🧰 Dependencies
To reproduce the notebook, install the required libraries:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels prophet tensorflow streamlit plotly joblib dill
🛠️ How to Run This Project
Clone or download the repository.

(Optional) Set up a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
Install dependencies.

Open the notebook:

bash
Copy
Edit
jupyter notebook notebooks/analysis.ipynb
📌 Key Insights
Prophet slightly outperforms ARIMA in capturing long-term trends.

Sharp oil price drops are visible around 2008 and 2020, corresponding to global crises.

The model provides short-term forecasting capability based on historical trends.
