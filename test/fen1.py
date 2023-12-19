import requests
import json

fans_list=[]

url='https://mp-action.csdn.net/interact/wrapper/pc/fans/v1/api/getFansOffsetList'
# 'https://mp-action.csdn.net/interact/wrapper/pc/fans/v1/api/getFansOffsetList'
# 'pageSize=20&username=weixin_62650212&fanId=2080628'
# url='https://mp-action.csdn.net/interact/wrapper/pc/fans/v1/api/getFollowOffsetList'
params={
	'pageSize':20,
	'username':'WhereIsHeroFrom'
}
res=requests.get(url=url,params=params).json()
fans_list.extend(res['data']['list'])
fanId=res['data']['fanId']
while fanId:
    params['fanId']=fanId
    res=requests.get(url=url,params=params).json()
    fans_list.extend(res['data']['list'])
    print(res['data']['list'])
    fanId=res['data']['fanId']
    print(len(fans_list))

    with open('fans_list.json', 'w',encoding='utf-8') as f:
        json.dump(fans_list,f,ensure_ascii=False)