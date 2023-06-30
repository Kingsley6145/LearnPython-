class Temperature:
    @staticmethod
    def convert_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    @staticmethod
    def convert_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
# Create a Temperature class
temp = Temperature()

# Convert Celsius to Fahrenheit
temp.convert_to_fahrenheit(27)

# Convert Fahrenheit to Celsius
temp.convert_to_celsius(88)
