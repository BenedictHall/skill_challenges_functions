from lib.todo_list import *

"""
checks that todolist creates an empty list when initialised
"""
def test_todo_list():
    todo_list = TodoList()
    assert [] == todo_list.list