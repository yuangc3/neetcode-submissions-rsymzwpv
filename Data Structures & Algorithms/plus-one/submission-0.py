class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digit = []
        for n in digits:
            new_digit.append(str(n))
        number_string = "".join(new_digit)
        number = int(number_string) + 1

        return [int(n) for n in str(number)]