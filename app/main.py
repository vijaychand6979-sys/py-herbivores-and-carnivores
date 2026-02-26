from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def reduce_health(self, health: int) -> None:
        self.health = max(0, self.health - health)

        if self.health == 0:
            for i in range(len(Animal.alive)):
                if Animal.alive[i] == self:
                    Animal.alive.pop(i)
                    return

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.reduce_health(50)
