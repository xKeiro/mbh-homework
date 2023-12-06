import unittest
from unittest.mock import patch
from unittest.mock import mock_open
from program import count_valid_passentences, display_passentence_count
from program import is_valid_passentence
from program import read_and_trim_from_file


class TestIsValidPassentence(unittest.TestCase):
    def test_valid(self):
        sentence = "this is a valid passsentence!"
        self.assertTrue(is_valid_passentence(sentence))

    def test_one_word(self):
        sentence = "notvalid."
        self.assertFalse(is_valid_passentence(sentence))

    def test_no_punctuation(self):
        sentence = "this is not valid"
        self.assertFalse(is_valid_passentence(sentence))

    def test_repeated_words(self):
        sentence = "this is is not valid"
        self.assertFalse(is_valid_passentence(sentence))

    def test_uppercase(self):
        sentence = "This is a valid passsentence!"
        self.assertTrue(is_valid_passentence(sentence))

    def test_non_english(self):
        sentence = "this is not válid."
        self.assertFalse(is_valid_passentence(sentence))

    def test_bad_punctuation(self):
        sentence = "this is not valid#"
        self.assertFalse(is_valid_passentence(sentence))

    def test_allowed_punctuation(self):
        VALID_PUNCTUATIONS = (".", "!", "?")
        for punctuation in VALID_PUNCTUATIONS:
            with self.subTest(test_allowed_punctuation=punctuation):
                sentence = f"this is valid{punctuation}"
                self.assertTrue(is_valid_passentence(sentence))

    def test_empty_string(self):
        sentence = ""
        self.assertFalse(is_valid_passentence(sentence))

    def test_with_two_punctuations(self):
        sentence = "this is not valid?!"
        self.assertFalse(is_valid_passentence(sentence))

    def test_with_a_dangling_punctuation(self):
        sentence = "this is not valid !"
        self.assertFalse(is_valid_passentence(sentence))


class ReadFromFileTestCase(unittest.TestCase):
    def test_read_from_file_existing_file(self):
        with patch(
            "builtins.open", new_callable=mock_open, read_data="line1\nline2\nline3"
        ) as mock_file:
            result = read_and_trim_from_file("test.txt")
            assert result == ["line1", "line2", "line3"]

    def test_read_from_file_non_existing_file(self):
        with patch("builtins.open") as mock_open:
            mock_open.side_effect = FileNotFoundError
            with self.assertRaises(FileNotFoundError):
                read_and_trim_from_file("non_existing.txt")


class TestCountValidPassentences(unittest.TestCase):
    def test_count_empty_passentences(self):
        passsentences = []
        self.assertEqual(count_valid_passentences(passsentences), 0)

    def test_count_multiple_passentences(self):
        passsentences = [
            "this is a valid passsentence!",
            "this also valid passsentence.",
        ]
        self.assertEqual(count_valid_passentences(passsentences), 2)

    def test_count_invalid_passentences(self):
        passsentences = ["this is not a valid passsentence", "neither is this"]
        self.assertEqual(count_valid_passentences(passsentences), 0)

    def test_count_mixed_valid_and_invalid_passentences(self):
        passsentences = [
            "this is a valid passsentence!",
            "this is not a valid passsentence",
        ]
        self.assertEqual(count_valid_passentences(passsentences), 1)


class TestDisplayPassentenceCount(unittest.TestCase):
    def test_display_passentence_count(self):
        test_cases = [5, 10, 0, 97585934812391223, -1]
        for count in test_cases:
            with self.subTest(test_display_passentence_count=count):
                with patch("builtins.print") as mock_print:
                    display_passentence_count(count)
                    mock_print.assert_called_once_with(
                        f"Helyes jelmondatok szama: {count}"
                    )


if __name__ == "__main__":
    unittest.main()
