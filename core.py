from enum import Enum
from unittest import TestCase


class Unit(Enum):
    GRAM = 1,
    KILOGRAM = 1000,
    UNIT = 1

class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit


class ZakatConfig:
    def __init__(self, nissab: Quantity, zakat_percentage):
        self.nissab = nissab
        self.zakat_percentage = zakat_percentage


class CamelType(Enum):
    REGULAR         = 'Normal'
    BINTOU_MAKHADH  = 'Female camel between 1 year and 2 years old'
    BINTOU_LABOUNE  = 'Female camel between 2 year and 3 years old'
    HAKKA           = 'Female camel between 3 year and 4 years old'
    JADAA           = 'Female camel greater than 4 years old'


class CattleType(Enum):
    CAMEL = ZakatConfig(Quantity(5, Unit.UNIT), 0)
    SHEEP = 'SHEEP'
    COWS = 'COWS'


class GoldType(Enum):
    KIRAT_18 = ZakatConfig(Quantity(113, Unit.GRAM), 2.5)
    KIRAT_21 = ZakatConfig(Quantity(97, Unit.GRAM), 2.5)
    KIRAT_24 = ZakatConfig(Quantity(85, Unit.GRAM), 2.5)


class AgricultureType(Enum):
    NATURALLY_IRRIGATED = ZakatConfig(Quantity(665, Unit.KILOGRAM), 10)
    ARTIFICIALLY_IRRIGATED = ZakatConfig(Quantity(665, Unit.KILOGRAM), 5)


class GoldZakat:
    def __init__(self, amount, type: GoldType):
        self.amount = amount
        self.type = type

    def calculate(self):
        zakat_config = self.type.value
        if self.amount < zakat_config.nissab.amount:
            return 0

        return self.amount * (zakat_config.zakat_percentage / 100)


class AgricultureZakat:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

    def calculate(self):
        zakat_config = self.type.value
        if self.amount < zakat_config.nissab.amount:
            return 0

        return self.amount * (zakat_config.zakat_percentage / 100)


class CattleZakat:
    def __init__(self, count, type):
        self.count = count
        self.type = type

    def calculate(self):
        zakat_config = self.type.value
        if self.count < zakat_config.nissab.amount:
            return 0

        return 0

        # if zakat_config == CattleType.CAMEL:
        #     if self.count >= 5 and self.count < 25:
        #         return int(self.count / 5) * CamelType.REGULAR
        #     elif self.count >= 25 and self.count < 35:
        #         return 1 * CamelType.BINTOU_MAKHADH
        #     elif self.count >= 35 and self.count < 45:
        #         return 1 * CamelType.BINTOU_LABOUNE
        #     elif self.count >= 45 and self.count < 60:
        #         return 1 * CamelType.HAKKA
        #     elif self.count >= 60 and self.count < 75:
        #         return 1 * CamelType.JADAA
        #     elif self.count >= 75 and self.count < 90:
        #         return 2 * CamelType.BINTOU_LABOUNE
        #     elif self.count >= 90 and self.count < 120:
        #         return 2 * CamelType.HAKKA
        #     else:
        #         return Every 40 * CamelType.HAKKA and Every 50 * CamelType.BINTOU_LABOUNE



class SilverZakat:
    def __init__(self, amount):
        self.amount = amount
        self.zakat_config = ZakatConfig(Quantity(595, Unit.GRAM), 2.5)

    def calculate(self):
        zakat_config = self.zakat_config
        if self.amount < zakat_config.nissab.amount:
            return 0

        return self.amount * (zakat_config.zakat_percentage / 100)


class LiquidityZakat:
    def __init__(self, amount, gold_gram_current_price):
        self.amount = amount
        self.zakat_config = ZakatConfig(Quantity(gold_gram_current_price * 85), 2.5)

    def calculate(self):
        zakat_config = self.zakat_config
        if self.amount < zakat_config.nissab.amount:
            return 0

        return self.amount * (zakat_config.zakat_percentage / 100)


