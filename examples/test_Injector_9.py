# -*- coding: utf-8 -*-
import unittest
from BusyBox.ServiceBox import Box
from examples.TestInjectorDemo_9 import FatherDeepService


class InjectorTest(unittest.TestCase):

    def setUp(self) -> None:
        '''
        测试之前的准备工作
        :return:
        '''
        self.box = Box()

    def tearDown(self) -> None:
        '''
        测试之后的收尾
        :return:
        '''
        pass

    def test_service_api_inject(self):
        """ 服务中根据依赖服务的接口注入 """
        f_srv = FatherDeepService()
        self.assertEqual(f_srv.is_context_id_deep_transmission(), True, '判断服务注入 context 传递是否成功')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(InjectorTest('test_service_api_inject'))
    runner = unittest.TextTestRunner()
    runner.run(suite)