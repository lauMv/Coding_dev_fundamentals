"""Write a short Python script, that takes two numbers values, where one of them is
the hours worked by employee and the other is the rate, the equation to calculate
the payment is (hours * rate), but if the hours is more than 40 the equation is
(hours * rate + (hours - 40) * rate * 0.5). So we need a script to do this automatically."""


def payment(hour, rate):
    payment = hour * rate
    if hour > 40:
        payment = payment + ((hour - 40) * rate * 0.5)
    return round(payment, 2)


def get_employees():
    employees_list= []
    aux = []
    with open("employees.csv") as file:
        for row in file:
            aux.append(row.split(","))
        index_names = aux.pop(0)
        for emp in aux:
            if len(emp)>1:
                employee = [(emp[0]),int(emp[1]), (emp[2]).replace('\n', "")]
                employees_list.append(employee)
    return employees_list


if __name__ == '__main__':
    employees = get_employees()
    print(employees)
    for emp in employees:
        print(emp[0] + "the payment is " + str(payment(emp[1], float(emp[2]))))