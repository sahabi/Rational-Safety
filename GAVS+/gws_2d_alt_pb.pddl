(define (problem gws_2d_alt_pb) 
 	 (:domain gws_2d_alt)  
 	 (:requirements :strips :conditional-effects :negative-preconditions :disjunctive-preconditions) 
 	     (:objects farL farR L R In faraway U UR UL B BR BL farU farB Loc0 Loc1 Loc2 Loc3 Loc4 Loc5 Loc6 Loc7 Loc8 Loc9 Loc10 Loc11 yLoc0 yLoc1 yLoc2 yLoc3 yLoc4 yLoc5 yLoc6 yLoc7 yLoc8 yLoc9 yLoc10 yLoc11 ) 
 	   (:init (robot_S_position R) (robot_A_position Loc1)(robot_B_position yLoc1)) 
 	 (:goal (or 
 	  (robot_S_position faraway) (robot_A_position Loc0)(robot_A_position Loc11)(robot_B_position yLoc0)(robot_B_position yLoc11))))