# -*- coding:utf-8 -*-
from list_test import _list_, _map_
# 如果不在loop目录下的__init__.py里 加入 from .for_loop import for_test，那么就要用下面的全路径方式引入
# from packages.loop.for_loop import for_test
# 如果在__init__.py定义了后，就可以使用以下的方式
from packages.loop import for_test


def hello():
    _str = input("input something:")
    print("%s" % _str)
    _list_()
    _map_()


hello()
for_test()
