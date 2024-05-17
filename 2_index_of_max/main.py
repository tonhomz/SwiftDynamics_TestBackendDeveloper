"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if self.check_list_input(numbers) == False:
            return "list can not blank"
        else:
            max_index = numbers.index(max(numbers))
            return max_index
    
    def check_list_input(self, numbers: list) -> list[int] | bool:
        # check input not blank and input is number
        if (not numbers) or (not all(isinstance(item, int) for item in numbers)):
            return False
        else:
            list_number = [int(item) for item in numbers]
            return list_number
        
    def get_input(self) -> list:
        try:
            list_input = input("input = ")
            list_input = list(eval(list_input))
            return list_input
        except:
            print("input is not list")
            exit()

solution = Solution()
list_input = solution.get_input()
print("output = ", solution.find_max_index(list_input))
