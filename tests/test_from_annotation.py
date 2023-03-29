from typing import Optional, Union, get_args, get_origin
from unittest.mock import patch

import pytest
from typingref import TypeHinter


@pytest.mark.parametrize("tp", [int, float, str, bool, object])
def test_simple_type(tp):
    th = TypeHinter.from_annotation(tp)
    assert th.type is tp


@pytest.mark.parametrize("tp", [int, float, str, bool, object])
def test_future_annotations(tp):
    th = TypeHinter.from_annotation(tp.__name__)
    assert th.type is tp


@pytest.mark.parametrize("tp", [list[float], Optional[str]])
def test_containers(tp):
    th = TypeHinter.from_annotation(tp)
    assert th.type[get_args(tp)[0]] == tp
    assert th.of_type[0].type is get_args(tp)[0]


def test_unions():
    tp = Union[str, int]
    th = TypeHinter.from_annotation(tp)
    assert th.type is get_origin(tp)
    for index, type_ in enumerate(th.of_type):
        assert type_.type is get_args(tp)[index]


def test_union_with_optionals():
    """Union with one optional basically means that the type is the union is
    optional."""
    tp = Union[Optional[str], Optional[int]]
    th = TypeHinter.from_annotation(tp)
    assert th.type is Optional
    inner = th.of_type[0]
    assert inner.of_type[0].type is str
    assert inner.of_type[1].type is int


def test_nested():
    tp = list[Union[str, int]]
    th = TypeHinter.from_annotation(tp)
    assert th.type is list
    assert th.of_type[0].type is Union
    assert th.of_type[0].of_type[0].type is str
    assert th.of_type[0].of_type[1].type is int


@patch.object(TypeHinter, TypeHinter.from_string.__name__)
def test_fall_back_to_from_string(mock):
    tp = "list[Union[str, int]]"
    TypeHinter.from_annotation(tp)
    assert mock.called


def test_with_fref_ns():
    class MyType:
        ...

    th = TypeHinter.from_annotation("Optional[MyType]", locals())
    assert th.of_type[0].type is MyType


def test_mixed_frefs_and_non_frefs():
    class MyType:
        ...

    def f(a: Optional["MyType"]):
        ...

    annot = Optional["MyType"]
    th = TypeHinter.from_annotation(annot, locals())
    assert th.of_type[0].type is MyType
    annot = f.__annotations__["a"]
    th = TypeHinter.from_annotation(annot, locals())
    assert th.of_type[0].type is MyType
