class Tank:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.tonnage = None
        self.hp = None
        self.cannon = None
        self.engine = None

    def __str__(self):
        info = (f'Tonnage: {self.tonnage} Tons',
                f'engine: {self.engine}',
                f'Horsepower: {self.hp} hp',
                f'Cannon: {self.cannon}',
                f'Serial: {self.serial}'
                )
        return '\n'.join(info)


class TankBuilder:
    def __init__(self):
        self.tank = Tank('RHN-00001')

    def configure_engine(self, engine_model):
        self.tank.engine = engine_model

    def configure_tonnage(self, amount):
        self.tank.tonnage = amount

    def configure_hp(self, amount):
        self.tank.hp = amount

    def configure_cannon(self, cannon_model):
        self.tank.cannon = cannon_model


class TankFactory:
    def __init__(self):
        self.builder = None

    def construct_tank(self, tonnage, hp, cannon, engine):
        self.builder = TankBuilder()
        steps = (self.builder.configure_tonnage(tonnage),
                 self.builder.configure_hp(hp),
                 self.builder.configure_cannon(cannon),
                 self.builder.configure_engine(engine))
        [step for step in steps]

    @property
    def tank(self):
        return self.builder.tank


def main():
    factory = TankFactory()
    factory.construct_tank(hp=1200, tonnage=65.7, cannon='Rheinmetall Rh-120 120mm Smoothbore', engine="MTY MB 873 V12")
    tank = factory.tank
    print(tank)


if __name__ == '__main__':
    main()
