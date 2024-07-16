from lib.todo import *

"""
test that a todo can be created and is marked False
"""
def test_todo_false():
    todo = Todo("task")
    assert ["task", False] == [todo.task, todo.complete]

"""
test that a todo can be marked complete
"""
def test_todo_complete():
    todo = Todo("task")
    todo.mark_complete()
    assert todo.complete == True