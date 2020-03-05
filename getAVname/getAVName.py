import requests
import json

def getAvlist():
    url = 'https://raw.githubusercontent.com/r00tSe7en/get_AV/master/av.json'
    content = requests.get(url).text
    content = json.loads(content)
    return content


def load_json_file():
    with open('./avlist.json','r',encoding='utf-8') as fp:
        content = fp.read()
    # print(content)
    content = json.loads(content)
    return content

def check(avName,avList):
    if avName in avList.keys():
        print("Found it : " + avName + " => " +avList[avName])
    else:
        print("Oooops! 未知的进程")

def update():
    content = getAvlist()
    with open('./avlist.json','w') as fp:
        json.dump(content,fp)


if __name__ == '__main__':
    model = input("请输入模式，模式1：拉取json文件搜索 模式2：本地读取json文件搜索 模式3：更新本地json文件\n")
    if model == '3':
        update()
        print("更新成功")
    elif model == '2' or model == '1':
        avName = input("请输入进程名字:")
        if model == '1':
            avList = getAvlist()
            check(avName,avList)
        else:
            avList = load_json_file()
            check(avName,avList)
    else:
        print("Oooops 请按要求输入哦~~")
    
