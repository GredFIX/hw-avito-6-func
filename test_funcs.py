import pytest

from issue import ilen, flatten, distinct, first, last


@pytest.mark.parametrize(
    'given, expected',
    [
        ([], 0),
        ([1, 2, 3, 4, 5], 5),
        (("hello world"), 11),
        ((1, 2, 3), 3),
    ]
)
def test_ilen(given, expected):
    assert ilen(given) == expected


@pytest.mark.parametrize(
    'given, expected',
    [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([1, [2], [3, [4]]], [1, 2, 3, 4]),
        (
            [[[{1, 2, 3}, 4], 5], 6], [1, 2, 3, 4, 5, 6]
        )
    ]
)
def test_flatten(given, expected):
    assert list(flatten(given)) == expected


@pytest.mark.parametrize(
    'given, expected',
    [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ((1 for x in range(10)), [1]),
        ([4, 1, 1, 2, 3, 2], [4, 1, 2, 3]),
    ]
)
def test_distinct(given, expected):
    assert list(distinct(given)) == expected


@pytest.mark.parametrize(
    'given, expected',
    [
        ([], None),
        ([1, 2, 3], 1),
        ("string", "s"),
        ((x for x in range(10)), 0),
    ]
)
def test_first(given, expected):
    assert first(given) == expected


@pytest.mark.parametrize(
    'given, expected',
    [
        ([], None),
        ([1, 2, 3], 3),
        ("string", "g"),
        ((x for x in range(10)), 9),
    ]
)
def test_last(given, expected):
    assert last(given) == expected
