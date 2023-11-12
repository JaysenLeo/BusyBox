# -*- coding: utf-8 -*-
import abc
from typing import Any
from BusyBox.ServiceBox import FactoryInjectAPI, factory_inject


class Child1RefAPI(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_context_id(self) -> int:
        raise NotImplementedError


class Child2RefAPI(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_context_id(self) -> int:
        raise NotImplementedError


class Context(object):
    session: Any

    def __init__(self, session: Any):
        self.session = session


class ContextChild1(object):
    session: Any

    def __init__(self, session: Any):
        self.session = session


class Child1RefService(Child1RefAPI):
    context: Context

    def __init__(self, ctx: Context):
        self.context = ctx

    def get_context_id(self) -> int:
        print(f"Child1 Context {self.context} {id(self.context)}")
        return id(self.context)


class Child2RefService(Child2RefAPI):
    context: Context

    def __init__(self, ctx: Context):
        self.context = ctx

    def get_context_id(self) -> int:
        print(f"Child2 Context {self.context} {id(self.context)}")
        return id(self.context)


class Child1RefServiceFactory(FactoryInjectAPI):

    def construct(self, context: Context) -> Child1RefAPI:
        return Child1RefService(context)


class Child2RefServiceFactory(FactoryInjectAPI):

    def construct(self, context: Context) -> Child2RefAPI:
        return Child2RefService(context)


@factory_inject(
    Child1RefServiceFactory,
    Child2RefServiceFactory,
    refer=Context
)
class FatherDeepService(object):

    child1_service: Child1RefAPI
    child2_service: Child2RefAPI
    context_host: Context

    def __init__(self):
        self.context_host = Context('context from host')
        print(f'Host Context initialize {self.context_host} {id(self.context_host)}')

    def is_context_id_deep_transmission(self):
        print(f'[Func] is_context_id_deep_transmission [Msg] 判断服务注入 context 传递是否成功  [Detail] child1 context: {self.child1_service.get_context_id()} '
              f'child1 context: {self.child2_service.get_context_id()}')
        return id(self.context_host) == self.child1_service.get_context_id() == self.child2_service.get_context_id()