from lib.diary import *

'''
test if diary can be created and entries can be added
'''
def test_diary_creation():
    diary = Diary()
    diary.add_entry("text 1")
    diary.add_entry("text 2")
    result_1 = diary.read_entry(0)
    result_2 = diary.read_entry(1)
    assert [result_1, result_2] == ["text 1", "text 2"]

'''
tests to see if diary entries can be filtered by time and reading speed
'''
def test_diary_non_too_long():
    diary = Diary()
    diary.add_entry("text 1")
    diary.add_entry("text 2")
    result = diary.sort_entries(1, 2)
    assert result == ["text 1", "text 2"]

def test_diary_some_too_long():
    diary = Diary()
    diary.add_entry("text 1")
    diary.add_entry("clearly this text is far too long and the average reader would stand absolutely no chance whatsoever to read this in the incredibly small time frame and reading speed by which this test is being run, which is rather unfortunate that they may never perceive the majesty of such a long and verbose text conjured up for such a pointless existence, that is to be tested against once and long forgotten")
    result = diary.sort_entries(2, 10)
    assert result == ["text 1"]

def test_diary_all_too_long():
    diary = Diary()
    diary.add_entry("I don't want to type as much as the other test")
    diary.add_entry("So I'll just make the reading speed really small")
    result = diary.sort_entries(2,1)
    assert result == []
    
'''
tests if phone numbers can be added and listed
'''

def test_diary_add_and_list_phone_numbers():
    diary = Diary()
    diary.add_phone_number("phone number 1")
    diary.add_phone_number("phone number 2")
    result = diary.list_phone_numbers()
    assert result == ["phone number 1", "phone number 2"]