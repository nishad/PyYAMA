import pytest
import yama
from yama import core


def test_expand_namespace():
    assert core.expand_namespace
    (
        {"ex": "http://example.com/"}, "ex:Example"
    ) == "http://example.com/Example"


def test_yama_class_init():
    yama_doc = yama.YAMA("samples/yama_my_book_case.yaml")
    assert isinstance(yama_doc, yama.core.YAMA)


def test_yama_class_version():
    yama_doc = yama.YAMA("samples/yama_my_book_case.yaml")
    assert str(yama_doc.version()) == "0.1.0"
