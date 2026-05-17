# -*- coding: utf-8 -*-
import re

# 读取cities.json文件
with open(r'e:\26年客户留存\一月份\1.27\更新\新\cities.json', 'r', encoding='utf-8') as f:
    cities_json = f.read()

# 读取weather.html文件
with open(r'e:\26年客户留存\一月份\1.27\更新\新\weather.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 使用正则表达式替换cities变量
pattern = r'const cities = \[.*?\];'
replacement = f'const cities = {cities_json};'

# 执行替换
new_html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

# 写回weather.html文件
with open(r'e:\26年客户留存\一月份\1.27\更新\新\weather.html', 'w', encoding='utf-8') as f:
    f.write(new_html_content)

print("weather.html更新完成")
