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
from datetime import datetime, timedelta
from random import randrange


class TicketDataBase:
    all_tickets = {}  # Database of all tickets

    def print_info(self):
        a = ''
        for i in self.all_tickets.items():
            a += str(i) + '\n'
        return a


class Ticket:
    """
    The same as a regular ticket
    """

    def __init__(self, unique_number='id' + str(randrange(1, 10000)),
                 price=100.0, isstudent=False):
        """
        Constructor.
        
        Used to set a unique number and price.
        :param unique_number: unique ID of ticket
        :param price: price of ticket
        :param isstudent: bool variable, which equal to 'True' if
        person is student.
        """
        if type(unique_number) == str and type(price) == float:
            self._unique_number = unique_number
            self._price = price
        else:
            raise TypeError
        self.isstudent = isstudent

    def add_to_base(self):
        """
        Add new key-value to data base

        """
        TicketDataBase.all_tickets.update({'id' + self._unique_number:
                                           'price: ' + str(self._price)})

    def get_price(self):
        """
        Price.
        
        :return: a price of ticket
        """
        if self.isstudent:
            self._price *= 0.5

        return 'The price of current ticket is: ' + str(self._price)

    def ticket_as_string(self):
        """
        Information.
        
        :return: information about ticket in string-form.
        """
        return 'Ticket number: {}\n' \
               'Ticket price: {}'.format(self._unique_number, self._price)

    def ticket_by_number(self):
        if 'id' + self._unique_number in TicketDataBase.all_tickets.keys():
            return 'Unique number: ' + self._unique_number + \
                   'Price: ' + str(self._price)


class Advanced(Ticket):
    discount = Ticket()._price * 0.4  # 0.4 - 40% Discount for advanced ticket
    price_advanced = Ticket()._price - discount
    unique_number = 'id' + str(randrange(1, 10000))

    def __init__(self, isstudent=False):
        super().__init__(self.unique_number, self.price_advanced, isstudent)


class Student(Ticket):
    discount = Ticket()._price * 50 / 100
    unique_number = 'id' + str(randrange(1, 10000))
    price_student = Ticket()._price - discount

    def __init__(self):
        super().__init__(self.unique_number, self.price_student)


class Late(Ticket):
    price_late = Ticket()._price * 1.1  # 1.1 - 110%(+10% additional
                                        # to regular ticket price)
    unique_number = 'id' + str(randrange(1, 10000))

    def __init__(self, isstudent=False):
        super().__init__(self.unique_number, self.price_late, isstudent)


def main():
    """
    A main-function, which allows to test this class
    """
    while True:
        construct = input('Do you want add a new ticket ?[y/n]\n'
                          '>>>')
        if construct == 'y':
            ticket = Ticket()
            unique_number = input('Choose a unique number for ticket: \n'
                                  '>>> {}'.format('id'))
            if 'id' + unique_number in TicketDataBase.all_tickets.keys():
                print('This number already exist!\n')
                continue
            else:
                ticket = Ticket(unique_number)
                ticket.add_to_base()

                print('Your ticket successfully added! ')
            see = input('Do you want to print ticket by number ?[y/n]')
            if see == 'y':
                print(ticket.ticket_by_number())

        try:
            date_of_event = datetime.date(datetime.now())
            date = input('Input a date, when you bought a '
                         'ticket in [dd/mm/yy] format: \n'
                         '>>> ').split('.')
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
            ask = input('Are you student ?[y/n]')
            isstudent = bool
            if ask == 'y':
                isstudent = True
                if int(day_delta[0]) >= 60:
                    ticket = Advanced(isstudent)
                elif int(day_delta[0]) <= 10:
                    ticket = Late(isstudent)
                ticket.add_to_base()
            elif ask == 'n':
                if int(day_delta[0]) >= 60:
                    ticket = Advanced()
                elif int(day_delta[0]) <= 10:
                    ticket = Late()
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

        if input('Press <Enter> to continue work with program...') != '':
            break


if __name__ == '__main__':
    main()
