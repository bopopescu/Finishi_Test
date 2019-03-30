from configparser import ConfigParser
from common.proje_path import conf_path

class TestConfig:
    '''测试配置类，可通过下列方法获取到配置文件内的信息'''
    wb=ConfigParser()
    wb.read(conf_path,encoding='utf-8')

    def get_data(self,section,option):
        '''获取字符串
        ：:param:section--配置文件内的大标题，option--配置文件内的小标题'''
        res=self.wb.get(section,option)
        return res
    def get_int(self,section,option):
        '''获取整数'''
        res=self.wb.getint(section,option)
        return res

    def get_float(self,section,option):
        '''获取浮点数'''
        res=self.wb.getfloat(section,option)
        return res
    def get_boolean(self,section,option):
        '''获取布尔值'''
        res=self.get_float(section,option)
        return res

if __name__ == '__main__':
    res=TestConfig().get_data('CASE','case')
    print(res)