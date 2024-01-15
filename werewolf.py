class Werewolf:
    def __init__(self, name, transforms_into, aggression):
        self.name = name
        self.transforms_into = transforms_into
        self.agr = aggression


    def get_difference(self):
        return self.agr[1] - self.agr[0]

    def __sub__(self, other):
        new_name = self.name[:-1] + other.name
        new_transforms_into = max(self.transforms_into, other.transforms_into)
        new_aggression = (min(self.agr[0], other.agr[0]),)
        new_aggression += (min(self.agr[1], other.agr[1]),)
        return Werewolf(new_name, new_transforms_into, new_aggression)

    def __mod__(self, number):
        new_aggression = (self.agr[0] % number,)
        new_aggression += (self.agr[1] % number,)
        return Werewolf(self.name, self.transforms_into, new_aggression)

    def __call__(self, new_transforms_into):
        self.transforms_into = new_transforms_into
        aggg = len(self.transforms_into)
        self.agr = (self.agr[0], aggg)
        return Werewolf(self.name, self.transforms_into, self.agr)

    def __lt__(self, other):
        return (self.agr[1] - self.agr[0], self.transforms_into, self.name) < \
               (other.agr[1] - other.agr[0], other.transforms_into, other.name)

    def __eq__(self, other):
        return (self.agr[1] - self.agr[0], self.transforms_into, self.name) == \
               (other.agr[1] - other.agr[0], other.transforms_into, other.name)

    def __le__(self, other):
        return (self.agr[1] - self.agr[0], self.transforms_into, self.name) <= \
               (other.agr[1] - other.agr[0], other.transforms_into, other.name)

    def __ne__(self, other):
        return (self.agr[1] - self.agr[0], self.transforms_into, self.name) != \
               (other.agr[1] - other.agr[0], other.transforms_into, other.name)

    def __gt__(self, other):
        return (self.agr[1] - self.agr[0], self.transforms_into, self.name) > \
               (other.agr[1] - other.agr[0], other.transforms_into, other.name)

    def __ge__(self, other):
        return (self.agr[1] - self.agr[0], self.transforms_into, self.name) >= \
               (other.agr[1] - other.agr[0], other.transforms_into, other.name)

    def __repr__(self):
        return f"Werewolf by name {self.name} ({self.transforms_into}, {self.agr})"

# тест 1
wf = Werewolf('Swen', 'wolf', (1, 10))
print(wf, wf.get_difference(), sep='\n')
wf('Grizzly bear')
id_wf = id(wf)
wf %= 5
print(wf)

# тест 2
wf = Werewolf('Draco', 'Basilisk', (8, 48))
wf1 = Werewolf('Lart', 'Morten', (1, 13))
print(wf > wf1, wf <= wf1, wf != wf1)
wf2 = wf - wf1
print(wf, wf1, wf2, sep='\n')
print(wf2 < wf1, wf2 >= wf, wf2 == wf)