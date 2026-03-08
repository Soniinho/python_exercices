def add_setting(settings: dict[str, str], key_value: tuple[str, str]) -> str:
    key, value = key_value
    key = key.lower()
    value = value.lower()

    if key in settings:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )

    settings.update({key: value})
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict[str, str], key_value: tuple[str, str]) -> str:
    key, value = key_value
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings: dict[str, str], key: str) -> str:
    key = key.lower()

    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings: dict[str, str]) -> str:
    if not settings:
        return "No settings available."

    textList: list = ["Current User Settings:"]

    for key, value in settings.items():
        textList.append(f"{key.capitalize()}: {value}")

    text: str = "\n".join(textList)
    text = text + "\n"
    return text


if __name__ == "__main__":
    test_settings: dict = {"setting1": "jogo", "setting2": "jogo2", "setting3": "jogo3"}
    print(view_settings(test_settings))