class TestingGold(TestCase):
    def test_gold_zakat_kirat_18(self):
        gold = GoldZakat(0, GoldType.KIRAT_18)
        self.assertEqual(0, gold.calculate())

    def test_gold_zakat_less_than_nissab_kirat_18(self):
        gold = GoldZakat(1, GoldType.KIRAT_18)
        self.assertEqual(0, gold.calculate())

    def test_gold_zakat_greater_than_nissab_kirat_18(self):
        # test data
        gold = GoldZakat(200, GoldType.KIRAT_18)
        # run test
        result = gold.calculate()
        # assert result
        self.assertEqual(5, result)

    def test_gold_zakat_kirat_21(self):
        gold = GoldZakat(0, GoldType.KIRAT_21)
        self.assertEqual(0, gold.calculate())

    def test_gold_zakat_less_than_nissab_kirat_21(self):
        gold = GoldZakat(1, GoldType.KIRAT_21)
        self.assertEqual(0, gold.calculate())

    def test_gold_zakat_greater_than_nissab_kirat_21(self):
        # test data
        gold = GoldZakat(100, GoldType.KIRAT_21)
        # run test
        result = gold.calculate()
        # assert result
        self.assertEqual(2.5, result)

    def test_gold_zakat_greater_than_nissab_kirat_24(self):
        # test data
        gold = GoldZakat(90, GoldType.KIRAT_24)
        # run test
        result = gold.calculate()
        # assert result
        self.assertEqual(2.25, result)


class TestingAgriculture(TestCase):
    def test_agriculture_less_than_nissab_natural(self):
        agr = AgricultureZakat(400, AgricultureType.NATURALLY_IRRIGATED)
        self.assertEqual(0, agr.calculate())

    def test_agriculture_less_than_nissab_artificial(self):
        agr = AgricultureZakat(400, AgricultureType.ARTIFICIALLY_IRRIGATED)
        self.assertEqual(0, agr.calculate())

    def test_agriculture_greater_than_nissab_artificial(self):
        agr = AgricultureZakat(1000, AgricultureType.ARTIFICIALLY_IRRIGATED)
        self.assertEqual(50, agr.calculate())

    def test_agriculture_greater_than_nissab_natural(self):
        agr = AgricultureZakat(1000, AgricultureType.NATURALLY_IRRIGATED)
        self.assertEqual(100, agr.calculate())

class TestingSilver(TestCase):
    def test_agriculture_less_than_nissab(self):
        agr = SilverZakat(400)
        self.assertEqual(0, agr.calculate())

    def test_agriculture_greater_than_nissab(self):
        agr = SilverZakat(1000)
        self.assertEqual(25, agr.calculate())


# We have an input X, we want to find the ways we can split X in perfect groups
# we want to split X in a way Z, Y where min(X - n * Z + m * Y >= 0)
# X = 200, Z=50, Y=40 => [(n = 4, m = 0), (n = 0, m = 5)]
# X = 210


X = 210
Z = 50
Y = 40


def solve(X, Z, Y):
    current_min = X
    solutions = []
    for n in range(0, int(X / Z) + 1):
        for m in range(0, int(X / Y) + 1):
            f = X - (n * Z + m * Y)
            if f < 0:
                break

            if f < current_min:
                current_min = f
                solutions = [(n, m)]
            elif f == current_min:
                solutions.append((n, m))

    return solutions

def solve2(X, Y, Z):
    s = solve_dp(X, Y, Z, {})
    current_min = X
    solutions = []
    for e in s:
        f = X - (e[0] * Y + e[1] * Z)
        if f < 0:
            continue

        if f < current_min:
            current_min = f
            solutions = [e]
        elif f == current_min:
            solutions.append(e)

    return solutions


def solve_dp(X, Y, Z, dp):
    if X in dp:
        return dp[X]
    if X < Y and X < Z:
        return [(0, 0)]
    if X == Y:
        return [(1, 0)]
    if X == Z:
        return [(0, 1)]

    result = []
    s1 = solve_dp(X - Y, Y, Z, dp)
    for e in s1:
        result.append((e[0] + 1, e[1]))

    s2 = solve_dp(X - Z, Y, Z, dp)
    for e in s2:
        result.append((e[0], e[1] + 1))

    dp[X] = result
    return result

# 150 -> (3, 0) <---
# 160 -> (0, 4) <---
# 200 -> (0, 5), (4, 0) <---


# farida(n) = {
#     farid(n-50) + hakka,
#     farida(n-40) + laboune
# }

def solve3(X, Y, Z):
    dp = {Y: [(1, 0)], Z: [(0, 1)]}
    current = Y
    while current < X:
        c = dp[current]
        r = []
        for e in c:
            r.append((e[0] + 1, e[1]))
        dp[current + Y] = r
        current += Y

    candidate = current
    if current > X:
        candidate = current - Y

    current = Z
    while current < X:
        c = dp[current]
        r = []
        if current + Z in dp:
            r = dp[current + Z]

        for e in c:
            r.append((e[0], e[1] + 1))
        dp[current + Z] = r
        current += Z

    if current > X:
        candidate = max(current - Z, candidate)
    return dp[candidate]


class TestingSolve(TestCase):
    def test_solve(self):
        X = 200
        Y = 50
        Z = 40
        # s = solve(X, Y, Z)
        # print(s)
        s = solve3(X, Y, Z)

        print(s)