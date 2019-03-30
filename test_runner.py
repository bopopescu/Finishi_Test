import unittest
import HTMLTestRunnerNew
from Test_data import test_login
from Test_data import test_recharge
from Test_data import test_register
from common.proje_path import report_path

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_login))
suite.addTest(loader.loadTestsFromModule(test_recharge))
suite.addTest(loader.loadTestsFromModule(test_register))
with open(report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='测试报告',
                                            description='2019.3.27接口自动化测试报告',
                                            tester='little-chen')
    runner.run(suite)