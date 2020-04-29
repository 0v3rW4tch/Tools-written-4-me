import requests,json,sys

def getDoamin(domain):
    get_info_url = 'http://ce.baidu.com/index/getRelatedSites?site_address={_}'.format(_=domain)
    res = requests.get(get_info_url)
    # print(res.text)
    return res.text 


def write_in_file(domain,contents):
    with open(domain + '.txt','a') as fp:
        for i in contents:
            fp.write(i['domain']+"\n")
    print("结果以保存在当前目录下的"+domain+'.txt中')


def start(domain):
    urlSet = getDoamin(domain)
    try:
        DataSet = json.loads(urlSet)['data']
        # print(len(DataSet))
        if len(DataSet):
            write_in_file(domain,DataSet)
        else:
            print("该域名在百度中没记录~")
    except:
        print("不合法的站点地址，请确认输入的地址")



if __name__ == '__main__':
    start(sys.argv[1])
