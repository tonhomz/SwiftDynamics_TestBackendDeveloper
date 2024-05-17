"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        else:
            length = len(str(number))
            ans = ""
            check_number = 0

            for index in range(length):
                check_number = number % 10
                if length > 1:
                    if index != 0:
                        index %= 6
                        if index % 6 == 0:
                            index = 6

                    if ((index == 0) and (check_number == 1)) or ((check_number == 1) and (index % 6 == 0) and (index != 0)):
                        check_number = 10
                    elif (index == 1) and (check_number == 2):
                        check_number = 11

                    elif (index == 1) and (check_number == 1):
                        check_number = 12
                    elif (check_number == 0):
                        index = 0
                        check_number = 12
                ans = self.convert_number(check_number) + self.convert_round(index) + ans
                number //= 10
            return ans

    def convert_round(self, number: int) -> str:
        round = {
            0: "",
            1: "สิบ",
            2: "ร้อย",
            3: "พัน",
            4: "หมื่น",
            5: "แสน",
            6: "ล้าน"
        }
        return round[number]

    def convert_number(self, number: int) -> str:
        number_text = {
            0: "ศูนย์",
            1: "หนึ่ง",
            2: "สอง",
            3: "สาม",
            4: "สี่",
            5: "ห้า",
            6: "หก",
            7: "เจ็ด",
            8: "แปด",
            9: "เก้า",
            10: "เอ็ด",
            11: "ยี่",
            12: ""
        }
        return number_text[number]

    def get_input(self) -> int:
        try:
            number_input = int(input("input = "))
            return number_input
        except:
            print("input is not int")
            exit()

solution = Solution()
number_input = solution.get_input()
print("output = ", solution.number_to_thai(number_input))
