"""The most basic test."""

from {{ cookiecutter.project_slug }}.library import hello_world

def test_hello_world():
    assert "Hello World!" == hello_world()