#Pratik Sanjay Belhekar
#Quiz_program
#python 2.7

import sqlite3
import os
import random
input = int(raw_input("1) Enter 1 for creating Quiz OR 2) Enter 2 For Taking Quiz = "))
db_fileName = "quiz.db"
db_Name = "user.db"


'''Create Quiz'''
if input == 1 :
    print "Create Quiz"
    if not os.path.exists(db_fileName):
        with sqlite3.connect(db_fileName) as conn:
            conn.execute("""CREATE TABLE quiz(questions text, answer text, option1 text, option2 text, option3 text);""")
    with sqlite3.connect(db_fileName) as conn:
        no_question = int(raw_input("Enter Total number of questions for quiz = "))
        for i in range(no_question):
            question = raw_input("Enter Question = ")
            ans = raw_input("Enter the answer for Question = ")
            option1= raw_input("Enter option1 = ")
            option2 = raw_input("Enter option2 = ")
            option3 = raw_input("Enter option3 = ")
            conn.execute("INSERT INTO quiz(questions,answer,option1,option2,option3) VALUES(?,?,?,?,?)",(question,ans,option1,option2,option3))
        #result = conn.execute("SELECT * FROM quiz;")
        #for row in result.fetchall():
        #    print row


    '''Take Quiz'''
elif input == 2:
    total_question = 0
    score = 0
    wrong = 0
    wrong_ans = " "
    print "Take a Quiz"
    string_format = "Ques :{}"
    option_format = "       (1) {}  (2) {}  (3) {} (4) {} "
    name = raw_input("Enter Your Name = ")

    #with sqlite3.connect(db_Name) as uconn:
    #    uconn.execute("""CREATE TABLE user(user_name text, attempts integer, score integer, wrong_questions text);""")


    with sqlite3.connect(db_fileName) as qconn:
        cursr = qconn.cursor()
        result = cursr.execute("""SELECT questions,answer,option1,option2,option3 from quiz""")
        for display in result.fetchall():
            total_question = total_question+1
            qu , o1,o2,o3,o4 = display
            print string_format.format(qu)
            print option_format.format(o2,o3,o4,o1)
            ans_in = int(raw_input("Enter the answer = "))
            if ans_in == 4:
                score = score +1
            else:
                wrong = wrong + 1
                wrong_ans = wrong_ans + " " + qu
        if score == total_question:
            wrong_ans = "You Got all question correct!"
            print wrong_ans
            #print name,"your score is ",score
            #print "Questions you gave wrong answer", wrong,wrong_ans


    with sqlite3.connect(db_Name) as usconn:
        user_result = usconn.execute("SELECT * from user WHERE user_name=?",(name,))
        row = user_result.fetchone()
        if row == None:
            usconn.execute("INSERT INTO user(user_name,attempts,score,wrong_questions) VALUES(?,?,?,?)",(name,1,score,wrong_ans))
        else:
            attempts = row[1]+1
            usconn.execute("UPDATE user SET attempts=?, score=?, wrong_questions=? WHERE user_name=?",(attempts,score,wrong_ans,name))
        check_result = usconn.execute("SELECT * FROM user")
        for row in check_result.fetchall():
            print "------------------user---------", row

    '''Handle input Error'''
else:
    print "Enter Correct option"

