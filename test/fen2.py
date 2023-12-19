import json

with open('fans_list.json', 'r',encoding='utf-8') as file:
    fans_list = json.load(file)

print(len(fans_list))
avatars_list=[user['avatar'].replace('!1','') for user in fans_list if 'default.jpg' not in user['avatar']]
print(f'共有{len(avatars_list)}张非默认图片！')
import time
import requests
for url in avatars_list[6176:]:
    print(f'{avatars_list.index(url)}，{url}保存中~')
    name=url.split('/')[-1]
    res=requests.get(url=url).content
    with open(f'csdn_/{name}','wb') as f:
        f.write(res)
    time.sleep(0.05)
# 3060，https://profile-avatar.csdnimg.cn/6ea9bdec9250477488fa61e3895115d3_djwsn.jpg保存中~