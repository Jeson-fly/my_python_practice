# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/5/26
  Desc  ：
"""
{
    1: {1: 0.8007, 2: 0.6607, 3: 0.4673, 4: 0.3007, 5: 0.2607, 6: 0.234, 7: 0.215, 8: 0.1907, 9: 0.1796, 10: 0.1507},
    2: {1: 0.8819, 2: 0.7319, 3: 0.5486, 4: 0.4319, 5: 0.3219, 6: 0.2152, 7: 0.2105, 8: 0.2069, 9: 0.2041, 10: 0.1419},
    3: {1: 0.8409, 2: 0.6965, 3: 0.5817, 4: 0.3743, 5: 0.2698, 6: 0.2669, 7: 0.2648, 8: 0.2632, 9: 0.2619, 10: 0.1409},
    4: {1: 0.8631, 2: 0.6881, 3: 0.5297, 4: 0.3256, 5: 0.2231, 6: 0.2214, 7: 0.2202, 8: 0.2193, 9: 0.2186, 10: 0.1381},
    5: {1: 0.8584, 2: 0.6824, 3: 0.5671, 4: 0.4344, 5: 0.3628, 6: 0.3318, 7: 0.311, 8: 0.2604, 9: 0.1808, 10: 0.1296},
    6: {1: 0.8357, 2: 0.6245, 3: 0.5508, 4: 0.489, 5: 0.4179, 6: 0.3771, 7: 0.3066, 8: 0.2562, 9: 0.1759, 10: 0.1257},
    7: {1: 0.8313, 2: 0.6632, 3: 0.5604, 4: 0.4991, 5: 0.4683, 6: 0.4377, 7: 0.3873, 8: 0.2677, 9: 0.1968, 10: 0.1246},
    8: {1: 0.8044, 2: 0.6982, 3: 0.5961, 4: 0.4951, 5: 0.4244, 6: 0.3694, 7: 0.3137, 8: 0.2435, 9: 0.1833, 10: 0.1232},
    9: {1: 0.8348, 2: 0.6499, 3: 0.5782, 4: 0.5274, 5: 0.4269, 6: 0.3666, 7: 0.3064, 8: 0.2362, 9: 0.1726, 10: 0.1219},
    10: {1: 0.8625, 2: 0.6585, 3: 0.5572, 4: 0.5065, 5: 0.4161, 6: 0.3559, 7: 0.2957, 8: 0.2255, 9: 0.1754, 10: 0.1213},
    11: {1: 0.8878, 2: 0.6445, 3: 0.5434, 4: 0.4928, 5: 0.4025, 6: 0.3422, 7: 0.2821, 8: 0.2282, 9: 0.1719, 10: 0.1208},
    12: {1: 0.8108, 2: 0.6308, 3: 0.5607, 4: 0.4866, 5: 0.4063, 6: 0.3361, 7: 0.2706, 8: 0.2159, 9: 0.1758, 10: 0.1201},
    13: {1: 0.8317, 2: 0.6294, 3: 0.5586, 4: 0.4782, 5: 0.3979, 6: 0.3378, 7: 0.2677, 8: 0.2176, 9: 0.1675, 10: 0.1195},
    14: {1: 0.8509, 2: 0.6288, 3: 0.5482, 4: 0.4778, 5: 0.3976, 6: 0.3345, 7: 0.2644, 8: 0.2133, 9: 0.1648, 10: 0.1172},
    15: {1: 0.8684, 2: 0.6166, 3: 0.5461, 4: 0.4658, 5: 0.3856, 6: 0.3315, 7: 0.2614, 8: 0.2103, 9: 0.1616, 10: 0.1152},
    16: {1: 0.8845, 2: 0.683, 3: 0.5424, 4: 0.4622, 5: 0.3782, 6: 0.3319, 7: 0.2618, 8: 0.2118, 9: 0.1617, 10: 0.1137},
    17: {1: 0.7993, 2: 0.6979, 3: 0.5475, 4: 0.4572, 5: 0.3771, 6: 0.3297, 7: 0.2569, 8: 0.2069, 9: 0.1568, 10: 0.1128},
    18: {1: 0.8129, 2: 0.69117, 3: 0.5313, 4: 0.4511, 5: 0.3709, 6: 0.3209, 7: 0.2508, 8: 0.2008, 9: 0.1507,
         10: 0.1117},
    19: {1: 0.8255, 2: 0.7244, 3: 0.5324, 4: 0.4438, 5: 0.3637, 6: 0.3136, 7: 0.2436, 8: 0.1935, 9: 0.1435, 10: 0.1101},
    20: {1: 0.8371, 2: 0.7361, 3: 0.5258, 4: 0.4456, 5: 0.3555, 6: 0.3054, 7: 0.2354, 8: 0.1953, 9: 0.1453, 10: 0.1088}
}

import time

cur_timestamp = int(time.time())
cur_day = time.strftime("%Y%m%d", time.localtime(cur_timestamp))
yesterday = time.strftime("%Y%m%d", time.localtime(cur_timestamp - 24 * 3600))
print(cur_day, yesterday)
l = ['#在地铁上被孕妇让座了#', '#拜登使用呼吸机治疗睡眠呼吸暂停#', '韩国改周岁算法后', '#台媒曝陈建州全裸骚扰S妈#']

for i in l:
    print(i.strip("#"))
print(set(map(lambda x: x.strip("#"), l)))
enumerate