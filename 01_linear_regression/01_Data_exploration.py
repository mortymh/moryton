#01_Data_exploration

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

# مسیر فایل CSV — لطفاً اینو به مسیر واقعی فایل خودت تغییر بده
file_path = "/content/drive/MyDrive/datasets/housing.csv"
# بارگذاری داده‌ها
df = pd.read_csv(file_path)

# نمایش اولین 5 ردیف از داده‌ها
print(df.head())

# بررسی اطلاعات کلی دیتافریم
print(df.info())

# آمار توصیفی
print(df.describe())

# بررسی مقادیر گمشده
print(df.isnull().sum())


