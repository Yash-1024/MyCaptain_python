import csv

def convert_csv(info_list):
    with open('student_info.csv', 'a', newline='') as f:
        writer = csv.writer(f)

        if f.tell() == 0:
            writer.writerow(["name","age","phone_no","email_id"])
        
        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_info = input(f"Enter student information for student{student_num} in the format\n(name [space] age [space] phone_no [space] email_id):\n")

        student_info_list  = student_info.split(' ')
        print(f"\nEntered student information is:\nname:{student_info_list[0]}\nage:{student_info_list[1]}\nphone_no:{student_info_list[2]}\nemail_id:{student_info_list[3]}")

        choice_check = input("verify if the details is correct (yes/no): ")

        if choice_check == 'yes':
            convert_csv(student_info_list)
        
            condition_check = input("Do you wish to enter another student details (yes/no) : ")
            if condition_check == 'yes':
                condition = True
                student_num += 1
            elif condition_check == 'no':
                condition = False
            else:
                print("Error Occured")
        elif choice_check == 'no':
            print(f"Please Re-enter the deatils for student{student_num}")

