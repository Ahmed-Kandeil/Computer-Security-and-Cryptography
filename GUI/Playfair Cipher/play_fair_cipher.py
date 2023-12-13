"""
Name: Ahmed Amro Abd-Elmoneim Kandil
ID: 4211133
Group: A1
Lec: 1

This file contains a class called PlayfairCipher which can be
used to encrypt and decrypt messages using the playfair cipher.
"""

import os
import subprocess

import string


class PlayfairCipher:
    """
    A class to encrypt and decrypt messages using the Playfair cipher.

    Attributes:
        key (str): The key to use for encryption or decryption.

    Methods:
        encrypt: Encrypts the plain text message.
        decrypt: Decrypts the cipher text message.
    """

    def __init__(self, key: str = "Delta") -> None:
        """
        Initializes a new PlayfairCipher object.

        Args:
            key (str, optional): The key to use for encryption or decryption.

        Raises:
            ValueError: if the `key` argument is empty or contains non-alphabetic characters.
        """

        key = key.upper().replace("J", "I")

        if not key or not key.isalpha():
            raise ValueError("The key must be a non-empty alphabetic string.")

        self.__key = key
        self.__generate_map()

    @property
    def key(self) -> str:
        """
        Gets the key used for encryption and decryption.

        Returns:
            str: The key.
        """

        return self.__key

    @key.setter
    def key(self, key: str) -> None:
        """
        Sets the key used for encryption and decryption.

        Args:
            key (str): The new key.

        Raises:
            ValueError: if the `key` argument is empty or contains non-alphabetic characters.
        """

        key = key.upper().replace("J", "I")

        if not key or not key.isalpha():
            raise ValueError("The key must be a non-empty alphabetic string.")

        self.__key = key
        self.__generate_map()

    def __generate_map(self) -> None:
        """
        Generates the Playfair cipher square.
        """

        alphabet = string.ascii_uppercase.replace("J", "")
        key_without_duplicates = "".join(sorted(set(self.__key), key=self.__key.index))

        key_square = key_without_duplicates + "".join(
            [char for char in alphabet if char not in key_without_duplicates]
        )

        self.map = [list(key_square[i : i + 5]) for i in range(0, 25, 5)]

    def __find_coordinates(self, char: str) -> tuple:
        """
        Finds the coordinates of a character in the Playfair square.

        Args:
            char (str): The character to find.

        Returns:
            tuple: The row and column coordinates.
        """
        if not char.isalpha():
            return

        for row, line in enumerate(self.map):
            if char in line:
                return row, line.index(char)

        raise ValueError(f"Character '{char}' not found in the Playfair square.")

    def encrypt(self, plain_text: str) -> str:
        """
        Encrypts the plain text message.

        Args:
            plain_text (str): The plain text message to encrypt.

        Returns:
            str: The encrypted message.
        """

        plain_text = plain_text.upper().replace("J", "I")

        if len(plain_text) % 2 != 0:
            plain_text += "X"

        encrypted_text = []

        for i in range(0, len(plain_text), 2):
            char1, char2 = plain_text[i], plain_text[i + 1]
            
            if char1.isalpha() and char2.isalpha():
                row1, col1 = self.__find_coordinates(char1)
                row2, col2 = self.__find_coordinates(char2)

                # Same row
                if row1 == row2:
                    letter_one, letter_two = (
                        self.map[row1][(col1 + 1) % 5],
                        self.map[row2][(col2 + 1) % 5],
                    )
                # Same column
                elif col1 == col2:
                    letter_one, letter_two = (
                        self.map[(row1 + 1) % 5][col1],
                        self.map[(row2 + 1) % 5][col2],
                    )
                # Different row and column
                else:
                    letter_one, letter_two = (
                        self.map[row1][col2],
                        self.map[row2][col1],
                    )

                encrypted_text.extend([letter_one, letter_two])

            else:
                encrypted_text.extend([char1, char2])

        return "".join(encrypted_text).lower()

    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypts the cipher text message.

        Args:
            cipher_text (str): The cipher text message to decrypt.

        Returns:
            str: The decrypted message.
        """

        cipher_text = cipher_text.upper()

        decrypted_text = []

        for i in range(0, len(cipher_text), 2):    
            char1, char2 = cipher_text[i], cipher_text[i + 1]

            if char1.isalpha() and char2.isalpha():

                row1, col1 = self.__find_coordinates(char1)
                row2, col2 = self.__find_coordinates(char2)

                # Same row
                if row1 == row2:
                    letter_one, letter_two = (
                        self.map[row1][(col1 - 1) % 5],
                        self.map[row2][(col2 - 1) % 5],
                    )
                # Same column
                elif col1 == col2:
                    letter_one, letter_two = (
                        self.map[(row1 - 1) % 5][col1],
                        self.map[(row2 - 1) % 5][col2],
                    )
                # Different row and column
                else:
                    letter_one, letter_two = (
                        self.map[row1][col2],
                        self.map[row2][col1],
                    )

                decrypted_text.extend([letter_one, letter_two])
            else:
                decrypted_text.extend([char1, char2])

        return "".join(decrypted_text).lower()


def clear_terminal() -> None:
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run([command])


def main() -> None:
    key = input("Enter the secret key: ")
    encrypter = PlayfairCipher(key=key)

    OPTIONS = (
        "Encrypt",
        "Decrypt",
        "Change Key",
    )

    FUNCTIONS = {
        1: encrypter.encrypt,
        2: encrypter.decrypt,
    }

    while True:
        clear_terminal()

        for i, option in enumerate(OPTIONS, start=1):
            print(f"{i}. {option}")

        text_tokens = input("Enter the message: ").split()
        option_num = int(input("Enter option num or 0 for quit: "))

        if option_num == 3:
            new_key = input("Enter the secret key: ")
            encrypter.key = new_key
            continue

        result = []

        for text in text_tokens:
            result.append(FUNCTIONS.get(option_num, quit)(text))

        result = " ".join(result)

        print(result)

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
