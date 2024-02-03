import csv

"""
表格文件存储

CSV, 全称 Comma Separated Values, 即逗号分隔值文件, 其文件以纯文本形式存储数据。
"""

# # -----------------------------------

"""
数组写入
"""

# with open('spider/data_array_test.csv', 'w') as f:
#   writer = csv.writer(f, delimiter='\t')
#   writer.writerow(['name', 'age', 'gender'])
#   writer.writerow(['Alice', 25, 'female'])
#   writer.writerow(['Bob', 30, 'male'])
#   writer.writerow(['Charlie', 35, 'female'])

# # -----------------------------------

"""
字典写入
"""

with open('spider/data_dict_test.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames=['name', 'age', 'gender'])
  writer.writeheader()
  writer.writerow({'name': 'Alice', 'age': 25, 'gender': 'female'})
  writer.writerow({'name': 'Bob', 'age': 30, 'gender': 'male'})
  writer.writerow({'name': 'Charlie', 'age': 35, 'gender': 'female'})

# # -----------------------------------
