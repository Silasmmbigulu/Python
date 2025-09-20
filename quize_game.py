#pyhton quize game

questions = [
     {
        "question": "How many progrmming languanges are used in the current world?:",
        "options": ["A. 15", "B. 20", "C. 17", "D. 13"],
        "answer": "C"
     },

     {
        "question": "Which is the mostly used programming language?:",  
        "options": ["A. Python", "B. Simula", "C. Small_talk", "D. Java"],
        "answer": "A"
     },

     {
        "question": "Which is the most abandunt gas in earth's atmosphere?:",
        "options": ["A. Oxygen", "B. Hydrogen", "C. Chlorine", "D. Flourine"],
        "answer": "A"
     },

     {
        "question": "How many languages are used for web development?:",
        "options": ["A. 7","B. 8", "C. 9", "D. 6"],
        "answer": "7"
     },

     {
          "question": "Who is regarded as the further of modern computing?:",
          "options": ["A.Elon Musk","B.Bill Gates", "C.Charles Babbage", "D.Donald Trump"],
          "answer": "C"
     }             
]

score = 0  
guesses = ()
answer = {}
#the variable q is each dictionery in turn
for q in questions:
     print("               ")
     print(q["question"])

     for option in q["options"]:
          print(option)
          
          guess = input("Enter (A, B, C or D):").upper()

          if guess == q["answer"]:
                  print("CORRECT!")
                  score += 1
          else:
               print("INCORRECT!")
               print(f"the correct answer was {q['answer']}.")
          
        

print("                              ")
print("           RESULT            ")
print("                             ")

 
       
score = int(score / len(questions) * 100)
print(score)
