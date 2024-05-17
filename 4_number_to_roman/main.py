"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    roman_num = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    roman_num_value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    def number_to_roman(self, number: int) -> str:
        if number > 0:
            if number < 4000:
                ans = ""
                number_input = number
                for round in range(len(str(number))):
                    calculate = number_input % (10 ** (round + 1))
                    number_input -= calculate
                    str_roman = ""
                    if calculate != 0:
                        while calculate > 0:
                            index = self.find_closest_index_number(calculate)
                            calculate -= self.roman_num_value[index]
                            str_roman += self.roman_num[index]
                    ans = str_roman + ans
                return ans
            else:
                return "input can not be greater than 4000"
        else:
            return "number can not less than 0"


    def find_closest_index_number(self, number: int) -> int:
        index = max(filter(lambda i: self.roman_num_value[i] <= number, range(len(self.roman_num_value))))
        return index

    def get_input(self) -> int:
        try:
            number_input = int(input("input = "))
            return number_input
        except:
            print("input is not int")
            exit()

solution = Solution()
number_input = solution.get_input()
print("output = ", solution.number_to_roman(number_input))
