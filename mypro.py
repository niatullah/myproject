import pandas as pd

# مسیر فایل CSV روی دسکتاپ
melbourne_file_path = 'melb_data.csv'

# خواندن داده‌ها
melbourne_data = pd.read_csv(melbourne_file_path)

# چاپ خلاصه آماری
print(melbourne_data.describe())