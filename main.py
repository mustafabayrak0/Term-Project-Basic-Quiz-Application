# Mustafa Bayrak
import matplotlib.pyplot as plt
import time
from random import sample


# Registration function
def register(lst_user_name):
    user_name_new = ""
    while len(
            user_name_new) == 0 or "," in user_name_new:  # comma is not allowed because I split items in csv by comma
        print("Enter a new username:")
        user_name_new = input()  # asking new username
        for i in lst_user_name:
            if i[1] == user_name_new:  # checking if this name is taken
                user_name_new = ""
                print("This username is already taken.Try Again.")
                break
            elif "," in user_name_new:
                print("Username cannot contain commas.Try Again")
                break
    print("Registration Successful!")
    lst_user_name.append([1, user_name_new, 0, 120])  # adding new user to the list
    return user_name_new


# Login function
def login(lst_user_name):
    print("Enter your username:")
    user_name_old = input()  # Asking username
    only_user_names = []
    for i in lst_user_name:  # list of usernames
        only_user_names.append(i[1])
    if user_name_old in only_user_names:  # Checking if user has registered before
        print("Login successful!")
    else:
        while user_name_old not in only_user_names:  # If user not registered before
            print("Wrong Username.Try again!")
            user_name_old = input()
        if user_name_old in only_user_names:  # Correct answer after the wrong answers
            print("Login successful!")
    return user_name_old


def read_file(filename):
    file = open(filename, "r", encoding="utf-8")  # open file and read
    lines = file.readlines()  # read lines
    lst_result = []
    for i in lines:
        k = i.rstrip()
        lst_result.append(k.split(","))  # append splited items to the list
    return lst_result


def time_convert(sec):  # this function converts time to minute and second
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    timer = '{:02d}:{:02d}'.format(int(mins), int(sec))
    return timer


def print_questions(questions):
    answer_list_user = []
    asked_questions = sample(questions, 10)
    start = time.time()  # it is the start time of quiz , there is no limitation but faster user wins
    t = 0
    while t < 10:  # while all the questions are not answered
        for i in range(10):
            print(time_convert(time.time() - start))  # print time info when new question printed
            print(
                f"Question {i + 1})\n{asked_questions[i][1]}  \n{asked_questions[i][3]}\n{asked_questions[i][4]}\n{asked_questions[i][5]}\n{asked_questions[i][6]}")
            user_answer = input()
            if user_answer == "A" or user_answer == "B" or user_answer == "C" or user_answer == "D":  # check if answer is appropriate
                answer_list_user.append(user_answer)  # add to list of user's answers
            else:
                control = True
                while control:  # while answer is inappropriate take new input from user
                    print("Wrong Choice.Try Again")
                    user_answer = input()
                    if user_answer == "A" or user_answer == "B" or user_answer == "C" or user_answer == "D":
                        control = False
                if user_answer == "A" or user_answer == "B" or user_answer == "C" or user_answer == "D":
                    answer_list_user.append(user_answer)
            t += 1  # add one after each question
        break
    time_score = time.time() - start  # this is the time score of user
    return answer_list_user, asked_questions, time_score


def check_answers(user_answer_list, list_questions):
    true_counter = 0
    print(2 * "\t" + " Your Answer:" + 1 * "\t" + "True Answer:")  # show true answer and user's answer
    for i in range(10):
        if user_answer_list[i] == list_questions[i][2]:  # check if answer is true
            print(f"{i + 1})True" + 2 * "\t" + f" {user_answer_list[i]}" + 4 * "\t" + f"{list_questions[i][2]}")
            true_counter += 1
            list_questions[i][7] = int(list_questions[i][7])
            list_questions[i][7] += 1  # increasing how many times it was answered correctly

        else:  # If answer is false
            print(f"{i + 1})False" + (
                    3 - len(str(i + 1))) * "\t" + f" {user_answer_list[i]}" + 4 * "\t" + f"{list_questions[i][2]}")
        list_questions[i][8] = int(list_questions[i][8])
        list_questions[i][8] += 1  # increasing how many times it was asked
    print(f"You answered {true_counter} questions correctly!")
    return true_counter, list_questions


# In this function I update users if they get a better score or time
def update_user(filename, lst):
    file = open(filename, "w", encoding="utf-8")  # open file and write
    lst.sort(
        key=lambda l: (-int(l[2]), float(l[3]))
    )
    for i in lst:
        file.write(str(lst.index(i) + 1) + "," + i[1] + "," + str(i[2]) + "," + str(i[3]) + "\n")  # writing new info
    file.close()


# In this function updating info of how many times the question were asked and answered correctly
def update_questions(filename, lst):
    file = open(filename, "w", encoding="utf-8")  # open file and write
    for i in lst:
        file.write(str(
            str(i[0]) + "," + str(i[1]) + "," + i[2] + "," + i[3] + "," + i[4] + "," + i[5] + "," + i[
                6] + "," + str(i[7]) + "," + str(i[8]) + "\n"))  # writing new info
    file.close()


if __name__ == "__main__":
    print("1)Register")
    print("2)Login")
    user_name_lst = read_file("usernames.csv")  # read usernames.csv
    user_choice = input()
    if user_choice == "1":
        active_user = register(user_name_lst)  # I check which user is playing

    elif user_choice == "2":
        active_user = login(user_name_lst)  # I check which user is playing
    else:
        while user_choice != "1" and user_choice != "2":  # If not an appropriate answer
            print("Wrong Choice.Try again!")
            user_choice = input()
        if user_choice == "1":
            active_user = register(user_name_lst)  # I check which user is playing
        else:
            active_user = login(user_name_lst)  # I check which user is playing
    questions_list = read_file("questions.csv")  # read questions.csv
    user_answers_list, asked_questions, time_score = print_questions(
        questions_list)  # taking info of user's answers and which questions asked
    true_answer_count, updated_questions = check_answers(user_answers_list,
                                                         asked_questions)  # I take number of true answer and how many times the questions were asked and answered correctly
    for i in user_name_lst:
        if len(i) == 4:  # To avoid empty lists
            if active_user == i[1]:
                if true_answer_count >= int(i[2]) and time_score < float(
                        i[3]):  # If it is best score of user, then update it
                    i[2] = true_answer_count
                    i[3] = time_score  # changing max score
                    break
    update_user("usernames.csv", user_name_lst)  # writing new list to usernames.csv
    for i in questions_list:  # Here I change values of questions if they are asked
        for j in updated_questions:
            if i[0] == j[0]:  # if they are same questions
                i[7] = j[7]  # giving new values
                i[8] = j[8]  # giving new values
                break

    update_questions("questions.csv",
                     questions_list)  # Updating info of how many times the question were asked and answered correctly
    print("")  # adding one empty line
    print("Ranking Table:")
    print("Rank,Username,Score,Time")  # printing order of information
    for i in user_name_lst:
        print(f"{i[0]}.{i[1]}, {i[2]}", ",", time_convert(float(i[3])))
    fig = plt.figure(figsize=(7, 5))
    # It calculates rate of correct answers
    graph_rates = []
    for i in range (10):
        graph_rates.append(int(asked_questions[i][7]) / int(asked_questions[i][8]) * 100)
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.title("Rate of questions answered correctly by other users")
    plt.bar(positions, graph_rates, width=0.5, color="g")
    plt.show()        
    # library codes are used


