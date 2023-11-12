# -*- coding: utf-8 -*-
import abc
from typing import Any

from BusyBox.ServiceBox import Box, FactoryInjectAPI, factory_inject, HostFactory
from logging import info
box = Box()


class Context(object):
    session: Any

    def __init__(self, session: Any):
        self.session = session


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


class Child1API(metaclass=abc.ABCMeta):
    def func1(self) -> str:
        raise NotImplementedError


class Child2API(metaclass=abc.ABCMeta):
    def func2(self) -> str:
        raise NotImplementedError


class Child1Service(Child1API):

    def func1(self) -> str:
        return f"func1"


class Child2Service(Child2API):

    def func2(self) -> str:
        return "func2"


class Child1ServiceFactory(FactoryInjectAPI):

    def construct(self, context: Context) -> Child1API:
        print(f'refer in Fac: Context {id(context)}')
        return Child1Service()


class Child2ServiceFactory(FactoryInjectAPI):

    def construct(self) -> Child2API:
        return Child2Service()


@factory_inject(
    Child1ServiceFactory,
    Child2ServiceFactory,
    refer=Context
)
class FatherService(HostFactory):

    child1_service: Child1API
    child2_service: Child2API
    context: Context

    def __init__(self, *father_args, **father_kwargs):
        super().__init__()
        print(f'实例化 FatherService father_args: {father_args} father_kwargs: {father_kwargs}')
        self.context = Context('session_1')
        print(f'refer in Host -> Context {id(self.context)}')

    def test(self):
        print('test:', self.child1_service.func1(), self.child2_service.func2())


@factory_inject(
    Child1ServiceFactory,
    Child2ServiceFactory,
)
class FatherDeepService(object):

    child1_service: Child1API
    child2_service: Child2API

    def __init__(self, *father_args, **father_kwargs):
        pass

    def test(self):
        print('test:', self.child1_service.func1(), self.child2_service.func2())