class Bottles:
    MAX_BOTTLES = 99
    MIN_BOTTLES = 0

    @staticmethod
    def capitalise(s: str) -> str:
        result = ""
        for i in s.splitlines():
            result += i[0].upper() + i[1:] + "\n"
        return result

    @staticmethod
    def bottle_of_beer(i: int) -> str:
        i = i if i >= 0 else 99
        bottle_s = "bottles" if i != 1 else "bottle"
        number_s = i if i > 0 else "no more"
        return f"{number_s} {bottle_s} of beer"

    @staticmethod
    def take_one_down(i: int) -> str:
        if i > 0:
            one_or_it = "one" if i else "it"
            return f"Take {one_or_it} down and pass it around"
        else:
            return "Go to the store and buy some more"

    @staticmethod
    def first_sentence(i: int) -> str:
        bottle_of_beer = Bottles.bottle_of_beer(i)
        return f"{bottle_of_beer} on the wall, {bottle_of_beer}."

    @staticmethod
    def second_sentence(i: int) -> str:
        take_one_down = Bottles.take_one_down(i)
        bottle_of_beer = Bottles.bottle_of_beer(i - 1)
        return f"{take_one_down}, {bottle_of_beer} on the wall."

    @staticmethod
    def verse(i: int) -> str:
        sentences = f"{Bottles.first_sentence(i)}\n{Bottles.second_sentence(i)}\n"
        return Bottles.capitalise(sentences)

    @staticmethod
    def verses(start: int, end: int) -> str:
        all_verses = [Bottles.verse(i) for i in range(start, end - 1, -1)]
        return "\n".join(all_verses)

    @staticmethod
    def song() -> str:
        return Bottles.verses(Bottles.MAX_BOTTLES, Bottles.MIN_BOTTLES)
