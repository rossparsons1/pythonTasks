def read_file():
    with open("data/second_task.txt", encoding="utf-8") as file:
        numbers = file.readlines()
        numberAll = []

        for number in numbers:
            words = number.strip().split(" ")
            numberAll.append(list(map(int, words)))

        return numberAll

def sum_pos(numberAll):
    result = []

    for line in numberAll:
        sum = 0
        for num in line:
            if num > 0:
                sum += num
        result.append(sum)

    return result

def sum_all(result):
    sumAll = 0
    for num in result:
        sumAll += num
    return sumAll


def save_file(result,sumAll):
    with open("data/second_task_out.txt", 'w', encoding='utf-8') as out_file:
        for sum in result:
            out_file.write(f'{sum}\n')
        out_file.write(f'----------------\n')
        out_file.write(f'{sumAll}\n')


numberAll = read_file()
result = sum_pos(numberAll)
sumAll = sum_all(result)
save_file(result,sumAll)