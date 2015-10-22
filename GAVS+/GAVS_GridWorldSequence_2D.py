
k = 4
X = k
Y = k
states = X*Y

string =  "(define (domain gws_2d) \n \t (:requirements :strips :conditional-effects :negative-preconditions :disjunctive-preconditions) \n \t (:constants " 
string2 = "(define (problem gws_2d_pb) \n \t (:domain gws_2d)  \n \t (:requirements :strips :conditional-effects :negative-preconditions :disjunctive-preconditions) \n \t     (:objects "
for x in range(0, X*Y):
    string +=  "s"+str(x)+" "
    string +=  "e"+str(x)+" "
    string2 +=  "s"+str(x)+" "
    string2 +=  "e"+str(x)+" "


string +=  ") \n \t (:predicates (robot_S_position ?x) (robot_E_position ?x) (P0TRAN) )"

string2 += ") \n \t   (:init (robot_S_position s1) (robot_E_position e1)) \n \t (:goal (or \n \t "

for i in range(0,(X*Y)):
  string2 += "(and (not(P0TRAN)) (robot_E_position e"+str(i)+") (not(robot_S_position s"+str(i)+")))\n"
string2 += ")))"
#Env move left precondition and effect
string +=  "\n \t (:action move_S_robot_left \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or" 

for i in range(0, Y):
  for x in range(1, X):
    if ((x+(i*Y))%Y != 0 ):
        string +=  "(robot_S_position s"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(1, X):
    if ((x+(i*Y))%Y != 0 ):
      string +=  "\t \t (when (robot_S_position s"+str(x+(i*Y))+") (and (not (P0TRAN)) (robot_S_position s"+str((x+(i*Y))-1)+" )  (not (robot_S_position s"+str((x+(i*Y)))+" )) ))"

#Env move up precondition and effect
string +=  ")\n) \n \t (:action move_S_robot_up \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or" 
for i in range(0, Y):
  for x in range(0, X):
    if (i != Y ):
        string +=  "(robot_S_position s"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(0, X):
    if (i != Y-1 ):
      string +=  "\t \t (when (robot_S_position s"+str(x+(i*Y))+") (and (not (P0TRAN)) (robot_S_position s"+str((x+(i*Y))+Y)+" )  (not (robot_S_position s"+str((x+(i*Y)))+" )) ))"

#Env move down precondition and effect
string +=  ")\n) \n \t (:action move_S_robot_down \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or" 
for i in range(0, Y):
  for x in range(0, X):
    if (i != 0 ):
        string +=  "(robot_S_position s"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(0, X):
    if (i != 0 ):
      string +=  "\t \t (when (robot_S_position s"+str(x+(i*Y))+") (and (not (P0TRAN)) (robot_S_position s"+str((x+(i*Y))-Y)+" )  (not (robot_S_position s"+str((x+(i*Y)))+" )) ))"


#Env move right precondition and effect
string +=  ")\n) \n \t (:action move_S_robot_right \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or" 
for i in range(0, Y):
  for x in range(0, X):
    string +=  "(robot_S_position s"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(0, X):
    if ((x+(i*Y))%Y != Y-1 ):
        string +=  "\t \t (when (robot_S_position s"+str(x+(i*Y))+") (and (not (P0TRAN)) (robot_S_position s"+str((x+(i*Y))+1)+" )  (not (robot_S_position s"+str(x+(i*Y))+" )) ))"

#Env stay precondition and effect
string +=  ")\n) \t (:action move_S_robot_stay \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or" 
for i in range(0, Y):
  for x in range(0, X):
    string +=  "(robot_S_position s"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(0, X):
    string +=  "\t \t (when (robot_S_position s"+str(x+(i*Y))+") (and (not (P0TRAN)) (robot_S_position s"+str(x+(i*Y))+" ) ))"

#Env move left precondition and effect
string +=  ")\n)\n \t (:action move_E_robot_left \n \t :parameters () \n \t :precondition (and (not (P0TRAN))  \n \t \t (or" 

for i in range(0, Y):
  for x in range(0, X):
    if ((x+(i*Y))%Y != 0 ):
        string +=  "(robot_E_position e"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(0, X):
    if ((x+(i*Y))%Y != 0 ):
        string +=  "\t \t (when (robot_E_position e"+str(x+(i*Y))+") (and (P0TRAN) (robot_E_position e"+str((x+(i*Y))-1)+" )  (not (robot_E_position e"+str((x+(i*Y)))+" )) ))"

#Env move right precondition and effect
string +=  ")\n) \n \t (:action move_E_robot_right \n \t :parameters () \n \t :precondition (and (not (P0TRAN))  \n \t \t (or" 
for i in range(0, Y):
  for x in range(0, X):
    if ((x+(i*Y))%Y != Y-1 ):
        string +=  "(robot_E_position e"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(0, X):
    if ((x+(i*Y))%Y != Y-1 ):
        string +=  "\t \t (when (robot_E_position e"+str(x+(i*Y))+") (and (P0TRAN) (robot_E_position e"+str((x+(i*Y))+1)+" )  (not (robot_E_position e"+str(x+(i*Y))+" )) ))"

#Env stay precondition and effect
string +=  ")\n) \t (:action move_E_robot_stay \n \t :parameters () \n \t :precondition (and (not (P0TRAN))  \n \t \t (or" 
for i in range(0, Y):
  for x in range(0, X):
    string +=  "(robot_E_position e"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(0, X):
    string +=  "\t \t (when (robot_E_position e"+str(x+(i*Y))+") (and (P0TRAN) (robot_E_position e"+str(x+(i*Y))+" ) ))"


#Env move up precondition and effect
string +=  ")\n) \n \t (:action move_E_robot_up \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or" 
for i in range(0, Y):
  for x in range(0, X):
    if (i != Y ):
        string +=  "(robot_E_position e"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(0, X):
    if (i != Y-1 ):
      string +=  "\t \t (when (robot_E_position e"+str(x+(i*Y))+") (and (not (P0TRAN)) (robot_E_position e"+str((x+(i*Y))+Y)+" )  (not (robot_E_position e"+str((x+(i*Y)))+" )) ))"

#Env move down precondition and effect
string +=  ")\n) \n \t (:action move_E_robot_down \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or" 
for i in range(0, Y):
  for x in range(0, X):
    if (i != 0 ):
        string +=  "(robot_E_position e"+str(x+(i*Y))+")" 
string +=  "))\n \t :effect (and"
for i in range(0, Y):
  for x in range(0, X):
    if (i != 0 ):
      string +=  "\t \t (when (robot_E_position e"+str(x+(i*Y))+") (and (not (P0TRAN)) (robot_E_position e"+str((x+(i*Y))-Y)+" )  (not (robot_E_position e"+str((x+(i*Y)))+" )) ))"

string +=  ")))"

f = open('gws_2d.pddl' , 'w')
f.write(string)
f.close

f = open('gws_2d_pb.pddl' , 'w')
f.write(string2)
f.close