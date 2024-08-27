import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name,'r',encoding='utf-8') as file:
        while file.readline():
            all_data.append(file.readline())



filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start1 = datetime.datetime.now()
for file in filenames:
    read_info(file)
fin1 = datetime.datetime.now()
print(f'{fin1 - start1} - линейный')

# Многопроцессный
if __name__ == '__main__':
    start2 = datetime.datetime.now()
    with multiprocessing.Pool(processes = 6) as pool:
        pool.map(read_info,filenames)
    fin2 = datetime.datetime.now()
    print(f'{fin2 - start2} - многопроцессный')