
class GenerateFibonacci:

    try:
        def generate(self):
            num1 = 1
            num2 = 2
            sum = 0

            length = int(input("Enter the length og series :: "))
            series = []
            series.append(num1)
            series.append(num2)
            while length > 0:
                sum = num1+num2
                num1 = num2
                num2 = sum
                series.append(sum)
                length = length - 1

            print(series)
    except Exception:
        print("Exception Occured")