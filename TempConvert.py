#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = 80

  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = (tempF - 32) * 5 / 9
  #Output converted temperature.
  print(tempF, "is ", round(tempC, 1), "degrees celsius.")

if __name__ == '__main__':
  main()
