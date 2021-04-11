  if(instruction =="L"):
        new_waypoint =[0,0,0,0]
        new_waypoint[0]=waypoint[1]
        new_waypoint[1]=waypoint[2]
        new_waypoint[2]=waypoint[3]
        new_waypoint[3]=waypoint[0]
        waypoint = new_waypoint
      else:
        new_waypoint = [0,0,0,0]
        new_waypoint[1] = waypoint[0]
        new_waypoint[2] = waypoint[1]
        new_waypoint[3] = waypoint[2]
        new_waypoint[0] = waypoint[3]
        waypoint = new_waypoint