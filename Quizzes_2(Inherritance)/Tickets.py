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


class Categories:
    """
    Preferential categories.

    This class include preferential categories and allows adding new category.
    """
    categories = {
        'Pensioner': 0.3,
        'Invalid': 0.35,
        'Student': 0.5
    }

    def print_categories(self):
        """
        Printing list of categories.
        """
        a = ''
        for i in self.categories.items():
            a += str(i) + '\n'
        return a


class Ticket:
    """
    The same as a regular ticket
    """

    def __init__(self, unique_number=None,
                 price=None, category=None):
        """
        Constructor.

        Used to set a unique number and price.
        :param unique_number: unique ID of ticket
        :param price: price of ticket
        :param category: category
        """

        if type(unique_number) == str and type(price) == float:
            self._unique_number = unique_number
            self._price = price
            self._category = category
        else:
            raise TypeError

    def get_price(self):
        """
        Price.

        :return: a price of ticket
        """
        self._price *= Categories.categories[self._category]
        return 'The price of current ticket is: ' + str(self._price)

    def ticket_as_string(self):
        """
        Information.

        :return: information about ticket in string-form.
        """
        self._price *= Categories.categories[self._category]
        return 'Ticket number: {}\n' \
               'Ticket price: {}'.format(self._unique_number, self._price)

    def ticket_by_number(self):
        """
        Information.

        This method used to print information about ticket
        :return: Unique number, Price, Ticket name
        """
        self._price *= Categories.categories[self._category]
        return 'Unique number: ' + self._unique_number + '\n' + \
               'Price: ' + str(self._price) + '\n' + \
               'Ticket name: ' + str(self.__class__.__name__)


class TicketDataBase(Ticket):
    all_tickets = {}

    def print_info(self):
        a = ''
        for i in self.all_tickets.items():
            a += str(i) + '\n'
        return a

    def add_to_base(self):
        """
        Add new key-value to data base
        """

        self.all_tickets.update({'id' + str(Ticket()._unique_number):
                                 'price: ' + str(Ticket()._price)})


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
        construct = input('Do you want add a new ticket ?[y/n]\n'
                          '>>>')
        price = 100.0
        unique_number = 'id' + str(uuid4().hex)
        category = input('Choose a category, to which you belong: \n' +
                         str(Categories().print_categories()))
        if construct == 'y':
            unique_number_new = input('Choose a unique number for ticket: \n'
                                      '>>> {}'.format('id'))
            if 'id' + unique_number_new in TicketDataBase.all_tickets.keys():
                print('This number already exist!\n')
                continue
            else:
                ticket = Ticket(unique_number_new, price, category)
                TicketDataBase().add_to_base()

                print('Your ticket successfully added! ')
            see = input('Do you want to print ticket by number ?[y/n]')
            if see == 'y':
                print(ticket.ticket_by_number())
        elif construct == 'n':
            try:
                a = input('Please, input a date of event'
                          ' in [dd/mm/yy] format: \n'
                          '>>> ').split('/')
                date_of_event = datetime.date(datetime(int(a[2]),
                                                       int(a[1]), int(a[0])))

                date = input('Input a date, when you bought a '
                             'ticket in [dd/mm/yy] format: \n'
                             '>>> ').split('/')
                day, month, year = int(date[0]), int(date[1]), int(date[2])

                date_of_purchase = datetime.date(datetime(year, month, day))
            except ValueError:
                print('Date is incorrect!')
                continue
            else:
                day_delta = str(date_of_event -
                                date_of_purchase).split()
                # difference between day of event
                # and day, when ticket
                # was purchased .

                if int(day_delta[0]) >= 60:
                    ticket = Advanced(unique_number, price, category)
                elif int(day_delta[0]) <= 10:
                    ticket = Late(unique_number, price, category)

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

        if input('Press <Enter> to continue work with program...') != '':
            break


if __name__ == '__main__':
    main()