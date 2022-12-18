class Monkey:

    def __init__(self, items, operation, divisible_by, monkey_true, monkey_false):
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.inspect_count = 0

    def act(self, monkeys):

        for item in self.items:

            self.inspect_count += 1

            new_worry_level = self.operation(item) % (2*3*5*7*11*13*17*19)
            if new_worry_level % self.divisible_by == 0:
                target_monkey = monkeys[self.monkey_true]
            else:
                target_monkey = monkeys[self.monkey_false]

            target_monkey.items.append(new_worry_level)

        self.items = []


with open('input') as f:
    lines = f.read().splitlines()

monkeys = [
        Monkey(items=[80],
            operation=lambda old: old * 5, divisible_by=2, monkey_true=4, monkey_false=3),
        Monkey(items=[75, 83, 74],
            operation=lambda old: old + 7, divisible_by=7, monkey_true=5, monkey_false=6),
        Monkey(items=[86, 67, 61, 96, 52, 63, 73],
            operation=lambda old: old + 5, divisible_by=3, monkey_true=7, monkey_false=0),
        Monkey(items=[85, 83, 55, 85, 57, 70, 85, 52],
            operation=lambda old: old + 8, divisible_by=17, monkey_true=1, monkey_false=5),
        Monkey(items=[67, 75, 91, 72, 89],
            operation=lambda old: old + 4, divisible_by=11, monkey_true=3, monkey_false=1),
        Monkey(items=[66, 64, 68, 92, 68, 77],
            operation=lambda old: old * 2, divisible_by=19, monkey_true=6, monkey_false=2),
        Monkey(items=[97, 94, 79, 88],
            operation=lambda old: old * old, divisible_by=5, monkey_true=2, monkey_false=7),
        Monkey(items=[77, 85],
            operation=lambda old: old + 6, divisible_by=13, monkey_true=4, monkey_false=0)]

for i in range(10000):

    print(i)

    for monkey in monkeys:

        monkey.act(monkeys)

top_inspections = sorted([monkey.inspect_count for monkey in monkeys], reverse=True)
print(top_inspections[0] * top_inspections[1])
