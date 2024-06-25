import pandas as pd

# 文件路径
file_path = '2023/01017099999.csv'

# 读取CSV文件
data = pd.read_csv(file_path)

# print(data.head(10))
print(data.columns)

print("LONGITUDE 列前10行数据:")
print(data['LONGITUDE'].head(5))

print("\nLATITUDE 列前10行数据:")
print(data['LATITUDE'].head(5))

print("\nELEVATION 列前10行数据:")
print(data['ELEVATION'].head(5))

print("\nWND 列前10行数据:")
print(data['WND'].head(5))

print("\nCIG 列前10行数据:")
print(data['CIG'].head(5))

print("\n\VIS 列前10行数据:")
print(data['VIS'].head(5))

print("\n\TMP 列前10行数据:")
print(data['TMP'].head(5))

print("\n\DEW 列前10行数据:")
print(data['DEW'].head(5))


print("\n\SLP 列前10行数据:")
print(data['SLP'].head(5))