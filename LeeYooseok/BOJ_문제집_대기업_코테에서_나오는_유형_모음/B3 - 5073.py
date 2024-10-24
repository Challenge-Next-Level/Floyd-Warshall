while True:
    triangle_side_list = list(map(int, input().split()))

    triangle_side_list.sort(reverse=True)

    a, b, c = triangle_side_list

    if a == 0 and b == 0 and c == 0:
        break

    if (b + c) <= a:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif (a == b) or (b == c) or (c == a):
        print("Isosceles")
    elif a != b and b != c and c != a:
        print("Scalene")
