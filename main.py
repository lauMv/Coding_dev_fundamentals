# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""Write a short Python script, that takes two numbers values, where one of them is
the hours worked by employee and the other is the rate, the equation to calculate
the payment is (hours * rate), but if the hours is more than 40 the equation is
(hours * rate + (hours - 40) * rate * 0.5). So we need a script to do this automatically."""


def payment(hour, rate):
    payment = hour * rate
    if hour > 40:
        payment = payment + ((hour - 40) * rate * 0.5)
    return payment



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print("Hours: ")
   hour = int(input())
   print ("Rate: ")
   rate = float(input())
   pay = payment(hour, rate)
   print("Payment: ", pay)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
