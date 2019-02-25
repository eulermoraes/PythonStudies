"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:


my_file = open('questions.txt','r')
questions_repository = my_file.readlines()
my_file.close()

right_answer = 0

for question in questions_repository:
    q, a = question.strip('\n').split('=')
    answer_user = input('{}='.format(q))
    if answer_user == a:
        right_answer += 1


my_result_file = open('result.txt','w')
my_result_file.write('Your final score is '+str(right_answer)+'/'+str(len(questions_repository))+'.')
my_result_file.close()
