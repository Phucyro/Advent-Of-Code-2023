def main():
    part1()
    part2()

def part1():
    calibration_values = []

    with open('input.txt', 'r') as file:
        for line in file:
            number_list = []
            for char in line:
                if char.isdigit():
                    number_list.append(char)
            
            calibration = number_list[0] + number_list[len(number_list)-1]
            calibration_values.append(int(calibration))
    
    sum = 0
    for value in calibration_values:
        sum += value
    print("Part 1: {}".format(sum))

def part2():
    numberDict = {
        "one" : "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    calibration_values = []

    with open('input.txt', 'r') as file:
        index = 1
        for line in file:
            number_list = []
            potential_number = ""
            for char in line:
                if not char.isdigit():
                    potential_number += char 
                    
                    for i in range(len(potential_number)):
                        test_number = ""
                        for y in range(i,len(potential_number)):
                            test_number += potential_number[y]
                        if test_number in numberDict:
                            number_list.append(numberDict[test_number])
                            potential_number = ""
                            break
                else:
                    number_list.append(char)
                    potential_number = ""
            print("index :" + str(index))
            print(number_list)

            if (len(number_list) > 1):
                calibration = number_list[0] + number_list[len(number_list)-1]
            elif (len(number_list) == 1):
                calibration = number_list[0] + number_list[0]
            print(calibration)
            

            calibration_values.append(int(calibration))
            index += 1

    

    sum = 0
    for value in calibration_values:
        sum += value
    print("Part 2: {}".format(sum))     

if __name__ == "__main__":
    main()
