"""The most basic test."""

from project_slug.minimal import hello_world


def test_hello_world():
    assert "Hello World!" == hello_world()
