from typing import List

def min_platforms(weights: List[int], limit: int) -> int:
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
    
    # Сортируем веса по возрастанию
    weights.sort()
    
    left = 0  # указатель на самого лёгкого
    right = len(weights) - 1  # указатель на самого тяжёлого
    platforms = 0
    
    while left <= right:
        # Если самого тяжёлого можно перевезти с самым лёгким
        if left < right and weights[left] + weights[right] <= limit:
            left += 1  # берём и лёгкого, и тяжёлого
            right -= 1
        else:
            # Если нельзя объединить, везём только тяжёлого
            right -= 1
        platforms += 1
    
    return platforms


def main():
    """Основная функция для чтения ввода и вывода результата."""
    try:
        # Читаем первую строку и преобразуем в список целых чисел
        weights_line = input().strip()
        if not weights_line:
            # Если строка пустая, выводим 0
            print(0)
            return
        
        weights = list(map(int, weights_line.split()))
        
        # Читаем вторую строку - лимит
        limit = int(input().strip())
        
        # Вычисляем и выводим результат
        result = min_platforms(weights, limit)
        print(result)
        
    except EOFError:
        print(0)
    except ValueError:
        print(0)


if __name__ == "__main__":
    main()