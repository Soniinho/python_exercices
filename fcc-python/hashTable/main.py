from typing import Any


class HashTable:
    """Hash Table"""

    def __init__(self) -> None:
        self.collection: dict[int, dict[str, Any]] = {}

    def hash(self, string: str) -> int:
        return sum(ord(char) for char in string)

    def add(self, key: str, value: Any) -> None:
        key_hash = self.hash(key)

        if key_hash not in self.collection:
            self.collection[key_hash] = {}

        self.collection[key_hash][key] = value

    def remove(self, key: str) -> None:
        key_hash = self.hash(key)

        bucket = self.collection.get(key_hash)

        if bucket:
            bucket.pop(key, None)

            # remover bucket vazio
            if not bucket:
                del self.collection[key_hash]

    def lookup(self, key: str) -> Any | None:
        key_hash = self.hash(key)

        bucket = self.collection.get(key_hash)

        if bucket:
            return bucket.get(key)

        return None


if __name__ == "__main__":
    hash_table = HashTable()

    hash_table.add("golf", "sport")
    hash_table.remove("golf1")
    print(hash_table.lookup("golf"))
