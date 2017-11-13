# Murovanyi Andrey.KNIT16-A
# Issue:
# Write a program for selling tickets to IT-events. Each ticket has a unique
# number and a price. There are four types of tickets: regular ticket,
# advance ticket (purchased 60 or more days before the event),
# late ticket (purchased fewer than 10 days
# before the event) and student ticket.
# Additional information:
# * advance ticket - discount 40% of the regular ticket price;
# * student ticket - discount 50% of the regular ticket price;
# * late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# * the ability to construct a ticket by number;
# * the ability to ask for a ticket’s price;
# * the ability to print a ticket as a String.

# Let's suppose, that the IT-event will be today.
from datetime import datetime
from uuid import uuid4
import json


def open_file():
    with open('Data.json', 'r') as data:
        f = json.load(data)
    return f


class Ticket:
    """
    The same as a regular ticket
    """

    def __init__(self, unique_number=None,
                 price=None, coefficient=None):
        """
        Constructor.
        Used to set a unique number and price.
        :param unique_number: unique ID of ticket
        :param price: price of ticket
        :param coefficient: coefficient of preferential category
        """
        self._unique_number = unique_number
        self._price = price
        self._coefficient = coefficient

    def get_price(self):
        """
        Price.
        :return: a price of ticket
        """
        self._price *= self._coefficient
        return 'The price of current ticket is: ' + str(self._price)

    def ticket_as_string(self):
        """
        Information.
        :return: information about ticket in string-form.
        """
        self._price *= self._coefficient
        return 'Ticket number: {}\n' \
               'Ticket price: {}'.format(self._unique_number, self._price)

    def add_to_base(self):
        """
        Add new key-value to data base
        """

        TicketDataBase().all_tickets.update({'id: ' + str(self._unique_number):
                                             'price: ' + str(self._price)})


class TicketDataBase(Ticket):
    all_tickets = {}

    def print_info(self):
        a = ''
        for i in self.all_tickets.items():
            a += str(i) + '\n'
        return a


class Advanced(Ticket):
    """
    Class for Advanced ticket.
    """

    unique_number = 'id' + str(uuid4().hex)

    def __init__(self, unique_number=None, price=None, category=None):
        price_advanced = price - price * 0.4  # 0.4 - 40% Discount for advanced ticket
        super().__init__(unique_number, price_advanced, category)


class Student(Ticket):
    """
    Class for student ticket.
    """

    unique_number = 'id' + str(uuid4().hex)

    def __init__(self, unique_number, price, category):
        price_student = price - price * 0.5
        super().__init__(unique_number, price_student, category)


class Late(Ticket):
    """
    Class for late ticket.
    """
    unique_number = 'id' + str(uuid4().hex)

    def __init__(self, unique_number=None, price=None, category=None):
        price_late = price + price * 0.1  # 0.1 (+10% additional to regular
        # ticket price.)
        super().__init__(unique_number, price_late, category)


def main():
    """
    A main-function, which allows to test this class
    """
    while True:
        see = input('Do you want to print ticket by number ?[y/n]\n'
                    '>>> ')
        if see == 'y':
            number = input('Input a number of ticket: \n'
                           '>>> ')
            if 'id: ' + number in TicketDataBase().all_tickets.keys():
                print(ticket.ticket_as_string())
            else:
                print('This ticket is absent!')
        elif see == 'n':
            try:
                my_file = open_file()['IT-events']
                for i in my_file:
                    print(i)
                choice = input('Choose the IT-event in list higher: ')
                print('There are following preferential categories on this event: ')
                for i in my_file[choice]['categories']:
                    print('* ' + str(i))
                category = input('Choose a category, to which you belong: \n'
                                 '>>> ')
                coefficient = my_file[choice]['categories'][category]
                price = my_file[choice]['price']
                unique_number = str(uuid4().hex)
                f = my_file[choice]['date']
                date_of_event = datetime.date(datetime.strptime(f, '%d.%m.%y'))
                date = input('Input a date, when you bought a '
                             'ticket in [dd.mm.yy] format: \n'
                             '>>> ').split('.')
                day, month, year = int(date[0]), int(date[1]), int(date[2])

                date_of_purchase = datetime.date(datetime(year, month, day))

                day_delta = str(date_of_event -
                                date_of_purchase).split()

                # difference between day of event
                # and day, when ticket
                # was purchased .
            except KeyError:
                print('No such category!')
                continue
            except IndexError:
                print('Invalid format of date!')
                continue

            if int(day_delta[0]) >= 60:
                ticket = Advanced(unique_number, price, coefficient)
            elif int(day_delta[0]) <= 10:
                ticket = Late(unique_number, price, coefficient)
            ticket.add_to_base()

            action = input('What you want to do? (see a list below)\n'
                           '<1 - ask a ticket price>\n'
                           '<2 - print ticket as string>\n'
                           '>>> ')
            if action == '1':
                print(ticket.get_price())
            elif action == '2':
                print(ticket.ticket_as_string())
            else:
                print('Please, make you\'re choice')
        else:
            print('Please, make you\'re choice!')
            continue

        if input('Press <Enter> to continue work with program...') != '':
            break

if __name__ == '__main__':
    main()
