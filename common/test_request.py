import requests
class TestRequest:
    def testrequest(self,method,url,Param,cookies):
        '''

        :param method:传入方法
        :param url:接口地址
        :param Param:参数
        :return:
        '''
        COOKIE=None
        global res
        if method.upper()=='GET':
            res=requests.get(url,params=Param,cookies=cookies)
            #get请求，传参使用params
        elif method.upper()=='POST':
            res=requests.post(url,data=Param,cookies=cookies)
            #post请求，传参使用data
        else:
            print('请求无效，不支持{}请求'.format(method))
        return res
if __name__ == '__main__':
    res_1=TestRequest().testrequest('post','http://47.107.168.87:8080/futureloan/mvc/api/member/login',{"mobilephone":"18254124516","pwd":"2584561"},cookies=None)
    cook=res_1.cookies
    res_1=TestRequest().testrequest('post','http://47.107.168.87:8080/futureloan/mvc/api/loan/add',{"memberId":"1127428","title":"自动化有点意思啊哈","amount":10000,"loanRate":18.0,"loanTerm":6,"loanDateType":0,"repaymemtWay":5,"biddingDays":5}
,cookies=cook)
    print(res_1.text)