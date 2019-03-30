import unittest
from ddt import ddt,data
from common.test_log import TestLog
from common.do_test_excel import DoExcel
from common.test_request import TestRequest
from common.test_get_data import GetData
from common.do_mysql import DoMysql


test_data=DoExcel().data_read('recharge')


# print(test_data)
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        '''执行用例前动作'''
        # global resp
        TestLog().info("===============测试开始=====================")
    def tearDown(self):
        '''执行用例后动作'''
        TestLog().info("===============测试结束=====================")

    @data(*test_data)    #将嵌套在列表内的字典格式用例做处理，分别取出字典格式用例并迭代赋值给变量cases
    def test_http_request(self,case):
        # global COOKIES
        #声明COOKIES为全局变量
        global resp
        global TestResult
        # global before_amount
        # global after_amount
        Caseid=case['用例序号']
        Module=case['模块']
        Method=case['请求方式']
        Url=case['接口地址']
        Case_name=case['用例名']
        param=eval(case['参数'])
        #传参使用字典格式
        Sql=case['sql']
        Expect_Result=case['预期结果']
        #字典格式断言预期结果与实际结果

        if case['sql'] is not None:
            before_amount=(DoMysql().domysql(eval(case['sql'])['sql']))[0]
        #充值前账户金额

        TestLog().info("正在执行{}模块，第{}条用例,用例名:{}".format(Module,Caseid,Case_name))
        getattr(GetData,'COOKIES')

        resp = TestRequest().testrequest(Method,Url,param,cookies=getattr(GetData,'COOKIES'))
        #获取请求结果  getattr(GetData,'COOKIES') --反射，获取类属性的值
        if case['sql'] is not None:
            after_amount=(DoMysql().domysql(eval(case['sql'])['sql']))[0]
            setattr(GetData,'leaveamout',after_amount)
        if Expect_Result.find('money') != -1:
            Expect_Result=case['预期结果'].replace('money',str(getattr(GetData,'leaveamout')))

        #充值后账户金额
        if resp.cookies:
            #判断请求结果cookies是否为真
            setattr(GetData,'COOKIES',resp.cookies)
            #反射，将登陆产生的cookie赋值给变量COOKIES


        try:
            if case['sql'] is not None:
                #sql不为空的情况下再判断
                Expect_amount= float(before_amount)+float(param['amount'])
                #预期金额=原金额+充值金额
                self.assertEqual(after_amount,Expect_amount)
                #断言实际金额与预期金额
            self.assertEqual(eval(Expect_Result),resp.json())
            #将请求结果转换为字典格式与预期结果对比
            TestResult='PASS'
        except AssertionError as e:
            TestLog().info("断言失败{}".format(e))
            TestResult='FAILED'
            raise e
        finally:
            TestLog().info("回写实际结果：{}".format(resp.text))
            DoExcel().data_write('recharge',Caseid+1,9,resp.text)
            TestLog().info("预期结果:：{}".format(Expect_Result))
            TestLog().info("回写测试结论：{}".format(TestResult))
            DoExcel().data_write('recharge',Caseid+1,10,TestResult)





