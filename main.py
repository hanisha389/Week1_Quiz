name = input("Enter Your name : ")
print("\n \nHello " +name+ ", Welcome to the Decision Making Style Assessment ! ")

print("\n \n ----------------------------------START QUIZ----------------------------------")

#scoring Initialisation
Analyst = 0 
Empath = 0
Leader = 0
Reflector = 0
max_score = 0

#questions starts
print("\n1. You are given limited time to complete an important task. You:")
print("A) Break it into smaller logical steps and plan carefully")
print("B) Check how others are handling the pressure")
print("C) Take charge and push forward quickly")
print("D) Feel unsure whether the work is good enough yet")
while True:
    Answer= input("\nEnter your option :").upper()
    if Answer == "A":
        print ("You choose option ", Answer)
        Analyst +=2 
        break
    elif Answer == "B":
        print ("You choose option ", Answer)
        Empath +=2
        break
    elif Answer == "C":
        print ("You choose option ", Answer)
        Leader +=2
        break
    elif Answer == "D":
        print ("You choose option ", Answer)
        Reflector +=2
        break
    else :
        print("Invalid Option, Please enter again!!!")



print("\n2. You are offered an opportunity outside your comfort zone. You:")
print("A) Research thoroughly before saying yes")
print("B) Think about how it may impact people around you")
print("C) Accept it confidently and adapt along the way")
print("D) Delay the decision until you feel completely prepared")
while True:
    Answer= input("\nEnter your option :").upper()
    if Answer == "A":
        print ("You choose option ", Answer)
        Analyst +=2 
        break
    elif Answer == "B":
        print ("You choose option ", Answer)
        Empath +=2
        break
    elif Answer == "C":
        print ("You choose option ", Answer)
        Leader +=2
        break
    elif Answer == "D":
        print ("You choose option ", Answer)
        Reflector +=2
        break
    else :
        print("Invalid Option, Please enter again!!!")
        

print("\n3. After receiving constructive criticism, you:")
print("A) Analyse the feedback logically")
print("B) Reflect on how it was communicated emotionally")
print("C) Use it as immediate motivation to improve")
print("D) Replay the situation multiple times in your mind")
while True:
    Answer= input("\nEnter your option :").upper()
    if Answer == "A":
        print ("You choose option ", Answer)
        Analyst +=2 
        break
    elif Answer == "B":
        print ("You choose option ", Answer)
        Empath +=2
        break
    elif Answer == "C":
        print ("You choose option ", Answer)
        Leader +=2
        break
    elif Answer == "D":
        print ("You choose option ", Answer)
        Reflector +=2
        break
    else :
        print("Invalid Option, Please enter again!!!")
 
print("\n4. Two team members strongly disagree on an idea. You:")
print("A) Suggest a structured solution based on facts")
print("B) Try to ease emotional tension between them")
print("C) Make a firm decision to move forward")
print("D) Observe quietly before giving your opinion")
while True:
    Answer= input("\nEnter your option :").upper()
    if Answer == "A":
        print ("You choose option ", Answer)
        Analyst +=2 
        break
    elif Answer == "B":
        print ("You choose option ", Answer)
        Empath +=2
        break
    elif Answer == "C":
        print ("You choose option ", Answer)
        Leader +=2
        break
    elif Answer == "D":
        print ("You choose option ", Answer)
        Reflector +=2
        break
    else :
        print("Invalid Option, Please enter again!!!")

    
print("\n5. Under pressure, you:")
A=print("A) Stay calm and analytical")
B=print("B) Become sensitive to others reactions")
C=print("C) Take control of the situation")
D=print("D) Overthink possible consequences") 
while True:
    Answer= input("\nEnter your option :").upper()
    if Answer == "A":
        print ("You choose option ", Answer)
        Analyst +=2 
        break
    elif Answer == "B":
        print ("You choose option ", Answer)
        Empath +=2
        break
    elif Answer == "C":
        print ("You choose option ", Answer)
        Leader +=2
        break
    elif Answer == "D":
        print ("You choose option ", Answer)
        Reflector +=2
        break
    else :
        print("Invalid Option, Please enter again!!!")

max_score = max(Analyst,Empath,Leader,Reflector)

#ActualLogic
max_score = max(Analyst, Empath, Leader, Reflector)

print("\n\n----------------------------------RESULT----------------------------------")

if Analyst == max_score:
    print("\nYou are primarily an ANALYST\n")
    print("Description:")
    print("You make decisions using logic, structure, and facts.")
    print("You prefer clarity, organized thinking, and well-evaluated pros and cons before acting.")
    print("People see you as rational, calm, and solution-focused.\n")
    print("Strengths:")
    print("- Strong critical thinking")
    print("- Objective decision-making")
    print("- Excellent problem solver\n")
    print("Improvement Suggestion:")
    print("Try to consider emotional factors occasionally.")
    print("Not every decision is purely logical — understanding feelings can strengthen your effectiveness.")

elif Empath == max_score:
    print("\nYou are primarily an EMPATH\n")
    print("Description:")
    print("You prioritize emotions and relationships when making decisions.")
    print("You care deeply about how choices affect others.")
    print("People trust you for your understanding and compassion.\n")
    print("Strengths:")
    print("- High emotional intelligence")
    print("- Strong listener")
    print("- Builds harmony in teams\n")
    print("Improvement Suggestion:")
    print("Be careful not to ignore logic for the sake of emotions.")
    print("Balanced decisions combine both heart and mind.")

elif Leader == max_score:
    print("\nYou are primarily a LEADER\n")
    print("Description:")
    print("You take charge confidently and act quickly.")
    print("You are comfortable making bold decisions and guiding others forward.")
    print("You perform well under pressure and uncertainty.\n")
    print("Strengths:")
    print("- Decisive and action-oriented")
    print("- Confident under pressure")
    print("- Motivates others\n")
    print("Improvement Suggestion:")
    print("Pause occasionally before acting.")
    print("Gathering input and analyzing risks can improve decision quality.")

elif Reflector == max_score:
    print("\nYou are primarily a REFLECTOR\n")
    print("Description:")
    print("You think deeply before making decisions.")
    print("You evaluate multiple perspectives and prefer careful consideration.")
    print("Your thoughtful nature reduces impulsive mistakes.\n")
    print("Strengths:")
    print("- Deep thinker")
    print("- Careful evaluator")
    print("- Self-aware and observant\n")
    print("Improvement Suggestion:")
    print("Avoid excessive overthinking.")
    print("Sometimes progress comes from taking action, not waiting for perfection.")

print("\nThank you for taking the Decision Making Style Assessment,", name ,"!")

#OUTPUT