> 示例一:
- 单实例化
```python
from BusyBox.ServiceBox import Box

class AppleService(object):

    def name(self):
        return 'test'

if __name__ == '__main__':
    box = Box()
    box.inject(AppleService)
    box.apple_service.name()
```
> 示例二:
- 带参 多实例化
```python
from BusyBox.ServiceBox import Box

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

if __name__ == '__main__':
    box = Box()
    box.inject(TestService, RestService, payload=dict(params1=1))
    box.rest_service.handle()
    box.test_service.handle()
```
> 示例三:
- 类命名中带实例
```python
from BusyBox.ServiceBox import Box

class Bus1Service(object):

    def name(self):
        return 'test'

if __name__ == '__main__':
    box = Box()
    box.inject(Bus1Service)
    box.bus1_service.name()
```
> 示例四:
- 类命名中带实例
```python
from BusyBox.ServiceBox import Box

box = Box()

@box.depend()
class CowService(object):

    @staticmethod
    def name():
        return 'test'

if __name__ == '__main__':
    box = Box()
    box.inject(CowService)
    box.cow_service.name()
```
> 示例五:
- __init__方法带参实例
```python
from BusyBox.ServiceBox import Box

box = Box()

@box.depend()
class EasyService(object):

    def __init__(self, params1, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.params1 = params1

    def name(self):
        return self.params1, self.args, self.kwargs

if __name__ == '__main__':
    box = Box()
    box.invoke('easy_service', 1, 2, 3, a=4, b=5)
    box.easy_service.name()
```
> 示例六:
- 注入参数 在__init__参数中不需要时，在有没有kwargs参数情况下会忽略
```python
from BusyBox.ServiceBox import Box
class PositionService(object):

    def __init__(self, params1: str):
        self.params1 = params1

    def show_params(self):
        print(f'{__class__}: self.params1:', self.params1)
        return self.params1
if __name__ == '__main__':
    box = Box()
    box.inject(PositionService, payload={'params1': 1, 'params2': 1})
    box.position_service.show_params()
    """
    输出：
        <class 'TestInjectorDemo.PositionService'>: self.params1: 1
    """
```
> 示例七:
- 实体重置复用
```python
from BusyBox.ServiceBox import Box

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

if __name__ == '__main__':
    box = Box()
    box.inject(Position4Service, args_payload=(99, 1, 2, 3, 4), kwargs_payload=dict(params2=88))
    box.position4_service.show_params1() == 99              # True
    box.position4_service.show_args() == (1, 2, 3, 4)       # True
    box.position4_service.show_kwargs() == dict(params2=88) # True
    box.position4_service.params1 = 100                     # True
    box.position4_service.show_params1() == 100
    # 重置
    box.reset('position4_service')
    box.position4_service.show_params1() == 99              # True
    box.position4_service.show_args() == (1, 2, 3, 4)       # True
    box.position4_service.show_kwargs() == dict(params2=88) # True
```