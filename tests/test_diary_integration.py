from lib.diary import *

"""
checks that diary can use all the methods from todo_list
"""
def test_adds_todos():
    diary = Diary()
    todo_1 = Todo("task_1")
    todo_2 = Todo("task_2")
    diary.todo_add(todo_1)
    diary.todo_add(todo_2)
    assert [todo_1, todo_2] == diary.todo_list.list

"""
adds a complete and incomplete todo to a todolist and checks which are incomplete
"""
def test_todo_list_incompletes():
    diary = Diary()
    todo_1 = Todo("task_1")
    todo_2 = Todo("task_2")
    diary.todo_add(todo_1)
    diary.todo_add(todo_2)
    diary.todo_list.list[0].mark_complete()
    result = diary.todo_incomplete()
    assert result == [todo_2]

"""
adds a complete and incomplete todo to a todolist and checks which are complete
"""
def test_todo_list_incompletes():
    diary = Diary()
    todo_1 = Todo("task_1")
    todo_2 = Todo("task_2")
    diary.todo_add(todo_1)
    diary.todo_add(todo_2)
    diary.todo_list.list[0].mark_complete()
    result = diary.todo_complete()
    assert result == [todo_1]

"""
creates a todo list and checks that give_up completes all todos
"""
def test_todo_list_incompletes():
    diary = Diary()
    todo_1 = Todo("task_1")
    todo_2 = Todo("task_2")
    diary.todo_add(todo_1)
    diary.todo_add(todo_2)
    diary.todo_list.list[0].mark_complete()
    diary.todo_give_up()
    result = diary.todo_complete()
    assert result == [todo_1, todo_2]