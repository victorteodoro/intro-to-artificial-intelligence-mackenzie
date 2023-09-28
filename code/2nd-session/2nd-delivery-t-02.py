###############################################################################
# No exercício abaixo, notamos que, se o unicórnio está mentindo, então o leão
# *não* irá mentir amanhã. Logo o leão deve estar mentindo hoje, já que o leão
# diz que vai mentir amanhã. Porém o unicórnio e o leão não mentem ambos no
# mesmo dia.
#
# Por outro lado, se o unicórnio está falando a verdade, o leão vai mentir 
# amanhã. O que implica que o leão está falando a verdade hoje, já que também
# diz que vai mentir amanhã. Logo, tanto o leão quanto o unicórnio deve, estar
# falando a verdade!
# 
# No exercício abaixo, então, definimos em que dia os animais não mentem (i.e. 
# falam a verdade) e buscamos saber em que dias ambos os animais falam a
# verdade. 
###############################################################################

from kanren import Relation, run, var, lall, lany, facts

# The day an animal doesn't lie
doesnt_lie = Relation()

# Define the animals
lion = 'Lion'
unicorn = 'Unicorn'

# Define the days of the week
mon = 'Monday'
tue = 'Tuesday'
wed = 'Wednesday'
thu = 'Thursday'
fri = 'Friday'
sat = 'Saturday'
sun = 'Sunday'

# The lion lies in which days
facts(doesnt_lie, (lion, thu))
facts(doesnt_lie, (lion, fri))
facts(doesnt_lie, (lion, sat))
facts(doesnt_lie, (lion, sun))

# The unicorn lies in which days
facts(doesnt_lie, (unicorn, sun))
facts(doesnt_lie, (unicorn, mon))
facts(doesnt_lie, (unicorn, tue))
facts(doesnt_lie, (unicorn, wed))

# First we must know in which days an `animal` doesn't lie
def days_i_dont_lie(days, animal):
    return lany(doesnt_lie(animal, days))

# Then we must find out in which days both animals don't lie
def which_day_is_it(day, animal1, animal2):
    return lall(days_i_dont_lie(day, animal1), days_i_dont_lie(day, animal2))

# Testing the definitions above
x = var()
print(f"The days in which the lion doesn't lie are {run(4, x, days_i_dont_lie(x, lion))}")

# We do in fact get the day we want (Sunday)
x = var()
print(f"Today is {run(1, x, which_day_is_it(x, lion, unicorn))[0]}")