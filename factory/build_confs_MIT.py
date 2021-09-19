# -*- coding: utf-8 -*-
import re
import time

# confs names in template/ and ../
# except sr_head and sr_foot


confs_names = [
    'Shadowrocket_backcn_ad_MIT'
]


def getRulesStringFromFile(path):
    file = open(path, 'r', encoding='utf-8')
    contents = file.readlines()
    ret = ''
    for content in contents:
        content = content.strip('\r\n')
        if not len(content) or content.startswith('#'):
            continue
        else:
            ret += content
    return ret


if __name__ == "__main__":
    # get head and foot
    str_head = open('template/Shadowrocket_head.txt', 'r', encoding='utf-8').read()
    str_foot = open('template/Shadowrocket_foot.txt', 'r', encoding='utf-8').read()

    # make values
    values = {'build_time': time.strftime("%Y-%m-%d %H:%M:%S"),
              'Mit_HostName': getRulesStringFromFile('resultant/Advertising_MITM.conf')}

    # make confs
    for conf_name in confs_names:
        file_template = open('template/' + conf_name + '.txt', 'r', encoding='utf-8')
        template = file_template.read()
        template = str_head + template + str_foot
        file_output = open('../' + conf_name + '.conf', 'w', encoding='utf-8')

        marks = re.findall(r'{{(.+)}}', template)
        for mark in marks:
            template = template.replace('{{' + mark + '}}', values[mark])

        file_output.write(template)

    print('Done!')
