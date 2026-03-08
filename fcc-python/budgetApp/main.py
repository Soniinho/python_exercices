from typing import List


class Category:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ledger: list = list()

    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -(amount), "description": description})
            return True
        else:
            return False

    def get_balance(self) -> float:
        balance: float = 0.0

        for item in self.ledger:
            balance += item["amount"]

        return balance

    def transfer(self, amount: float, other: "Category") -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount: float) -> bool:
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self) -> str:
        title = self.name.center(30, "*")

        description_list = []
        for item in self.ledger:
            description_list.append(
                f'{item["description"][:23]:<23}{item["amount"]:>7.2f}'
            )

        description = "\n".join(description_list)

        total = sum(item["amount"] for item in self.ledger)

        return f"{title}\n{description}\nTotal: {total:.2f}"


def create_spend_chart(categories: List["Category"]) -> str:
    title: str = "Percentage spent by category\n"

    # total spent amount
    spent: List[float] = []
    for c in categories:
        category_spent: float = 0
        for item in c.ledger:
            if item["amount"] < 0:
                category_spent += abs(item["amount"])
        spent.append(category_spent)
    total_spent: float = sum(spent)

    # percentage
    percentages: List[int] = []
    for s in spent:
        percent_real: int = int((s / total_spent) * 100)
        percentages.append((percent_real // 10) * 10)  # arredondar

    # chart part start
    chart: str = title

    # graph part
    for i in range(100, -1, -10):
        # y-axis 100 to 0 in steps of 10
        chart += f"{i:>3}| "

        # add the bars "o"
        for p in percentages:
            if p >= i:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # inicial + "-" *3 to match " o " used + "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # names in list
    names: List[str] = []
    for c in categories:
        names.append(c.name)

    max_len: int = max(map(len, names))
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n")


"""
def create_spend_chart(categories: List["Category"]) -> str:
    title: str = "Percentage spent by category\n"

    spent: List[float] = [
        sum(-item["amount"] for item in c.ledger if item["amount"] < 0)
        for c in categories
    ]

    total_spent: float = sum(spent)

    percentages: List[int] = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    chart: str = title

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        chart += "".join("o  " if p >= i else "   " for p in percentages)
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names: List[str] = [c.name for c in categories]
    max_len: int = max(map(len, names))

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n") 
"""

if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    print(food)
    print(create_spend_chart([food, clothing]))
