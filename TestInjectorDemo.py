# -*- coding: utf-8 -*-
from BusyBox.ServiceBox import Box
from logging import info
box = Box()


class AppleService(object):

    def name(self):
        return __class__.__name__


class Bus1Service(object):

    def name(self):
        return __class__.__name__


@box.depend()
class CowService(object):

    @staticmethod
    def name():
        _name = __class__.__name__
        print('_name:', _name)
        return _name


@box.depend()
class EasyService(object):

    def __init__(self, params1, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.params1 = params1

    def name(self):
        print('self.args:', self.args)
        print('self.kwargs', self.kwargs)
        print('self.params1', self.params1)
        return self.params1, self.args, self.kwargs


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
