def loading_bar(number: int):
    if number < 100:
        loading_str = ''
        for index in range(1, int(number / 10) + 1):
            loading_str += "%"
        for index in range(1, 10 - (int(number / 10)) + 1):
            loading_str += "."
        print(f"{number}% [{loading_str}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")

loding_number = int(input())
loading_bar(loding_number)