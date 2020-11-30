# -*- coding: utf-8 -*-
from ServiceBox import InjectorBox

inject = InjectorBox.Injector()


@inject.depend()
class CowService(object):

    def name(self):

        return __class__.__name__


if __name__ == "__main__":
    print(inject)
    inject.cow_service.name()
