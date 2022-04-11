#Program 1: Modify the program below by adding two conversion methods - Fahrenheit to Celsius and Kelvin to Celsius (50 points)


def main():

  class TemperatureConversion:
    def __init__(self, temp = 1):
      self._temp = temp

  class CelsiusToFahrenheit(TemperatureConversion):
    def conversion(self):
      return (self._temp * 9)/5 + 32

  class CelsiusToKelvin(TemperatureConversion):
    def conversion(self):
      return self._temp + 273.15

  tempInCelsius = float(input("Enter the temperature in Celsius: "))
  convert = CelsiusToKelvin(tempInCelsius)
  print(str(convert.conversion()) + " Kelvin")
  convert = CelsiusToFahrenheit(tempInCelsius)
  print(str(convert.conversion()) + " Fahrenheit")


  #Add - Fahrenheit to Celsius and Kelvin to Celsius (Solution)

  class FahrenheitToCelsius(TemperatureConversion):
    def conversion(self):
      return (self._temp - 32) * 5/9

  tempInFahrenheit = float(input("\nEnter the temperature in Fahrenheit: "))
  convert = FahrenheitToCelsius(tempInFahrenheit)
  result = round(convert.conversion(), 2)
  print(f"{str(result)} Celsius")

  class KelvinToCelsius(TemperatureConversion):
    def conversion(self):
      return (self._temp - 273.15)

  tempInKelvin = float(input("\nEnter the temperature in Kelvin: "))
  convert = KelvinToCelsius(tempInKelvin)
  result = round(convert.conversion(), 2)
  print(f"{str(result)} Celsius")


main()


#Program 2. Create a program to produce the interface:
# (Hint: After typing your full name in the first entry field widget,
# the bottom entry field will show your full name after clicking the button - 50 points)

from tkinter import *


class MidtermWindow:

    def __init__(self, window):
        self.input = Label(window, text='Enter your fullname:', fg='red')
        self.output = Button(window, text='Click here to display your Fullname', fg='red')
        self.i1 = Entry(window, width=21, bd=4, font =('Helvetica', 16))
        self.o1 = Entry(window, width=21, bd=4, font =('Helvetica', 16))
        self.input.place(x=50, y=100)
        self.i1.place(x=300, y=150)
        self.output.place(x=50, y=150)
        self.o1.place(x=300, y=100)





window = Tk()
mywin = MidtermWindow(window)
window.title('Midterm in OOP')
window.geometry("600x300+10+10")

window.mainloop()
