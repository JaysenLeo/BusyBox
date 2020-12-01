# -*- coding: utf-8 -*-
import unittest
from BusyBox.ServiceBox import Box
from TestInjectorDemo import (
    AppleService, TestService, RestService, Bus1Service,
    CowService, box
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

    def test_multi_inj(self):
        self.box.inject(TestService, RestService, payload=dict(params1=1))
        self.assertEqual(id(self.box.test_service), id(self.box.test_service))

    def test_multi_simple_params_inj(self):
        self.box.inject(TestService, RestService, payload=dict(params1=2))
        self.assertEqual(self.box.test_service.handle(), self.box.rest_service.handle())

    def test_num_in_name_inj(self):
        self.box.inject(Bus1Service)
        self.assertEqual(self.box.bus1_service.name(), 'Bus1Service')

    def test_inj_by_decor(self):
        print(self.box2)
        self.assertEqual(self.box2.cow_service.name(), 'CowService')


if __name__ == "__main__":
    # inject.cow_service.name()
    suite = unittest.TestSuite()
    suite.addTest(InjectorTest('test_simple_inj'))
    suite.addTest(InjectorTest('test_multi_inj'))
    suite.addTest(InjectorTest('test_multi_simple_params_inj'))
    suite.addTest(InjectorTest('test_num_in_name_inj'))
    runner = unittest.TextTestRunner()
    runner.run(suite)


    # ij = InjectorBox.Injector()
    # ij.inject(TestService, RestService, payload=dict(params1=1))
    # t_obj = ij.test_service
    # print(id(t_obj))
    # t_obj.handle()
    # t_obj.handle()
    # print(id(t_obj))
    # r_obj = ij.rest_service
    # print(id(r_obj))
    # r_obj.handle()
    # r_obj.handle()
    # print(id(r_obj))
    # inj = InjectorBox.Injector()
    # i = inj.Inject(TestService, RestService, payload=dict(params1=1))