"""The most basic test."""

from {{ cookiecutter_project_slug }}.minimal import hello_world

def test_hello_world():
    assert "Hello World!" == hello_world()