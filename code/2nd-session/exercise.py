from kanren import facts, var, eq, lall, lany, run, Relation, membero

# Define relations
mother = Relation()
father = Relation()

# The parents are the mother and father of `person`
def parents(x, person):
    return lany(
        mother(x, person),
        father(x, person)
    )

# The siblings are those who share the same set father (or mother) with `person`
def siblings(x, person):
    y = var()
    return lall(
        father(y, person),
        father(y, x)
    )

# The chidren of a `person` are those whose father or mother are the `person`
def children(x, person):
    return lany(
       father(person, x),
       mother(person, x)
    )

# The paternal grandparents of a `person` are the parents of the father of the person
def paternal_grandparents(x, person):
    y = var()
    return lall(
        parents(x, y),
        father(y, person)
    )

# The maternal grandparents of a `person` are the parents of the mother of the person
def maternal_grandparents(x, person):
    y = var()
    return lall(
        parents(x, y),
        mother(y, person)
    )

# The grandparents of a `person` are either the paternal grandparents or the maternal grandparents
def grandparents(x, person):
    return lany(
        paternal_grandparents(x, person),
        maternal_grandparents(x, person)
    )

# Define constants
eric = 'Eric'
carol = 'Carol'
thomas = 'Thomas'
olga = 'Olga'
ken = 'Ken'
renata = 'Renata'
john = 'John'
julia = 'Julia'
leo = 'Leo'
angela = 'Angela'
karen = 'Karen'
rodrigo = 'Rodrigo'
lisa = 'Lisa'
bia = 'Bia'
arthur = 'Arthur'
cris = 'Cris'
silvia = 'Silvia'

# Define facts
facts(father, (eric, john))
facts(father, (eric, julia))
facts(father, (eric, leo))
facts(mother, (carol, john))
facts(mother, (carol, julia))
facts(mother, (carol, leo))

facts(father, (thomas, angela))
facts(father, (thomas, karen))
facts(mother, (olga, angela))
facts(mother, (olga, karen))

facts(father, (ken, rodrigo))
facts(mother, (renata, rodrigo))

facts(father, (leo, lisa))
facts(father, (leo, bia))
facts(father, (leo, arthur))
facts(mother, (angela, lisa))
facts(mother, (angela, bia))
facts(mother, (angela, arthur))

facts(father, (rodrigo, cris))
facts(father, (rodrigo, silvia))
facts(mother, (karen, cris))
facts(mother, (karen, silvia))

# Test the program
t = var()
print(f"Arthur's parents are {run(2, t, parents(t, arthur))}")

t = var()
print(f"Arthur's siblings are {run(3, t, siblings(t, arthur))}")

t = var()
print(f"Leo's children are {run(3, t, children(t, leo))}")

t = var()
print(f"Angela's children are {run(3, t, children(t, angela))}")

t = var()
print(f"Arthur's paternal grandparents are {run(2, t, paternal_grandparents(t, arthur))}")

t = var()
print(f"Arthur's maternal grandparents are {run(2, t, maternal_grandparents(t, arthur))}")

t = var()
print(f"Arthur's grandparents are {run(4, t, grandparents(t, arthur))}")