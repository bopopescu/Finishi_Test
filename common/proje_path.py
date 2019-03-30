import os
path=os.path.realpath(__file__)
#获取当前文件所在的绝对路径
common_path=os.path.split(path)[0]
#common文件夹的绝对路径
Api_test_path=os.path.split(common_path)[0]
#Api文件夹的绝对路径
conf_path=os.path.join(Api_test_path,'conf','case.conf')
#配置文件路径
log_path=os.path.join(Api_test_path,'Test_Log','测试日志.log')
#测试日志路径
cases_path=os.path.join(Api_test_path,'Test_data','前程贷接口自动化测试用例.xlsx')
#测试用例路径
# print(cases_path)
report_path=os.path.join(Api_test_path,'Test_Report','前程贷接口自动化测试报告.html')
#测试报告路径