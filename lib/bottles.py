class Bottles:
    @staticmethod
    def pluralize_bottle(number) -> str:
        return "bottles" if number > 1 else "bottle"

    @staticmethod
    def first_sentence(i) -> str:
        bottle = Bottles.pluralize_bottle(i)
        if i > 0:
            return f"{i} {bottle} of beer on the wall, {i} {bottle} of beer."
        else:
            return "No more bottles of beer on the wall, no more bottles of beer."

    @staticmethod
    def second_sentence(i) -> str:
        bottle = Bottles.pluralize_bottle(i-1)
        if i > 1:
            return f"Take one down and pass it around, {i-1} {bottle} of beer on the wall."
        elif i == 1:
            return "Take it down and pass it around, no more bottles of beer on the wall."
        else:
            return "Go to the store and buy some more, 99 bottles of beer on the wall."

    @staticmethod
    def verse(i: int) -> str:
        return Bottles.first_sentence(i) + "\n" + Bottles.second_sentence(i) + "\n"

    @staticmethod
    def verses(start: int, end: int) -> str:
        response = ""
        for i in range(start, end - 1, -1):
            response += Bottles.verse(i) + "\n"

        return response[:-1]

    @staticmethod
    def song():
        return Bottles.verses(99, 0)
