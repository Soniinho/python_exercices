from math import sqrt, pow


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return sqrt(pow(self.width, 2) + pow(self.height, 2))

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            row = "*" * self.width
            picture = (row + "\n") * self.height
            return picture

    """     
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture: list = []

            for _ in range(self.width):
                picture.append("*")
            picture.append("\n")

            for _ in range(self.height - 2):
                picture.append("*")
                for _ in range(self.width - 2):
                    picture.append(" ")
                picture.append("*\n")

            for _ in range(self.width):
                picture.append("*")
            picture.append("\n")

            picture_string: str = "".join(picture)
            return picture_string 
    """

    def get_amount_inside(self, shape: "Rectangle") -> int:
        if shape.width > self.width and shape.height > self.height:
            return 0
        else:
            height_help: int = self.height // shape.height
            width_help: int = self.width // shape.width
            return height_help * width_help

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length: int) -> None:
        super().__init__(length, length)

    def set_width(self, width: int) -> None:
        self.width = width
        self.height = width

    def set_height(self, height: int) -> None:
        self.width = height
        self.height = height

    def set_side(self, length: int) -> None:
        self.width = length
        self.height = length

    def __str__(self) -> str:
        return f"Square(side={self.width})"


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
