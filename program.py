import string


def is_valid_passentence(passsentence: str) -> bool:
    PUNCTUATUIONS = (".", "!", "?")

    words = passsentence.split(" ")
    if (
        (len(words) <= 1)
        or not passsentence.endswith(PUNCTUATUIONS)
        or words[-1] in PUNCTUATUIONS
    ):
        return False

    last_word_without_punctuation = words[-1][:-1]
    words[-1] = last_word_without_punctuation

    seen = set()
    for word in words:
        if not is_valid_word(word) or word in seen:
            return False
        seen.add(word)

    return True


def is_valid_word(word: str) -> bool:
    ACCEPTED_LETTERS = string.ascii_letters
    return all(char in ACCEPTED_LETTERS for char in word)


def read_and_trim_from_file(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return file.read().splitlines()


def count_valid_passentences(passsentences: list[str]) -> int:
    valid_count = 0
    for passsentence in passsentences:
        if is_valid_passentence(passsentence):
            valid_count += 1
    return valid_count


def display_passentence_count(count: int) -> None:
    print(f"Helyes jelmondatok szama: {count}")


def main():
    FILENAME = "input.txt"
    passsentences = read_and_trim_from_file(FILENAME)
    passentence_count = count_valid_passentences(passsentences)
    display_passentence_count(passentence_count)


if __name__ == "__main__":
    main()
