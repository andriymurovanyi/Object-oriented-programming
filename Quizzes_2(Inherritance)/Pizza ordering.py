# Murovanyi Andrey.KNIT16-A
# Issue: Pizzeria offers pizza-of-the-day for business lunch.
#  The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers.
# They don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day.
# Write a program that will form orders from customers.
import datetime


class AllIngredients:
    all_ingredients = {
        'cheese': 3.0,
        'basil': 2.5,
        'tomatoes': 2.0,
        'olives': 5.0,
        'anchovies': 5.5,
        'parmesan': 7.0,
        'oregano': 4.0,
        'mozzarella': 5.0,
        'garlic': 2.0,
        'artichokes': 5.0,
        'peperoni': 4.0,
        'salami': 6.5,
        'pineapple': 10.0
    }  # this dict includes all ingredients, which also

    # can be added to pizza as extra ingredient

    def print_all_ingredients(self):
        """
        Price list.
        
        :return: list of all ingredients
        """
        a = ''
        for i in self.all_ingredients.items():
            a += str(i) + '\n'
        return a


class Pizza:
    """
    It's a base class.
    """
    def __init__(self, ingredients=None,
                 cost=None, extra_ingredients=None):
        """
        Constructor.
        
        Used to initialize ingredients, cost and extra ingredients
        :param ingredients: list of ingredients
        :param cost: cost of pizza
        :param extra_ingredients: list of extra ingredients.
        """
        self.ingredients = ingredients
        self.coast = cost
        self.extra_ingredients = extra_ingredients

    def get_ingredients(self):
        """
        Ingredients.
        
        :return: list of pizza ingredients.
        """
        return self.ingredients

    def get_extra_ingredients(self):
        """
        Extra ingredients.
        
        :return: list of all pizza extra ingredients
        """
        for i in self.extra_ingredients:
            if i in AllIngredients.all_ingredients.keys():
                return self.extra_ingredients
            else:
                raise KeyError

    def get_cost(self):
        """
        Cost.
        
        Calculate summary cost of pizza and all extra ingredients.
        :return: 
        """
        for i in range(len(self.extra_ingredients)):
            self.cost += \
                AllIngredients.all_ingredients[self.extra_ingredients[i]]
        return self.cost

    @staticmethod
    def pizza_of_day_the_day():
        """
        Pizza of the day.

        This method used to identify pizza of the day.
        :return: pizza of the day
        """
        day = {0: 'Margarita', 1: 'Neapolitano',
               2: 'Capricciosa', 3: 'Diavola',
               4: 'Hawaii', 5: 'Marenara', 6: 'Pimaavera'}
        return day[datetime.date.today().weekday()]


class Margherita(Pizza):
    cost = 35.0
    ingredients = ['cheese', 'tomatoes', 'basil', 'olives']

    def __init__(self, extra_ingredients):
        super().__init__(self.ingredients, self.cost, extra_ingredients)


class Neapolitano(Pizza):
    cost = 50.0
    ingredients = ['parmesan', 'tomatoes', 'anchovies', 'basil', 'oregano']

    def __init__(self, extra_ingredients):
        super().__init__(self.ingredients, self.cost, extra_ingredients)


class Capricciosa(Pizza):
    cost = 45.0
    ingredients = ['tomatoes', 'mozzarella', 'artichokes', 'olives']

    def __init__(self, extra_ingredients):
        super().__init__(self.ingredients, self.cost, extra_ingredients)


class Diavola(Pizza):
    cost = 40.0
    ingredients = ['peperoni', 'olives', 'salami', 'garlic']

    def __init__(self, extra_ingredients):
        super().__init__(self.ingredients, self.cost, extra_ingredients)


class Hawaii(Pizza):
    cost = 47.0
    ingredients = ['pineapple', 'ham', 'basil', 'tomatoes']

    def __init__(self, extra_ingredients):
        super().__init__(self.ingredients, self.cost, extra_ingredients)


class Marenara(Pizza):
    cost = 46.0
    ingredients = ['tomatoes', 'oregano', 'anchovies', 'garlic']

    def __init__(self, extra_ingredients):
        super().__init__(self.ingredients,
                         self.cost, extra_ingredients)


class Pimaavera(Pizza):
    cost = 52.0
    ingredients = ['oregano', 'cheese', 'olives', 'tomatoes', 'anchovies']

    def __init__(self, extra_ingredients):
        super().__init__(self.ingredients, self.cost, extra_ingredients)


# Testing part.
def main():
    while True:
        print('=======[Welcome to our Pizzeria!]=======\n'
              '[> Pizza of the day is {} <]'
              .format(Pizza.pizza_of_day_the_day()))
        ask = input('Would you like to make an order ?[y/n]\n'
                    '>>> ')
        print('Choose and input here some extra-ingredients, '
              'which you want add to pizza in list you\'ll see below: \n'
              'If you don\'t want add them - press <Enter>')
        print(AllIngredients().print_all_ingredients())
        list_of_ingredients = input('>>> ').split(', ')
        if '' in list_of_ingredients:
            list_of_ingredients.remove('')
        if ask == 'y':
            pizza = eval(Pizza.pizza_of_day_the_day() + '(list_of_ingredients)')
            try:
                print('You\'re order is: {}\n'
                      'It includes: {}\n'
                      'Extra-ingredients: {} \n'
                      'Total price: {}'.format(pizza.__class__.__name__,
                                               pizza.get_ingredients(),
                                               pizza.get_extra_ingredients(),
                                               pizza.get_cost()))
            except KeyError:
                print('Not available ingredients in your input!')
                continue
        else:
            print('Don\'t want it - whatever you want :)')
            break

        if input('To order this pizza with another '
                 'ingredients press <Enter> key') != '':
            break


if __name__ == '__main__':
    main()
