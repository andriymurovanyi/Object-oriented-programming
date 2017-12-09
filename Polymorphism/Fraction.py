# Modify the class Rational of ASSIGNMENTS No1 to perform the following tasks:
#  adding two Rational numbers. The result should be stored in reduced form;
#  subtracting two Rational numbers. The result should be stored in reduced form;
#  multiplying two Rational numbers. The result should be stored in reduced form;
#  dividing two Rational numbers. The result should be stored in reduced form;
#  comparison two Rational numbers.
import os


class Rational:
    __slots__ = ['_num', '_den', '_gcd']

    def __init__(self, num=None, den=None):
        """
        Constructor.
        
        Initialize numerator and denominator variables
        :param num: numerator
        :param den: denominator
        """
        if den == 0:
            raise ZeroDivisionError

        if type(num) is int and type(den) is int:
            self._num = num
            self._den = den
        else:
            raise TypeError
        self._gcd = Rational.euklid(num, den)

    def __str__(self):
        """
        Output.
        
        Used to print a reduced fraction in slash-form and in point-floating form.
        :return: fraction in slash-form
        """
        return 'In slash-form: ' + str(self._num // self._gcd) + \
               '/' + str(self._den // self._gcd) + '\n' + \
               'In point-floating-form: ' + str(self._num / self._den)

    @staticmethod
    def euklid(num, den):
        """
        Greatest common division.

        :param num: numerator
        :param den: denominator
        :return: greatest common division 
        """
        if den == 0:
            return num
        else:
            return Rational.euklid(den, num % den)

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self._num * other._den + self._den * other._num,
                            self._den * other._den)
        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self._num * other._den - self._den * other._num,
                            self._den * other._den)
        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self._num * other._num, self._den * other._den)

        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self._num * other._den, self._den * other._num)
        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, Rational):
            firstnum = self._num * other._den
            secondnum = other._num * self._den
            return firstnum == secondnum
        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))

    def __lt__(self, other):
        if isinstance(other, Rational):
            firstnum = self._num * other._den
            secondnum = other._num * self._den
            return firstnum < secondnum
        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))

    def __le__(self, other):
        if isinstance(other, Rational):
            firstnum = self._num * other._den
            secondnum = other._num * self._den
            return firstnum <= secondnum

        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))

    def __gt__(self, other):
        if isinstance(other, Rational):
            firstnum = self._num * other._den
            secondnum = other._num * self._den
            return firstnum > secondnum

        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, Rational):
            firstnum = self._num * other._den
            secondnum = other._num * self._den
            return firstnum >= secondnum
        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))

    def __ne__(self, other):
        if isinstance(other, Rational):
            firstnum = self._num * other._den
            secondnum = other._num * self._den
            return firstnum != secondnum
        raise TypeError('Unsupported operand for '
                        '{} and {}!'.format(Rational.__name__, type(other).__name__))



if __name__ == '__main__':
    try:
        f1 = Rational(2, 5)
        f2 = Rational(2, 5)
    except TypeError:
        print('Unsupported operand for Type {} and {}!'.format(type(Rational), int))

    except ZeroDivisionError:
        print('Division by Zero!')

    else:
        print(f1 + 5)


