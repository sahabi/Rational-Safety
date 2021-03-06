(define (problem gws_1d_pb) 
 	 (:domain gws_1d)  
 	 (:requirements :strips :conditional-effects :negative-preconditions :disjunctive-preconditions) 
 	     (:objects s0 e0 s1 e1 s2 e2 s3 e3 s4 e4 s5 e5 s6 e6 s7 e7 s8 e8 s9 e9 s10 e10 ) 
 	   (:init (robot_S_position s1) (robot_E_position e1)) 
 	 (:goal (or 
 	 (and (not(P0TRAN)) (robot_E_position e0) (not(robot_S_position s0)))
(and (not(P0TRAN)) (robot_E_position e1) (not(robot_S_position s1)))
(and (not(P0TRAN)) (robot_E_position e2) (not(robot_S_position s2)))
(and (not(P0TRAN)) (robot_E_position e3) (not(robot_S_position s3)))
(and (not(P0TRAN)) (robot_E_position e4) (not(robot_S_position s4)))
(and (not(P0TRAN)) (robot_E_position e5) (not(robot_S_position s5)))
(and (not(P0TRAN)) (robot_E_position e6) (not(robot_S_position s6)))
(and (not(P0TRAN)) (robot_E_position e7) (not(robot_S_position s7)))
(and (not(P0TRAN)) (robot_E_position e8) (not(robot_S_position s8)))
(and (not(P0TRAN)) (robot_E_position e9) (not(robot_S_position s9)))
)))