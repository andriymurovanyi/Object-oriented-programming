# Murovanyi Andrey.KNIT16-A
# Create a class Rectangle with attributes length and width,
# each of which defaults to 1. Provide methods that calculate
# the perimeter and the area of the rectangle. Also, provide
# setter and getter for the length and width attributes. The
# setter should verify that length and width are each
# floating-point numbers larger than 0.0 and less than 20.0.
from os import system


class Rectangle:
    __slots__ = ['_length', '_width']

    def __init__(self, length=1.0, width=1.0):
        """
        Constructor.
        
        Initialize length and width variables
        :param length: length of rectangle
        :param width: width of rectangle
        """
        self._length = length
        self._width = width

    def perimeter(self):
        """
        Perimeter.
        
        Calculate a perimeter of rectangle
        :return: perimeter value
        """
        return 2 * (self._length + self._width)

    def area(self):
        """
        Area.
        
        Calculate an area of rectangle
        :return: area value
        """
        return self._width * self._length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        """
        Setter.
        
        Check if values, which you input, satisfied condition
        """
        assert 0 < width < 20 and isinstance(width, float)
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        """
        Setter.

        Check if values, which you input, satisfied condition
        """
        assert 0 < length < 20 and isinstance(length, float)
        self._length = length


def main():
    flag = True
    while flag:
        how = input('Do you want to use default values?[y/n]\n'
                    '>>> ')
        if how == 'y':
            figure = Rectangle()
            print(figure.perimeter())
        elif how == 'n':
            figure = Rectangle()
            while True:
                try:
                    figure.width = float(input('Input a width:\n'
                                         '>>> '))
                    figure.length = float(input('Input a length:\n'
                                          '>>> '))
                except ValueError:
                    print('Some ERROR in your input occured\n')
                    continue
                except AssertionError:
                    print('ERROR! Value not in range or not float!\n')
                    continue
                else:
                    break
            perimeter = figure.perimeter()
            area = figure.area()
            print('The perimeter of Rectangle is [{}]\n'
                  'The area of Rectangle is [{}]'.format(perimeter, area))
        else:
            print('You must make a choice!\n')
            continue
        if input('Press Enter key to continue...') != '':
            system('cls')
            flag = False
            break


if __name__ == '__main__':
    main()

