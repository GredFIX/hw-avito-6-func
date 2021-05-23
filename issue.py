from collections import defaultdict
from collections.abc import Iterable
from itertools import islice


def ilen(iterable: Iterable) -> int:
    """Функция получения размера генератора
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return sum(1 for _ in iterable)


def flatten(iterable: Iterable) -> Iterable:
    """Делает из многоуровневого массива одноуровневый
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    for i in iterable:
        if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
            yield from flatten(i)
        else:
            yield i


def distinct(iterable: Iterable) -> dict:
    """Удалит дубликаты, сохранив порядок
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    return dict.fromkeys(iterable)


def groupby(key, iterable: Iterable) -> dict:
    """Упорядочивает неупорядоченную последовательность из словарей,
    группируя их по ключу
    >>> users = [
    ... {'gender': 'female', 'age': 33},
    ... {'gender': 'male', 'age': 20},
    ... ]
    >>> groupby('gender', users)
    {'female': [{'gender': 'female', 'age': 33}],
    'male': [{'gender': 'male', 'age': 20}]}
    >>> groupby('age', users)
    {33: [{'gender': 'female', 'age': 33}],
    20: [{'gender': 'male', 'age': 20}]}
    """
    res = defaultdict(list)
    for i in iterable:
        res[i.get(key, None)].append(i)
    return dict(res)


def chunks(size: int, iterable: Iterable) -> Iterable:
    """Разбивает последовательность на заданные куски
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4)]
    """
    iterator = iter(iterable)
    item = list(islice(iterator, size))
    while item:
        yield item
        item = list(islice(iterator, size))


def first(iterable: Iterable):
    """Возвращает первый элемент в последовательности или None
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0))
    """
    return next(iter(iterable), None)


def last(iterable: Iterable):
    """Возвращает последний элемент в последовательности или None
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0))
    """
    i = None
    for i in iterable:
        pass
    return i
