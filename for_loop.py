# # for character in "a tall giraffe":
# #     print(character)


# names = ["Jom", "Mausha", "lindzy"]
# for name in names:
#    print(name)

# for num in range(len(names)):
#     print(names[num])


# print(names[0],len(names))

# for num in range(12):
#     print(num)

students = {"amy":90,"tom":80,"jerry":20,"lucy":30,"charles": 0, "lammy": 60}																								
# for stu in students:																								
#     print(students[stu])		

for stu in students:
    if students[stu] > 80:
        print(stu + " - " + str(students[stu]) + " excellent!")
    elif students[stu] > 60:
        print(stu + " - " + str(students[stu]) + " pass")
    elif students[stu] < 10:
        print(stu + " - " + str(students[stu]) + " bring your parent to school")
    elif students[stu] < 30:
        print(stu + " - " + str(students[stu]) + " you need to work harder")
    elif students[stu] < 60:
        print(stu + " - " + str(students[stu]) + " you need catch up")
    else: print(stu + " - " + str(students[stu]) + " phew, just one more then you'll fail")
# > 80, excellent																								
# > 60 you passed																								
# < 60 you need catch up																								
# < 30 you need to work harder																								
# < 10 bring your parent to school																								
# append the name and score for each print

# amy - 90, you are excellent










