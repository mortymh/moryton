#03_linear_regression
from sklearn.linear_model import LinearRegression

# ساخت مدل رگرسیون
model = LinearRegression()

# آموزش مدل
model.fit(X_train, y_train)

# پیش‌بینی روی داده‌های تست
y_pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# خطاهای پیش‌بینی
mse = mean_squared_error(y_test, y_pred)      # میانگین مربع خطا
mae = mean_absolute_error(y_test, y_pred)     # میانگین قدر مطلق خطا
r2 = r2_score(y_test, y_pred)                  # ضریب تعیین (چقدر مدل خوب داده‌ها رو توضیح میده)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared (R2): {r2:.2f}")

