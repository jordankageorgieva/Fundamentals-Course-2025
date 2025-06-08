def smallest_of_three_numbers(num_1: int, num_2 : int, num_3: int) -> int:
        if num_1 < num_2 and num_1 < num_3:
            return num_1
        elif num_2 < num_1 and num_2 < num_3:
            return  num_2
        elif num_3 < num_1 and num_3 < num_2 :
            return  num_3


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(smallest_of_three_numbers(number_1, number_2, number_3))
