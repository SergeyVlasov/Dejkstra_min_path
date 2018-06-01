


def sxema_input():
    sxema = {}
    print('введите число ребер(участков):')
    dist = int(input())      # число участков
    print('первая точка (пробел) вторая точка (пробел) расстояние между ними:')

    i = 0
    while i < dist:
        a, b, weight = input().split()
        distance = float(weight)
        if a not in sxema:
            sxema[a] = {b:distance}
        else:
            sxema[a][b] = distance
        if b not in sxema:
            sxema[b] = {a:distance}
        else:
            sxema[b][a] = distance
        i+=1
    return sxema

def deikstra(sxema, start):
    shortest_path = {point:float('+inf') for point in sxema}
    shortest_path[start] = 0
    queue = [start]
    while len(queue) != 0:
        current = queue.pop(0)
        for neighbour in sxema[current]:
            offering_shortest_path = shortest_path[current]+sxema[current][neighbour]
            if offering_shortest_path  < shortest_path[neighbour]:
                shortest_path[neighbour] = offering_shortest_path
                queue.append(neighbour)
    return shortest_path



def find_path(sxema, shortest_path, interesting_point, start_point):
    interesting_path = [interesting_point]
    current_point = interesting_point

    while current_point != start_point:
        
        [interesting_path.append(neigh) for neigh in sxema[current_point] if
        shortest_path[current_point] - shortest_path[neigh] == sxema[current_point][neigh]]

        current_point = interesting_path[-1]
    return interesting_path



def find_path2(sxema, shortest_path, interesting_point, start_point):
    interesting_path = [interesting_point]
    current_point = interesting_point

    while current_point != start_point:
        
      
        [interesting_path.append(neigh) for neigh in sxema[current_point] if
        shortest_path[current_point] - shortest_path[neigh] == sxema[current_point][neigh]]

        current_point = interesting_path[-1]
    return interesting_path



def main():
    sxema = sxema_input()
    print(' граф: ')
    print(sxema)
    i = 1
    while i< 100:
        print('введите начальную точку:             ')

        start_point = input()
        shortest_path = deikstra(sxema, start_point)
        print('Кратчайшие расстояния:                 ')
        for point in sxema:
            print(point, shortest_path[point])
        print('кратчайшие пути от начальной точки:    ')
        print(shortest_path)
        print(' введите интересующую точку:   ')
        this_point = input()
        interesting_path = find_path(sxema, shortest_path, this_point, start_point)
        print('путь от начала к интересующей точке:   ')
        for point in reversed(interesting_path):
            print(point)
        print('press ENTER to continue')
        input()
        i+=1


if __name__ == '__main__':
    main()

