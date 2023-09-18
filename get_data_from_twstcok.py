import os
import twstock as tt
import pandas as pd

name_attribute = ['Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change', 'Transcation']
tt.__update_codes()

target_stock = '2330'
stock = tt.Stock(target_stock)
target_price = stock.fetch_from(2023, 5)
# print(target_price)

df =  pd.DataFrame(columns=name_attribute,data=target_price)
# print(df)


filename = target_stock+'.csv'

csv_save_path = 'data/'+ target_stock+'/'
os.makedirs(csv_save_path, exist_ok= True)

df.to_csv(csv_save_path + filename)

print(os.path.abspath(os.getcwd()))