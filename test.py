# -*- coding: utf-8 -*-
import re
import json
msg = input()
difficulty = re.match(r'(\d)',msg).group()
name = re.match(r'(\d)!(\w+),',msg).group(2)
phone = re.search(r'(\d{11})',msg).group()
address = re.sub(r'\d{11}', "", re.match(r'(\d)!(\w+),(\w+).',msg).group(3))
person = {"姓名":name, "手机":phone}
area = []
if difficulty == '1':
    province = re.search(r'(\w+省)|(\w+自治区)|(北京市|上海市|天津市|重庆市)',address)
    if province:
        area.append(province.group())
    else:
        area.append("")
    address1 = re.sub(province.group(), "", address) #去掉省级之后的地址

    if province != '北京市|上海市|天津市|重庆市':
        city = re.search( r'(\w+?市)|(\w+?自治州)', address1)
        if city:
            area.append(city.group())
            address2 = re.sub(city.group(), "", address1) #去掉省级和市级之后的地址
        else:
            area.append("")
            address2 = address1
    else:
        city = province
        area.append(city.group())
        address2 = address1

    district = re.search(r'(\w+?区)|(\w+?县)|(\w+?市)', address2)
    if district:
        area.append(district.group())
        address3 = re.sub(district.group(), "", address2) #去掉省市区级别后的地址
    else:
        area.append("")
        address3 = address2
    
    town = re.search(r'(\w+?街道)|(\w+?镇)|(\w+?乡)', address3)
    if town:
        area.append(town.group())
        address4 = re.sub(town.group(), "", address3) #详细地址
    else:
        area.append("")
        address4 = address3
    area.append(address4)

elif difficulty == '2':
    province = re.search(r'(\w+?省)|(\w+?自治区)|(北京市|上海市|天津市|重庆市)',address)
    if province:
        area.append(province.group())
    else:
        area.append("")
    address1 = re.sub(province.group(), "", address) #去掉省级之后的地址

    if province != '北京市|上海市|天津市|重庆市':
        city = re.search( r'(\w+?市)|(\w+?自治州)', address1)
        if city:
            area.append(city.group())
            address2 = re.sub(city.group(), "", address1) #去掉省级和市级之后的地址
        else:
            area.append("")
            address2 = address1
    else:
        city = province
        area.append(city.group())
        address2 = address1

    district = re.search(r'(\w+?区)|(\w+?县)|(\w+?市)', address2)
    if district:
        area.append(district.group())
        address3 = re.sub(district.group(), "", address2) #去掉省市区级别后的地址
    else:
        area.append("")
        address3 = address2
    
    town = re.search(r'(\w+?街道)|(\w+?镇)|(\w+?乡)', address3)
    if town:
        area.append(town.group())
        address4 = re.sub(town.group(), "", address3) #路名，门牌号，详细地址
    else:
        area.append("")
        address4 = address3
    
    road = re.search(r'(\w+?路)|(\w+?街)|(\w+?巷)', address4)
    if road:
        area.append(road.group())
        address5 = re.sub(road.group(), "", address4) #门牌号，详细地址
    else:
        area.append("")
        address5 = address4

    number = re.search(r'(\w+?号)', address5)
    if number:
        area.append(number.group())
        address6 = re.sub(number.group(), "", address5) #详细地址
    else:
        area.append("")
        address6 = address5
    area.append(address6)
person['地址'] = area
jsonStr = json.dumps(person,ensure_ascii=False)
print(jsonStr)