class Numberus:
    roman_digit_weights = {
        "i": 1,
        "v": 5,
        "x": 10,
        "l": 50,
        "c": 100,
        "m": 1000
    }

    def __init__(self,roman_number_as_string):
        self.roman_number_as_string = roman_number_as_string.lower()

    def to_decimal(self):
        prev_value = 0
        total_value = 0
        for roman_digit in self.roman_number_as_string:
            current_value = self.roman_digit_weights[roman_digit]

            if prev_value < current_value:
                total_value -= prev_value
                current_value -= prev_value

            prev_value = current_value
            total_value += current_value
        return total_value

numberus = Numberus("mmxx")
print( numberus.to_decimal() )