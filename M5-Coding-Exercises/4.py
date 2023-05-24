class Median:
  def calculate_median(self, num1, num2, num3=None, num4=None, num5=None):
    numbers = [num1, num2]
    if num3 is not None:
      numbers.append(num3)
    if num4 is not None:
      numbers.append(num4)
    if num5 is not None:
      numbers.append(num5)

    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
      mida = numbers[length // 2 - 1]
      midb = numbers[length // 2]
      median = (mida + midb) / 2
    else:
        median = numbers[length // 2]

    return median

m = Median()
print(m.calculate_median(3, 5, 1, 4, 2))
print(m.calculate_median(8, 6, 4, 2))
print(m.calculate_median(9, 3, 7))
print(m.calculate_median(5, 2))
