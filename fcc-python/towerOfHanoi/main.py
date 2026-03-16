from typing import List


def hanoi_solver(disks: int) -> str:
    # 3 rods, first starts with all disks
    rods: List[list[int]] = [list(range(disks, 0, -1)), [], []]

    moves: list[str] = []

    def record_move():
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move_disks(n: int, source: int, aux: int, target: int):
        if n == 1:
            # mover n diretamente de source -> target
            rods[target].append(rods[source].pop())
            record_move()
        else:
            # mover n-1 de source -> auxiliar
            move_disks(n - 1, source, target, aux)

            # mover maior de source -> target
            rods[target].append(rods[source].pop())
            record_move()

            # mover n-1 de auxiliar -> target
            move_disks(n - 1, aux, source, target)

    record_move()
    move_disks(disks, 0, 1, 2)

    return "\n".join(moves)


if __name__ == "__main__":
    print(f"Hanoi with 5 disks:\n{hanoi_solver(5)}")
