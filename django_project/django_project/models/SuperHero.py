from django_project.models.Person import Person


class SuperHero(Person):

    def __init__(self, first, last, nick) -> None:
        self.last = last
        self.nick = nick
        super(SuperHero, self).__init__(first, last)

    # def __init__(self, first, last, nick) -> None:
    #     super(SuperHero, self).__init__(first, last)
    #     self.nick = nick

    def nick_name(self) -> int:
        return "I'm %s" % self.nick


super_hero = SuperHero('Carl', 'Sagan', "Imobilyzer")
print(super_hero.nick_name())
print(super_hero.full_name())