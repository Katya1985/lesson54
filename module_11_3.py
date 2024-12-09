import inspect
import sys
import requests
from pprint import pprint


class Introspection:
    pass

def introspection_info(obj):
    type_ = type(obj).__name__                                      # Тип объекта
    attributes_ = getattr(introspection_info, 'obj', None)          # Атрибуты объекта
    methods_ = dir(introspection_info)                              # Методы объекта
    module_ = inspect.getmodule(introspection_info)                 # Модуль, к которому объект принадлежит
    dir_ = dir(obj)                                                 # Cписок имён, определяемых объектом.
    callable_ = callable(introspection_info)                        # Проверка можно вызвать или нет
    id_ = id(Introspection)                                         # Уникальный идентификатор

    return {'type': type_, 'attributes' : attributes_, 'methods': methods_, 'module': module_,
    'dir': dir_,'callable': callable_,'id': id_}


obj = Introspection
number_info = introspection_info(42)
pprint(number_info)
