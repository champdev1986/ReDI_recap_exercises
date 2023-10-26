class WaterBottle:
    def __init__(self, water_amount):
        self.water_amount = water_amount

    def fill_up(self, other_bottle):
        self.water_amount += other_bottle.water_amount
        other_bottle.water_amount = 0

def main():
    first_bottle = WaterBottle(1)
    second_bottle = WaterBottle(2)

    first_bottle.fill_up(second_bottle)

    print(f"First bottle water amount = {first_bottle.water_amount}")
    print(f"Second bottle water amount = {second_bottle.water_amount}")

main()

