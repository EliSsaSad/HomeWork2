class CaesarsCipher:
    def __init__(self):
        self.alphabet = \
            ("ABCDEFGHIJKLMNOPQRSTUVWXY"
             "Zabcdefghijklmnopqrstuvwxyz1234567890 !?.")
        self.alphabet_set = set(self.alphabet)

    def encrypt(self, message: str, key: int) -> str:
        """
        Шифрует сообщение с помощью шифра Цезаря.

        Args:
            message: Сообщение для шифрования.
            key: Ключ для шифрования.

        Returns:
            Зашифрованное сообщение.
        """
        encrypted_message = ""
        for char in message:
            if char in self.alphabet:
                index = self.alphabet.find(char)
                new_index = (index + key) % len(self.alphabet)
                encrypted_message += self.alphabet[new_index]
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message: str, key: int) -> str:
        """
        Расшифровывает сообщение, зашифрованное шифром Цезаря.

        Args:
            message: Сообщение для расшифровки.
            key: Ключ для расшифровки.

        Returns:
            Расшифрованное сообщение.
        """
        decrypted_message = ""
        for char in message:
            if char in self.alphabet:
                index = self.alphabet.find(char)
                new_index = (index - key) % len(self.alphabet)
                decrypted_message += self.alphabet[new_index]
            else:
                decrypted_message += char
        return decrypted_message


def find_key(message: str) -> int:
    """
    Ищет ключ шифрования Цезаря.

    Args:
        message: Зашифрованное сообщение.

    Returns:
        Ключ шифрования.
    """
    cipher = CaesarsCipher()

    # Дополнительная проверка: список осмысленных слов
    common_words = ["the", "and", "you", "is", "it", "this",
                    "that", "we", "he", "she", "to", "in", "of", "on"]

    for key in range(len(cipher.alphabet)):
        decrypted_message = cipher.decrypt(message, key)
        # Проверка на наличие пробела и осмысленных слов
        if " " in decrypted_message and any(word in decrypted_message.lower()
                                            for word in common_words):
            return key
    return None


if __name__ == "__main__":
    message = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"

    # Находим ключ
    key = find_key(message)
    print(f"Подобранный ключ: {key}")

    # Дешифруем сообщение с найденным ключом
    cipher = CaesarsCipher()
    decrypted_message = cipher.decrypt(message, key)
    print(f"Расшифрованное сообщение: {decrypted_message}")

    # Запрашиваем путь к файлу у пользователя
    file_path = input("Введите путь к файлу для записи: ")

    # Записываем расшифрованное сообщение в файл
    with open(file_path, "w") as file:
        file.write(decrypted_message)

print(f"Сообщение записано в файл: {file_path}")
