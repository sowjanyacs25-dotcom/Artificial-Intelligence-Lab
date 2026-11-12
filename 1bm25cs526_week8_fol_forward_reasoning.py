

facts = {
    "Barks(Tommy)",
    "FourLegs(Tommy)",
    "SharpTeeth(Tommy)"
}

rules = [
    (["Barks(Tommy)", "FourLegs(Tommy)"], "Dog(Tommy)"),
    (["Dog(Tommy)"], "Mammal(Tommy)"),
    (["Mammal(Tommy)", "SharpTeeth(Tommy)"], "Carnivore(Tommy)"),
    (["Feathers(Tommy)", "LaysEggs(Tommy)"], "Bird(Tommy)"),
    (["Bird(Tommy)"], "CanFly(Tommy)")
]

while True:
    new_fact = False

    for conditions, conclusion in rules:
        if all(condition in facts for condition in conditions):
            if conclusion not in facts:
                facts.add(conclusion)
                print("Derived:", conclusion)
                new_fact = True

    if not new_fact:
        break

if "Carnivore(Tommy)" in facts:
    print("\nTommy is a Carnivore")
else:
    print("\nTommy is not a Carnivore")

output
Derived: Dog(Tommy)
Derived: Mammal(Tommy)
Derived: Carnivore(Tommy)

Tommy is a Carnivore
