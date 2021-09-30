class Even:
    def very_even(self, number):
        while number > 9:
            sum_of_nums = 0
            while number > 0:
                sum_of_nums += number % 10
                number = number // 10
            number = sum_of_nums
        if number % 2 == 0:
            return "четное"
        else:
            return "нечетное"


