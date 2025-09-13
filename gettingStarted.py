### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "9c1caffe164825bb86385a575719a63bf53409db23349d2720670dfed7cb060e"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = "5"
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = "3"
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "Error"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers("In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"))
    print(welcome_assignment_answers("Are encoding and encryption the same? - Yes/No"))
    print(welcome_assignment_answers("Is it possible to decrypt a message without a key? - Yes/No"))
    print(welcome_assignment_answers("Is it possible to decode a message without a key? - Yes/No"))
    print(welcome_assignment_answers("Is a hashed message supposed to be un-hashed? - Yes/No"))
    print(welcome_assignment_answers("What is the SHA256 hashing value of your NYU email and use the answer in your code - "))
    print(welcome_assignment_answers("Is MD5 a secured hashing algorithm? - Yes/No"))
    print(welcome_assignment_answers("What layer of the TCP/IP model does the protocol DNS belong to?"))
    print(welcome_assignment_answers("What layer of the TCP/IP model does the protocol ICMP belong to?"))



#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": DONE
#"Are encoding and encryption the same? - Yes/No": DONE
#"Is it possible to decrypt a message without a key? - Yes/No": DONE
#"Is it possible to decode a message without a key? - Yes/No": DONE
#"Is a hashed message supposed to be un-hashed? - Yes/No": DONE
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ": DONE
#"Is MD5 a secured hashing algorithm? - Yes/No": DONE
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number": DONE
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": DONE