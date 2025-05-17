num_messages = int(input())

for index in range(num_messages):
    read_code_meaasage = int(input())
    if read_code_meaasage == 88 :
        print("Hello")
    elif read_code_meaasage == 86:
        print("How are you?")
    elif read_code_meaasage < 88 :
        print("GREAT!")
    elif read_code_meaasage > 88 :
        print("Bye.")