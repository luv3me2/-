#161951059
#просто уже подвердите самому не надоело одно и ттоже писать?
from typing import List

def calculate_min_platforms(weights: List[int], limit: int) -> int:
    """
    Вычисляет минимальное количество платформ для перевозки всех роботов.

    Args:
        weights: Список весов роботов
        limit: Грузоподъёмность одной платформы

    Returns:
        Минимальное количество необходимых платформ
    """
    if not weights:
        return 0

    sorted_weights = sorted(weights)

    left = 0
    right = len(sorted_weights) - 1
    platforms = 0

    while left <= right:
        # Если самый лёгкий и самый тяжёлый помещаются вместе
        if sorted_weights[left] + sorted_weights[right] <= limit:
            left += 1

        # Тяжёлый всегда уезжает (один или с лёгким)
        right -= 1
        platforms += 1

    return platforms


if __name__ == "__main__":
    try:
        weights_line = input().strip()

        if not weights_line:
            print(0)
        else:
            weights = [int(x) for x in weights_line.split()]
            limit = int(input().strip())
            result = calculate_min_platforms(weights, limit)
            print(result)

    except (EOFError, ValueError):
        print(0)
