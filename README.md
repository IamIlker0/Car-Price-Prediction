# Car Price Prediction Using Machine Learning

## Project Goal

The objective of this project is to predict the dependent variable, **Price**, as accurately as possible using the most effective machine learning methods. To achieve this, the process includes:

- Data preprocessing
- Data visualization
- Exploratory data analysis (EDA)
- Statistical exploration
- Data cleaning
- Model selection and evaluation

## Dataset

This project uses the **Car Price Prediction Dataset** from Kaggle: [Dataset Link](https://www.kaggle.com/datasets/asinow/car-price-dataset/data)

The dataset contains **10,000 entries**, with each row representing a car and its attributes. Below are the key features:

- **Brand**: Car brand (e.g., Toyota, BMW, Ford)
- **Model**: Car model (e.g., Corolla, Focus, X5)
- **Year**: Production year of the car
- **Engine\_Size**: Engine capacity in liters
- **Fuel\_Type**: Fuel category (Petrol, Diesel, Hybrid, Electric)
- **Transmission**: Type of transmission (Manual, Automatic, Semi-Automatic)
- **Mileage**: Total distance traveled in kilometers
- **Doors**: Number of doors
- **Owner\_Count**: Number of previous owners
- **Price**: Estimated selling price of the car (target variable)

## Installation

To set up and run this project, install the necessary dependencies using the following commands:

```bash
# Create a virtual environment (optional but recommended)
python -m venv env
source env/bin/activate  # On Windows, use 'env\\Scripts\\activate'

# Install required Python libraries
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

## Exploratory Data Analysis (EDA)

### Data Loading and Initial Exploration

- The dataset was loaded using `pandas` and explored for structure and consistency.
- It contains **10,000 entries** with essential features like `Brand`, `Model`, `Year`, `Engine_Size`, `Mileage`, and `Price`.
- **No missing values** were found in the dataset.

### Data Cleaning and Preprocessing

- **Outliers**: The `Price` column contained outliers, identified using the **Interquartile Range (IQR) method** and removed for better model stability.
- **Categorical Encoding**: Features like `Fuel_Type` and `Transmission` were **one-hot encoded** for model compatibility.
- **Feature Engineering**:
  - `Age`: Computed as `2025 - Year`, representing the car's age.
  - `Mileage_per_Age`: Defined as `Mileage / Age`, indicating the average mileage per year.
- **Feature Scaling**: `StandardScaler` was applied to numerical features for uniform scaling.

## Model Selection and Evaluation

Multiple models were tested, including **Linear Regression, Ridge Regression, and Lasso Regression**. After hyperparameter tuning with **GridSearchCV**, the best-performing model was **Ridge Regression** with an **R² score of 94.47%**.

### Challenges and Solutions

1. **Feature Selection**: Used **Recursive Feature Elimination (RFE)** and **Lasso Regression** to identify the most relevant features.
2. **Outlier Handling**: The **IQR method** was applied to remove extreme values affecting model accuracy.
3. **Hyperparameter Tuning**: **GridSearchCV** was used to find optimal parameters for regularized models.
4. **Model Interpretability**: **SHAP values** were used to understand feature importance.

### Best Model Performance

- **Algorithm**: Ridge Regression
- **R² Score**: 94.47%
- **Selected Features**: `Year`, `Engine_Size`, `Mileage`, `Fuel_Type_Electric`, `Transmission_Manual`

### Visualization of Results

1. **Actual vs. Predicted Prices**: Strong linear correlation between actual and predicted values.
2. **Residual Error Distribution**: Symmetric distribution, indicating unbiased predictions.

## Usage

This model can be used for:

- **Car dealerships** to estimate fair selling prices
- **Buyers & sellers** to evaluate car pricing
- **Insurance companies** to assess vehicle values

## Contributing

Contributions are welcome! If you'd like to improve the model, feel free to:

- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Commit changes and push (`git push origin feature-branch`)
- Submit a pull request

## License

The dataset specifies **Other (specified in description)** as its license. Ensure compliance with Kaggle's terms before commercial use.

