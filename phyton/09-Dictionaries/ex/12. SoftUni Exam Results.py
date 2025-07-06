command = input()
student_data_out = {}
count_removed_names = 0
while command != "exam finished":
    student_data_in = command.split("-")
    if len(student_data_in) == 3:
        name = student_data_in[0]
        language = student_data_in[1]
        points = int(student_data_in[2])
        if name not in student_data_out.keys():
            student_data_out[name] = {language : points}
        else:
            current_data = student_data_out[name]
            # print(current_data)
            if language in current_data:
                # updata the data with lowest
                current_points = current_data[language]
                new_name = f"update_{str(count_removed_names)}"
                student_data_out[new_name] = {language: points}
                count_removed_names += 1
                if points > current_points:
                    student_data_out[name] = {language: points}

            else:
                 #  add new data
                 current_data[language] = points
                 student_data_out[name] = current_data
    elif len(student_data_in) == 2:
        #     banned user
        name = student_data_in[0]
        if name in student_data_out.keys():
            current_data = student_data_out[name]
            student_data_out.pop(name)
            # print(current_data)
            new_name = f"removed_{str(count_removed_names)}"
            student_data_out[new_name] = current_data
            count_removed_names += 1
    command = input()

# print(student_data_out)
# data out
results_student = {}
for key, value in student_data_out.items():
    for k1, v1 in value.items():
        if "removed_" not in key and "update_" not in key :
            results_student[key] = v1

results_language = {}
for key, value in student_data_out.items():
    for k1, v1 in value.items():
        if k1 not in results_language.keys():
            results_language[k1] = 0
        count = int(results_language[k1]) + 1
        results_language[k1] = count

print(f"Results:")
print("\n".join([key + f" | {value}" for key, value in results_student.items()]))
print(f"Submissions:")
print("\n".join([key + f" - {value}" for key, value in results_language.items()]))