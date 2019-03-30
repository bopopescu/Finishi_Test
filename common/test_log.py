import logging
from common.proje_path import log_path
from common.test_config import TestConfig
class TestLog:
    '''测试日志类，可以将日志信息打印到控制台和指定的日志文件'''
    test_log_name=TestConfig().get_data('LOGGER','test_log')
    test_log_level=TestConfig().get_data('LOGGER','test_log_level')
    ch_level=TestConfig().get_data('LOGGER','ch_level')
    fh_level=TestConfig().get_data('LOGGER','fh_level')
    format_conf=TestConfig().get_data('LOGGER','fomatter_conf')
    #调用配置类，将日志的等级、名称、格式等信息进行可配置化操作
    def log(self,level,msg):
        '''
        :param level: 日志等级
        :param msg: 日志信息
        :return: None
        '''
        test_log=logging.getLogger(self.test_log_name)
        #添加日志收集器，并命名为 api_test
        test_log.setLevel(self.test_log_level)
        #设置日志收集器收集日志的等级
        formatter=logging.Formatter(self.format_conf)
        #设置输出的日志格式
        ch=logging.StreamHandler()
        #添加控制台日志处理器，可将日志信息打印到控制台
        ch.setLevel(self.ch_level)
        #设置处理器处理日志的最低等级
        ch.setFormatter(formatter)
        #设置处理器输出的日志格式
        fh=logging.FileHandler(log_path,encoding="UTF-8")
        #添加文本日志处理器，可将日志信息打印到文本
        fh.setLevel(fh.level)
        #设置处理器处理日志的最低等级
        fh.setFormatter(formatter)
        #设置处理输出的日志格式
        test_log.addHandler(ch)
        test_log.addHandler(fh)
        #将对应的处理器添加到日志收集器中
        if level=="DEBUG":
            test_log.debug(msg)
        elif level=="INFO":
            test_log.info(msg)
        elif level=="WARNING":
            test_log.warning(msg)
        elif level=="ERROR":
            test_log.error(msg)
        else:
            test_log.critical(msg)
        #判断等级，并输出信息
        test_log.removeHandler(ch)
        test_log.removeHandler(fh)
        #移除日志处理器
    def debug(self,msg):
        '''
        调用log方法，并传入对应的等级，方便调用
        :param msg: 输出的信息
        :return:
        '''
        self.log("DEBUG",msg)
    def info(self,msg):
        self.log("INFO",msg)
    def warning(self,msg):
        self.log("WARNING",msg)
    def error(self,msg):
        self.log("ERROR",msg)
    def critical(self,msg):
        self.log("CRITICAL",msg)
if __name__ == '__main__':
    TestLog().info("我错了")