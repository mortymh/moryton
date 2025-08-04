#04_model_improvement
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# مدل Ridge Regression
ridge = Ridge(alpha=1.0)  # alpha میزان قدرت منظم‌سازی را کنترل می‌کند
ridge.fit(X_train, y_train)  # آموزش مدل روی داده‌های آموزش

y_pred_ridge = ridge.predict(X_test)  # پیش‌بینی روی داده‌های تست

# ارزیابی مدل Ridge
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)

print("Ridge Regression:")
print(f"Mean Squared Error: {mse_ridge:.2f}")
print(f"R2 Score: {r2_ridge:.2f}")

# مدل Lasso Regression
lasso = Lasso(alpha=0.1)  # alpha کمتر، منظم‌سازی ملایم‌تر
lasso.fit(X_train, y_train)  # آموزش مدل

y_pred_lasso = lasso.predict(X_test)  # پیش‌بینی روی داده‌های تست

# ارزیابی مدل Lasso
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)

print("\nLasso Regression:")
print(f"Mean Squared Error: {mse_lasso:.2f}")
print(f"R2 Score: {r2_lasso:.2f}")

