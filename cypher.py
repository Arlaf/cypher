import string


class Key:
    def __init__(self, key: str):
        self.key = key
        self.current_index = 0

    def next(self) -> int:
        letter = self.key[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.key)
        return string.ascii_lowercase.index(letter) + 1

    def reset(self) -> None:
        self.current_index = 0


class Cypher:
    def __init__(self) -> None:
        self.key = None
        self.alphabet = string.ascii_lowercase

    def set_key(self, key: str) -> None:
        self.key = Key(key.lower())

    def _convert(self, msg: str, func):
        self.key.reset()
        msg = msg.lower()
        cyphered = ''
        for letter in msg:
            if letter not in self.alphabet:
                cyphered += letter
            else:
                offset = self.key.next()
                cyphered += func(letter, offset)
        return cyphered

    def cypher(self, msg: str) -> str:
        return self._convert(msg, self.cypher_letter)

    def decypher(self, msg: str) -> str:
        return self._convert(msg, self.decypher_letter)

    def cypher_letter(self, letter: str, offset: int) -> str:
        letter_i = self.alphabet.index(letter)
        return self.alphabet[(letter_i + offset) % 26]

    def decypher_letter(self, letter: str, offset: int) -> str:
        return self.cypher_letter(letter,  (-1 * offset))


if __name__ == '__main__':
    cypher = Cypher()
    cypher.set_key('qsjefgqkdfjljbgqlkrgtbf')
    msg = 'Bonjour tout le monde. Comment allez-vous ? Moi ca va pas mal'
    coded = cypher.cypher(msg)
    print(coded)
    decoded = cypher.decypher(coded)
    print(decoded)
