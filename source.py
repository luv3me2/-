from typing import List

PACKAGE_ID = "161586820"

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
        print(f"ID посылки {PACKAGE_ID}: нет роботов для перевозки")
        return 0
    
    sorted_weights = sorted(weights)
    
    left = 0
    right = len(sorted_weights) - 1
    platforms = 0
    
    while left <= right:
        if left < right and sorted_weights[left] + sorted_weights[right] <= limit:
            left += 1
        right -= 1
        platforms += 1
    
    print(f"ID посылки {PACKAGE_ID}: требуется {platforms} платформ для {len(weights)} роботов")
    return platforms


if __name__ == "__main__":
    try:
        print(f"Обработка посылки {PACKAGE_ID}")
        
        weights_line = input().strip()
        
        if not weights_line:
            print(f"ID посылки {PACKAGE_ID}: 0")
            print(0)
        else:
            weights = [int(x) for x in weights_line.split()]
            limit = int(input().strip())
            result = calculate_min_platforms(weights, limit)
            print(result)
            
    except (EOFError, ValueError):
        print(f"ID посылки {PACKAGE_ID}: ошибка ввода данных")
        print(0)
