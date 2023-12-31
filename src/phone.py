from src.item import Item


class Phone(Item):
    def __init__(self,
                 name: str,
                 price: float,
                 quantity: int,
                 number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError('Количество сим-карт должно быть больше нуля')

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', "
                f"{self.price}, {self.quantity}, {self.number_of_sim})")
