from mysql import connector
from common.test_config import TestConfig
from common.proje_path import conf_path

class DoMysql:
    '''链接数据库并操作'''
    def domysql(self,query,flag=1):
        '''

        :param query:数据库操作语句
        :param flag: 默认为1，查询一条数据；另外可以查询多条
        :return: res查询结果
        '''
        host=TestConfig().get_data('MYSQL','address')
        #读取存储在配置文件内的数据库信息
        res=connector.connect(**eval(host))
        #连接数据库
        cursor=res.cursor()
        #建立游标
        cursor.execute(query)
        #执行语句
        if flag==1:
            res=cursor.fetchone()
        else:
            res=cursor.fetchall()
        return res
