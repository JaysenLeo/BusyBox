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