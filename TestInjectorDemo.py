# -*- coding: utf-8 -*-
from BusyBox.ServiceBox import Box

box = Box()


class AppleService(object):

    def name(self):
        return __class__.__name__


class Bus1Service(object):

    def name(self):
        return __class__.__name__


@box.depend()
class CowService(object):

    def name(self):
        return __class__.__name__


class TestService(object):

    def __init__(self, params1):
        self.params1 = params1

    def handle(self):
        return self.params1


class RestService(object):

    def __init__(self, params1):
        self.params1 = params1

    def handle(self):
        return self.params1


# if __name__ == "__main__":
#     inject.cow_service.name()
#     suite = unittest.TestSuite()
#     suite.addTest(MyclassTest('test_simple_inj'))
#     # suite.addTest(MyclassTest('test_sub'))
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
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