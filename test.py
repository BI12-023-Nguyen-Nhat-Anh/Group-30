import pandas as pd

# Đọc file excel vào dataframe
df = pd.read_excel('data/customer_test.xlsx')

# Tách dữ liệu ra theo cột và lưu vào một list
column_data = df['column_name'].tolist()
