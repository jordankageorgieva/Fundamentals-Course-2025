def is_repeated_simbol(ticket: str, simbol: str) -> bool:
    is_repeated = False
    if simbol in ticket:
        if 6 * simbol in ticket:
            is_repeated = True
    return is_repeated

def count_repeated_simbol(ticket: str, simbol: str) -> int:
    count = 0
    for index in range(len(ticket)):
        if (index == len(ticket) - 1) or ticket[index] == simbol and ticket[index] == ticket[index + 1] :
            count += 1
    return count

simbols = ['@', '#', '$' , '^']
tickets = input().split(", ")
for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) < 20 :
        print("invalid ticket")
        continue
    ticket_front = ticket[:10]
    ticket_back = ticket[10:]
    front_ticket_count = 0
    front_ticket_simbol = ''
    back_ticket_count = 0
    back_ticket_simbol = ''
    for simbol in simbols:
        if is_repeated_simbol(ticket_front, simbol):
            front_ticket_count = count_repeated_simbol(ticket_front, simbol)
            front_ticket_simbol = simbol
            break
    for simbol in simbols:
        if is_repeated_simbol(ticket_back, simbol):
            back_ticket_count = count_repeated_simbol(ticket_back, simbol)
            back_ticket_simbol = simbol
            break
    # print(f" back : {back_ticket_simbol}")
    # print(f" front : {front_ticket_simbol}")
    if back_ticket_simbol == front_ticket_simbol and back_ticket_simbol != '':
        min_count = min(back_ticket_count, front_ticket_count)
        if back_ticket_count == front_ticket_count and back_ticket_count == len(ticket) // 2:
            print(f"ticket \"{ticket}\" - {back_ticket_count}{simbol} Jackpot!")
            continue
        if min_count >= 6:
            print(f"ticket \"{ticket}\" - {min_count}{simbol}")
            continue
    else:
        print(f"ticket \"{ticket}\" - no match")
