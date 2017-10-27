# Murovanyi Andrey.KNIT16-A
# Create a class called Rational for performing arithmetic with fractions. Write a
# program to test your class. Use integer variables to represent the private data of the class –
# the numerator and the denominator. Provide a __init__() method that enables an object of
# this class to be initialized when it’s declared. The __init__() should contain default
# parameter values in case no initializers are provided and should store the fraction in
# reduced form. For example, the fraction 2/4 would be stored in the object as 1 in the
# numerator and 2 in the denominator. Provide public methods that perform each of the
# following tasks:
# - printing Rational numbers in the form a/b, where a is the numerator and b is the
# denominator.
# - printing Rational numbers in floating-point format.
import os


class Rational:
    __slots__ = ['_num', '_den']

    def __init__(self, num=3, den=6):
        """
        Constructor.
        
        Initialize numerator and denominator variables
        :param num: numerator
        :param den: denominator
        """
        self._num = num
        self._den = den
        if den == 0:
            raise ZeroDivisionError

    def __str__(self):
        """
        Output.
        
        Used to print a reduced fraction in slash-form
        :return: fraction in slash-form
        """
        gcd = self.euklid(self._num, self._den)
        return str(self._num // gcd) + '/' + str(self._den // gcd)

    def floating_form(self):
        """
        Output.
        
        Used to print a fraction in point-floating form
        :return: fraction in point floating form
        """
        return self._num / self._den

    def euklid(self, num, den):
        """
        Greatest common division.
        
        :param num: numerator
        :param den: denominator
        :return: greatest common division 
        """
        if den == 0:
            return num
        else:
            return self.euklid(den, num % den)


def main():
    while True:
        ask = input('Do you want to use default values?[y/n]\n'
                    '>>> ')
        if ask == 'y':
            print('Resulting fraction is: {}\n'
                  'In point-floating form: {}\n'.format(Rational(),
                                                        Rational().floating_form()))
        elif ask == 'n':
            try:
                fraction = input('Input a fraction in slash-form:\n'
                                 '>>> ').split('/')
                num = int(fraction[0])
                den = int(fraction[1])
                f = Rational(num, den)
            except ValueError:
                print('ERROR! Incorrect input!\n')
                continue
            except ZeroDivisionError:
                print('ERROR! Division by zero\n')
                continue
            else:
                print('Resulting fraction is: {}\n'
                      'In point-floating form: {}\n'.format(f, f.floating_form()))
        else:
            print('Please, make your choice')
            continue
        if input('Press Enter key to continue...') != '':
            os.system('cls')
            break

if __name__ == '__main__':
    main()
