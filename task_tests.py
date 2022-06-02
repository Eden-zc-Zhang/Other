from task_functions import *

test_list = list_menu = {
    "A": "all tasks",
    "C": "completed tasks",
    "I": "incomplete tasks"
}

assert get_written_date(["01", "02", "2022"]) == 'January 2, 2022'
assert get_written_date(["01", "12", "1970"]) == 'January 12, 1970'
assert get_written_date(["04", "14", "2020"]) == 'April 14, 2020'
assert get_written_date(["06", "19", "2000"]) == 'June 19, 2000'

assert