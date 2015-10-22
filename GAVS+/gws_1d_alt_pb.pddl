(define (problem gws_1d_alt_pb) 
 	 (:domain gws_1d_alt)  
 	 (:requirements :strips :conditional-effects :negative-preconditions :disjunctive-preconditions) 
 	     (:objects farL farR L R In faraway U UR UL B BR BL farU farB Loc0 Loc1 Loc2 Loc3 Loc4 Loc5 Loc6 Loc7 Loc8 Loc9 Loc10 ) 
 	   (:init (robot_S_position R) (robot_A_position Loc1)) 
 	 (:goal (or 
 	  (robot_S_position faraway) (robot_A_position Loc0)(robot_A_position Loc10))))