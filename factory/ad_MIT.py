# -*- coding: utf-8 -*-
# 提取广告规则

import sys
import time

import requests

rules = [
    # blackmatrix7 过滤规则
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Advertising/Advertising.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Advertising/Advertising_Domain.list',
    'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/China/China.list',
    'https://github.com/blackmatrix7/ios_rule_script/raw/master/rule/Shadowrocket/Advertising/Advertising_MITM.conf',
    'https://choler.github.io/Surge/Script/YouTube.js'
]

for rule in rules:
    filename = rule.split('/')[-1]
    print('downloading... ' + rule)

    # get rule text
    success = False
    try_times = 0
    res = None
    while try_times < 5 and not success:
        res = requests.get(rule)
        if res.status_code != 200:
            time.sleep(1)
            try_times = try_times + 1
        else:
            success = True
            break

    if not success:
        sys.exit('error in request {} \n return code: {}'.format(rule, res.status_code))

    if filename.split('.')[-1] == 'list':
        with open('resultant/{}'.format(filename), 'wb') as file:
            file.write(res.content)
    elif filename.split('.')[-1] == 'js':
        with open('resultant/Script/{}'.format(filename), 'wb') as file:
            file.write(res.content)

print("Done!")
