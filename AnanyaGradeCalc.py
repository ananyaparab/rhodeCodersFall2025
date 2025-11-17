#code to add test scores together
test_list = []
math_test = int(input("What did you score on your math test?: "))
test_list.append(math_test)
science_test = int(input("What grade did you get on your science test?: "))
test_list.append(science_test)
english_test = int(input("What did you get on your english exam?: "))
test_list.append(english_test)
test_total = 0
for x in test_list:
    test_total += x


#code to add homework scores together
hw_list = []
math_hw = int(input("What did you score on your math homework?: "))
hw_list.append(math_hw)
science_hw = int(input("What grade did you get on your science homework?: "))
hw_list.append(science_hw)
english_hw = int(input("What did you get on your english homework?: "))
hw_list.append(english_hw)
hw_total = 0
for x in hw_list:
    hw_total += x


#code to get participation score
participation = int(input("How much did you score for participation?(1-100): "))

#code to get averages
test_avg = test_total / 3
hw_avg = hw_total / 3

#code to get the final scores for each seperate category
test_final = test_avg * 0.5
hw_final = hw_avg * 0.3
participation_final = participation * 0.2

#code to get final number grade
grade = test_final + hw_final + participation_final
print(grade)

#code to transfer number grade into letters
if grade >= 96 and grade <= 100:
    print("A+")
elif grade >= 92:
    print("A")
elif grade >= 90:
    print("A-")
elif grade >= 86:
    print("B+")
elif grade >= 83:
    print("B")
elif grade >= 80:
    print("B-")
elif grade >= 76:
    print("C+")
elif grade >= 73:
    print("C")
elif grade >= 70:
    print("C-")
elif grade >= 66:
    print("D+")
elif grade >= 63:
    print("D")
elif grade >= 60:
    print("D-")
elif grade >= 56:
    print("F+")
elif grade >= 53:
    print("F")
elif grade >= 0:
    print("F-")
else:
    print("Not Valid")