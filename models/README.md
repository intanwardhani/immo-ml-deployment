# Overview
Below you can see a summary of the available models. Indeed, the models don't seem to perform well. It is because I haven't done feature engineering, feature selection, and hyperparameter tuning. For this deployment, I use XGBoost model.

# Currentt performance of the available models
| Model        | RMSE (Train) | R² (Train) | RMSE (Test) | R² (Test) | Overfitting? | Notes                              |
| ------------ | ------------ | ---------- | ----------- | --------- | ------------ | ---------------------------------- |
| Ridge        | 158,390      | 0.66       | 168,892     | 0.65      | Low          | Stable, moderate accuracy          |
| RandomForest | 68,240       | 0.94       | 185,850     | 0.58      | High         | Overfits badly, tune needed        |
| XGBoost      | 97,071       | 0.87       | 175,518     | 0.62      | Moderate     | Good compromise, slightly overfits |
