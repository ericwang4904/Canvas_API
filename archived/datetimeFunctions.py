import datetime as dt
import logging

class datetimeFunctions:
    def __init__(self):
        pass
    def return_block_time(self, block):
        TIME = {
            1: (dt.time(8,55), dt.time(10,10)),
            2: (dt.time(10,15), dt.time(11,30)),
            3: (dt.time(12,35), dt.time(13,50)),
            0: (dt.time(13,55), dt.time(15,10))
        }

        return TIME[block % 4]

    def return_offset_from_block(self, block):
        match block:
            case 1|2|3|4:
                return 1
            case 5|6|7|8:
                return 2
            case _:
                logging.error(f"Invalid block number {block} used as input!")
                return 0

    def set_due_date(self, sunday_date: dt.date, block, is_prime_day: bool, due_type='custom', custom_time=dt.time(23, 59, 59), class_offset=dt.timedelta(minutes=0)) -> dt.datetime:
        due_date = sunday_date
        due_date += dt.timedelta(days=self.return_offset_from_block(block))
        if is_prime_day:
            due_date += dt.timedelta(days=3)

        
        if due_type == "before_class":
            due_time = self.return_block_time(block)[0]
            return dt.datetime.combine(due_date, due_time) + class_offset
        elif due_type == "after_class":
            due_time = self.return_block_time(block)[1]
            return dt.datetime.combine(due_date, due_time) + class_offset
        elif due_type == "custom":
            due_time = custom_time
            return dt.datetime.combine(due_date, due_time)
        
        logging.error(f"Invalid due_type {due_type} used as input!")

    def find_sunday_of_assignment(self, assignment, block, is_prime_day: bool) -> dt.date:
        assignment_datetime_string = assignment['due_at']
        assignment_datetime = dt.datetime.fromisoformat(assignment_datetime_string)
        
        sunday_date = assignment_datetime.date()
        sunday_date -= dt.timedelta(days=self.return_offset_from_block(block))
        
        if is_prime_day:
            sunday_date -= dt.timedelta(days=3)

        return sunday_date

    def return_tzinfo_from_assignment(self, assignment):
        assignment_datetime_string = assignment['due_at']
        assignment_datetime = dt.datetime.fromisoformat(assignment_datetime_string)

        return assignment_datetime.tzinfo
        
