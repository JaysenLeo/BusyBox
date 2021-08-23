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
        print('EasyService self.args:', self.args)
        print('EasyService self.kwargs', self.kwargs)
        print('EasyService self.params1', self.params1)
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


class PositionService(object):

    def __init__(self, params1: str):
        self.params1 = params1

    def show_params(self):
        print(f'{__class__}: self.params1:', self.params1)
        return self.params1


class Position1Service(object):

    def __init__(self, params1: str, **kwargs):
        self.params1 = params1
        self.kwargs = kwargs

    def show_params(self):
        print('self.params1:', self.params1)
        print('self.kwargs:', self.kwargs)
        return self.params1


class Position2Service(object):

    def __init__(self, params1: str, *_args):
        self.params1 = params1
        self.args = _args

    def show_params1(self):
        print('self.params1:', self.params1)
        return self.params1

    def show_args(self):
        print('self._args:', self.args)
        return self.args


class Position3Service(object):

    def __init__(self, params1: str, *_args, **_kwargs):
        self.params1 = params1
        self.args = _args

    def show_params1(self):
        print('self.params1:', self.params1)
        return self.params1

    def show_args(self):
        print('self._args:', self.args)
        return self.args


class Position4Service(object):

    def __init__(self, params1: str, *_args, **_kwargs):
        self.params1 = params1
        self.args = _args
        self.kwargs = _kwargs

    def show_params1(self):
        print('self.params1:', self.params1)
        return self.params1

    def show_args(self):
        print('self._args:', self.args)
        return self.args

    def show_kwargs(self):
        print('self._kwargs:', self.kwargs)
        return self.kwargs
