import random as rnd


class Dice:

    def __init__(self):
        self._set = []
        self._rolls = []
        self._outcomes = []

    def add(self, sides):
        self._set.append(sides)

    def remove(self, index):
        self._set.remove(index)

    def clear(self):
        del self._outcomes[:]
        del self._rolls[:]

    def roll(self):
        t = 0
        rolls = []
        for d in self._set:
            r = rnd.randrange(1, d + 1)
            t += r
            rolls.append(r)

        self._rolls.append(rolls)
        self._outcomes.append(t)

        return t

    def count(self):
        return len(self._outcomes)

    def mean(self):
        return float(sum(self._outcomes)) / max(len(self._outcomes), 1)

    def mode(self):
        numbers = self.countPerOutcome()

        max = 0
        number = 0
        for n in numbers:
            if numbers[n] > max:
                max = numbers[n]
                number = n

        return number

    def countPerOutcome(self):
        numbers = {}

        for n in self._outcomes:
            if n in numbers:
                numbers[n] += 1
            else:
                numbers[n] = 1

        return numbers

    def highestLastRoll(self, count=1):
        rolls = self._rolls[-1]
        highest = []

        for r in rolls:
            if len(highest) < count:
                highest.append(r)
            else:
                for h in highest:
                    if r > h:
                        highest.remove(h)
                        highest.append(r)

    def lowestLastRoll(self, count=1):
        rolls = self._rolls[-1]
        lowest = []

        for r in rolls:
            if len(lowest) < count:
                lowest.append(r)
            else:
                for l in lowest:
                    if r < l:
                        lowest.remove(l)
                        lowest.append(r)










