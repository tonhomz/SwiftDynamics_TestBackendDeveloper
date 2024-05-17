"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number >= 0:
            output = self.factorial(number)
            outputZero = self.countZero(output)
            return outputZero
        else:
            return "number can not be negative"

    def factorial(self, number: int) -> int:
        result = 1
        while number > 1:
            result *= number
            number -= 1
        return result
    
    def countZero(self, number: int) -> int:
        count = 0
        while number % 10 == 0:
            count += 1
            number //= 10
        return count
    
    def get_input(self) -> int:
        try:
            inputNumber = int(input("input = "))
            return inputNumber
        except:
            print("input is not int")
            exit()

solution = Solution()
inputNumber = solution.get_input()
print("output = ", solution.find_tailing_zeroes(inputNumber))