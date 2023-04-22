from random import randint

def random_array(n,m,max_value=20):
    array = []
    for i in range(0,n):
        sub_array = []
        for j in range(m):
            number = randint(0,max_value)
            sub_array.append(number)
        array.append(sub_array)
    return array

def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%d\t" % j, end='')
        print()

def counting(array):
    print()
    max_value = array[0][0]
    min_value = array[0][0]
    max_j = 0
    max_i = 0
    min_j = 0
    min_i = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] >= max_value:
                max_value = array[i][j]
                max_j = j
                max_i = i
            if array[i][j] <= min_value:
                min_value = array[i][j]
                min_j = j
                min_i = i
    print("Координаты максимума: ["+ str(max_i+1)+"]["+str(max_j+1)+"]")
    print("Координаты минимума: [" + str(min_i + 1) + "][" + str(min_j + 1) + "]")
    return max_value,min_value, max_i,max_j,min_i, min_j

def main():
    array = random_array(4,5)
    print_array(array)
    max_value,min_value,max_i,max_j,min_i,min_j = counting(array)
    while True:
        print()
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание")
        print("3. Выход.")
        key = input("Введите комманду 1, 2 или 3: ")
        if key == '1':
            array = random_array(4, 5)
            array[0][1] = 1
            array[1][1] = 1
            array[2][1] = 1
            array[3][1] = 1
            print_array(array)
            max_value,min_value,max_i,max_j,min_i,min_j = counting(array)
        elif key == '2':
            print()
            count = 0
            for i in range(len(array)):
                for j in range(len(array[i])):
                    if(array[i][1] == 1):
                        count += 1
                    if(count == 4):
                        array[min_i][min_j] = max_value
                        array[max_i][max_j] = min_value
            print_array(array)
        elif key == "3":
            exit(0)


if __name__ == '__main__':
    main()
