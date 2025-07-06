command = input()
force = {}
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        if force_user not in force.values() and force_side not in force.keys() :
            force[force_side] = [force_user]
        # elif force_user not in force.values():
        #     force[force_side] = force[force_side] + [force_user]
    elif "->" in command:
        force_user , force_side = command.split(" -> ")
        value = force[force_side]
        if force_user not in value:
            # add it
            force[force_side] = force[force_side] + [force_user]
            print(f"{force_user} joins the {force_side} side!")
        for key in force.keys():
            if key != force_side:
                value = force[key]
                # print(value)
                if force_user in value:
                    # remove it
                    value.remove(force_user)
                    force[key] = value
    command = input()

for key, value in force.items():
    if value:
        print(f"Side: {key}, Members: {len(value)}")
        for v in value:
            print(f"! {v}")