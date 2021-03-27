def main():
    
    N = int(input())
    # S = input()
    a_li = list(map(int, input().split()))
    # N, M = map(int, input().split())
    
    min_value = 2e+30
    
    for pattern in range(0, 2**(N-1), 1):
        binary_mask = format(pattern, "b")
        binary_mask = (((N-1) - len(binary_mask)) * "0") + binary_mask
    
        if pattern == 0:
            sections = [a_li]
        else:
            sections = []
            last_idx = 0
            for idx, mask in enumerate(binary_mask):
                if mask == "1":
                    sections.append(a_li[last_idx:idx+1])
                    last_idx = idx+1
            sections.append(a_li[last_idx:])
        # print(pattern, binary_mask, sections)
    
        list_bitwise_or = []
        for section in sections:
            s = 0
            for element in section:
                s = s | element
            list_bitwise_or.append(s)
    
        s = 0
        for element in list_bitwise_or:
            s = s ^ element
    
        if s < min_value:
            min_value = s
    
    print(min_value)


if __name__ == "__main__":
    main()