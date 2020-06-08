#Бинарный поиск

#Задаём пустой список
my_list = []
#Вводим количество элементов
n = int(input("Ввведите количество элементов в массиве: "))
for i in range(n):
    new_element = int(input("Ввведите очередной элемент массива по возрастанию: "))  # считываем очередной элемент
    my_list.append(new_element)  # добавляем его в список


def binary_search(list, item):
  # low минимальная и high максимальная граница списка
  low = 0
  high = len(list) - 1

  # Пока эта часть не сократится до одного элемента
  while low <= high:
    #Проверяем средний элемент
    mid = (low + high) // 2
    guess = list[mid]
    #print(guess) #для отладки видеть значения проходов
    # Значение найдено
    if guess == item:
      return mid
    # Много
    if guess > item:
      high = mid - 1
    # Мало
    else:
      low = mid + 1

  # Значение не существует
  return None


print("Ваш элемент находится на "+str(binary_search(my_list, int(input("Ввведите число для поиска: "))))+" позиции в массиве.")
