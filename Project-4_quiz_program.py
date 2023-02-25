# this program stores questions in dictionary and display one by one to  the user and ask him to answer and finally calculating the score and displaying to him

quiz_dict={
    "Question_1":{"Question":"What is the capital of India " , "Answer":"Delhi"},
    "Question_2":{"Question":"What is the capital of France " , "Answer":"Paris"},
    "Question_3":{"Question":"What is the capital of Germany " , "Answer":"Berlin"},
    "Question_4":{"Question":"What is the capital of Italy " , "Answer":"Rome"},
    "Question_5":{"Question":"What is the capital of Spain " , "Answer":"Madrid"},
    "Question_6":{"Question":"What is the capital of Portugal " , "Answer":"Lisbon"},
}

score=0

for key,value in quiz_dict.items():
    print(key+"->"+value["Question"]+"\n")  #string concatination requires + operator
    answer=input("type here")

    if answer.lower()==value["Answer"].lower():
        print("correct answer")
        score=score+1
    else:
        print("wrong , the correct answer is :" + value["Answer"])

print("this quiz has ended successfully and you scored",score,"marks")  #string and integer concatinations require comma->","

print("thank you")

