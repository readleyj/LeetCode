class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        num_students = 0

        for start_time, end_time in zip(startTime, endTime):
            num_students += start_time <= queryTime <= end_time

        return num_students
