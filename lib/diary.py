## 1. describe the problem
'''
needs to record experiences
read recorded experiences
select entries to read based on time they have and reading speed
track a todo list along with the diary
keep list of phone numbers
'''

'''
Step 2: design class system
┌──────────────────────┐
│Diary                 │
│entries               │
│todo list             │
│phone numbers         │
│add_entry()           │
│read an entry()       │
│filter_entry_by_time()│
│all_todo_commands()   │
│list_phone_numbers()  │
└──────────────────────┘
  ▲                     
  │ contains one        
  │                     
┌─┴───────────┐         
│todo_list    │         
│already_done │         
└─────────────┘         
  ▲                     
  │ contains multiple   
┌─┴───────────┐         
│todo         │         
│already_done │         
└─────────────┘         
'''
from lib.todo_list import *
from lib.todo import *

class Diary():
    def __init__(self):
        self.entries = []
        self.todo_list = TodoList()
        self.phone_numbers = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def read_entry(self, entry_number):
        return self.entries[entry_number]

    def sort_entries(self, time, reading_speed):
        return list(filter(lambda x: len(x.split()) <= (reading_speed * time), self.entries))

    def todo_add(self, todo):
        self.todo_list.add(todo)

    def todo_incomplete(self):
        return self.todo_list.incomplete()

    def todo_complete(self):
        return self.todo_list.complete()

    def todo_give_up(self):
        self.todo_list.give_up()

    def add_phone_number(self, number):
        self.phone_numbers.append(number)

    def list_phone_numbers(self):
        return self.phone_numbers