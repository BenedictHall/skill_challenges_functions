from lib.todo import *
from lib.todo_list import *

"""
adds two todos to a todolist
"""
def test_adds_todos():
    todo_list = TodoList()
    todo_1 = Todo("task_1")
    todo_2 = Todo("task_2")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert [todo_1, todo_2] == todo_list.list

"""
adds a complete and incomplete todo to a todolist and checks which are incomplete
"""
def test_todo_list_incompletes():
    todo_list = TodoList()
    todo_1 = Todo("task_1")
    todo_2 = Todo("task_2")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.list[0].mark_complete()
    result = todo_list.incomplete()
    assert result == [todo_2]

"""
adds a complete and incomplete todo to a todolist and checks which are complete
"""
def test_todo_list_incompletes():
    todo_list = TodoList()
    todo_1 = Todo("task_1")
    todo_2 = Todo("task_2")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.list[0].mark_complete()
    result = todo_list.complete()
    assert result == [todo_1]

"""
creates a todo list and checks that give_up completes all todos
"""
def test_todo_list_incompletes():
    todo_list = TodoList()
    todo_1 = Todo("task_1")
    todo_2 = Todo("task_2")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.list[0].mark_complete()
    todo_list.give_up()
    result = todo_list.complete()
    assert result == [todo_1, todo_2]