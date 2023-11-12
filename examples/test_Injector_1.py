# -*- coding: utf-8 -*-
import unittest
from BusyBox.ServiceBox import Box
from examples.TestInjectorDemo_1 import (
    AppleService, TestService, RestService, Bus1Service,
    PositionService, Position1Service, Position2Service,
    Position3Service, Position4Service, box, FatherService, AppleServiceFactory
)


class InjectorTest(unittest.TestCase):

    def setUp(self) -> None:
        '''
        测试之前的准备工作
        :return:
        '''
        self.box = Box()
        self.box2 = box

    def tearDown(self) -> None:
        '''
        测试之后的收尾
        :return:
        '''
        pass

    def test_simple_inj(self):
        self.box.inject(AppleService)
        self.assertEqual(self.box.apple_service.name(), 'AppleService')

    def test_factory_inj(self):
        self.box.inject_factory(AppleServiceFactory)
        self.assertEqual(self.box.apple_service.name(), 'AppleService', '工厂注册')

    def test_multi_inj(self):
        self.box.inject(TestService, RestService, payload=dict(params1=1))
        self.assertEqual(id(self.box.test_service), id(self.box.test_service))

    def test_multi_simple_params_inj(self):
        self.box.inject(TestService, RestService, payload=dict(params1=2))
        self.assertEqual(self.box.test_service.handle(), self.box.rest_service.handle())

    def test_num_in_name_inj(self):
        self.box.inject(Bus1Service)
        self.assertEqual(self.box.bus1_service.name(), 'Bus1Service', msg="服务名中含数字")

    def test_init_with_params_inj(self):
        easy_service = self.box2.invoke('easy_service', 1, 2, 3, a=4, b=5)
        self.assertEqual(easy_service.name(), (1, (2, 3), {'a': 4, 'b': 5}))

    def test_inj_by_decor(self):
        print(self.box2)
        self.assertEqual(self.box2.cow_service.name(), 'CowService')

    def test_position_param_no_exist(self):
        """ 注入参数命名 与 宿主类 __init__ 参数不匹配 在无 kwargs 的情况下 直接忽略"""
        self.box.inject(PositionService, payload={'params1': 1, 'params2': 1})
        self.assertEqual(self.box.position_service.show_params(), 1)

    def test_position_param_no_exist_has_kwargs(self):
        """ 注入参数命名 与 宿主类 __init__ 参数不匹配 """
        self.box.inject(Position1Service, payload={'params1': 1, 'params2': 1})
        self.assertEqual(self.box.position1_service.show_params(), 1)

    def test_position_param_all_args(self):
        """ 注入参数命名 与 宿主类 __init__ 参数不匹配 """
        self.box.inject(Position2Service, payload=(1, 2, 3, 4))
        self.assertEqual(self.box.position2_service.show_params1(), 1)
        self.assertEqual(self.box.position2_service.show_args(), (2, 3, 4))

    def test_position_param_args_kwargs(self):
        """ 注入参数命名 与 宿主类 __init__ 参数不匹配 """
        self.box.inject(Position3Service, payload=(1, 2, 3, 4))
        self.assertEqual(self.box.position3_service.show_params1(), 1)
        self.assertEqual(self.box.position3_service.show_args(), (2, 3, 4))

    def test_position_param_args_kwargs1(self):
        """ 注入参数命名 与 宿主类 __init__ 参数不匹配 """
        self.box.inject(Position4Service, args_payload=(99, 1, 2, 3, 4), kwargs_payload=dict(params2=88))
        self.assertEqual(self.box.position4_service.show_params1(), 99)
        self.assertEqual(self.box.position4_service.show_args(), (1, 2, 3, 4))
        self.assertEqual(self.box.position4_service.show_kwargs(), dict(params2=88))
        print('重置前：', id(self.box.position4_service))
        self.box.position4_service.params1 = 100
        self.assertEqual(self.box.position4_service.show_params1(), 100)
        self.box.reset('position4_service')
        self.assertEqual(self.box.position4_service.show_params1(), 99)
        self.assertEqual(self.box.position4_service.show_args(), (1, 2, 3, 4))
        self.assertEqual(self.box.position4_service.show_kwargs(), dict(params2=88))
        print('重置后：', id(self.box.position4_service))

    def test_service_api_inject(self):
        """ 服务中根据依赖服务的接口注入 """
        f_srv = FatherService()
        self.assertEqual(f_srv.child1_service.func1(), 'func1', '服务中根据依赖服务的接口注入')
        self.assertEqual(f_srv.child2_service.func2(), 'func2', '服务中根据依赖服务的接口注入')
        f_srv.test()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(InjectorTest('test_simple_inj'))
    suite.addTest(InjectorTest('test_multi_inj'))
    suite.addTest(InjectorTest('test_multi_simple_params_inj'))
    suite.addTest(InjectorTest('test_num_in_name_inj'))
    suite.addTest(InjectorTest('test_inj_by_decor'))
    suite.addTest(InjectorTest('test_position_param_no_exist'))
    suite.addTest(InjectorTest('test_position_param_no_exist_has_kwargs'))
    suite.addTest(InjectorTest('test_position_param_all_args'))
    suite.addTest(InjectorTest('test_position_param_args_kwargs'))
    suite.addTest(InjectorTest('test_position_param_args_kwargs1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)