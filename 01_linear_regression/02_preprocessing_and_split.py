#02_preprocessing_and_split

from sklearn.preprocessing import LabelEncoder

# پر کردن مقادیر گمشده با میانگین همون ستون
df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].mean())


# ساخت encoder
encoder = LabelEncoder()

# تبدیل ستون متنی به عددی
df['ocean_proximity'] = encoder.fit_transform(df['ocean_proximity'])

from sklearn.preprocessing import StandardScaler

# جدا کردن ستون target (یعنی اون چیزی که می‌خوایم پیش‌بینی کنیم)
features = df.drop('median_house_value', axis=1)

# نرمال‌سازی بقیه ستون‌ها
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


import pandas as pd

# تبدیل به DataFrame با اسم‌های ستون‌های قبلی
df_scaled = pd.DataFrame(scaled_features, columns=features.columns)

# اضافه کردن ستون target (قیمت خانه)
df_scaled['median_house_value'] = df['median_house_value']

from sklearn.model_selection import train_test_split

X = df_scaled.drop('median_house_value', axis=1)  # همه ستون‌ها به‌جز قیمت
y = df_scaled['median_house_value']               # فقط قیمت

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)