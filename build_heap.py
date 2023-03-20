# python3

def build_heap(data, n):
    swap_list = []

    sort_heap(data,n, swap_list)

    return swap_list

def sort_heap(data, n, swap_list, lowest=0):

    for i in range(int(n/2)-1,-1,-1):
        left = 2*i+1
        right = 2*i+2
        lowest = i
        if data[left] < data[lowest]:
            lowest = left
        if data[right] < data[lowest]:
            lowest = right

        if lowest is not i:
            data[i], data[lowest] = data[lowest], data[i]
            swap_list.append((i, lowest))
            sort_heap(data, n, swap_list, lowest)

def main():
    input_method = input()
    if "F" in input_method:
        filepath = "tests/" + input()
        with open(filepath, 'r', encoding='UTF-8') as file:
            (n, line) = file.read().splitlines()
            data = list(map(int, line.split()))
            n = int(n)
    elif "I" in input_method:
        n = int(input())
        data = list(map(int, input().split()))
    else:
        return

    assert len(data) == n

    swaps = build_heap(data, n)

    assert len(swaps) < 4*len(data)
    # this number should be less than 4n (less than 4*len(data))

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()