

k = 12

string =  "(define (domain modified_fmcad) \n \t (:requirements :strips :conditional-effects :negative-preconditions :disjunctive-preconditions) \n \t (:constants "
string2 = "(define (problem modified_fmcad_pb) \n \t (:domain modified_fmcad)  \n \t (:requirements :strips :conditional-effects :negative-preconditions :disjunctive-preconditions) \n \t     (:objects "

for x in range(0,k+1):
    string += "s"+str(x)+" "
    string2 += "s"+str(x)+" "

string +=  ") \n \t (:predicates (robot_position ?x) (P0TRAN) )"

string2 += ") \n \t   (:init (robot_position s1)) \n \t (:goal (robot_position s"+str(k)+")) \n \t )"
#system move left precondition and effect
string +=  "\n \t (:action move_S_robot_left \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or"
for x in range(1,k/2):
  string +=  "(robot_position s"+str(x)+")"
string +=  "))\n \t :effect (and"
for x in range(1,k/2):
  string +=  "\t \t (when (robot_position s"+str(x)+") (and (not (P0TRAN)) (robot_position s"+str(x-1)+" )  (not (robot_position s"+str(x)+" )) ))"

#system move right precondition and effect
string +=  ")\n) \n \t (:action move_S_robot_right \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or"
for x in range(k/2,k):
  string +=  "(robot_position s"+str(x)+")"
string +=  "))\n \t :effect (and"
for x in range(k/2,k):
  string +=  "\t \t (when (robot_position s"+str(x)+") (and (not (P0TRAN)) (robot_position s"+str(x+1)+" )  (not (robot_position s"+str(x)+" )) ))"

#system stay precondition and effect
string +=  ")\n) \t (:action move_S_robot_stay \n \t :parameters () \n \t :precondition (and (P0TRAN) \n \t \t (or"
for x in range(0,k+1):
  string +=  "(robot_position s"+str(x)+")"
string +=  "))\n \t :effect (and"
for x in range(0,k+1):
  string +=  "\t \t (when (robot_position s"+str(x)+") (and (not (P0TRAN)) (robot_position s"+str(x)+" ) ))"

#Environment move right precondition and effect
string +=  ")\n) \n \t (:action move_E_robot_right \n \t :parameters () \n \t :precondition (and (not (P0TRAN)) \n \t \t (or"
for x in range(0,k):
  string +=  "(robot_position s"+str(x)+")"
string +=  "))\n \t :effect (and"
for x in range(0,k):
  string +=  "\t \t (when (robot_position s"+str(x)+") (and (P0TRAN) (robot_position s"+str(x+1)+" )  (not (robot_position s"+str(x)+" )) ))"

#Environment stay precondition and effect
string +=  ")\n) \n \t (:action move_E_robot_stay \n \t :parameters () \n \t :precondition (and (not (P0TRAN)) \n \t \t (or"
for x in range(0,k+1):
  string +=  "(robot_position s"+str(x)+")"
string +=  "))\n \t :effect (and"
for x in range(0,k+1):
  string +=  "\t \t (when (robot_position s"+str(x)+") (and (P0TRAN) (robot_position s"+str(x)+" ) ))"
string +=  ")\n) \n)"

f = open('modified_fmcad.pddl' , 'w')
f.write(string)
f.close

f = open('modified_fmcad_pb.pddl' , 'w')
f.write(string)
f.close
