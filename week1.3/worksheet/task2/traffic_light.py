
states = { "red":4, "red_amber":3, "green":5, "amber":3 }

order = ["red", "red_amber", "green", "amber"] 

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

index = 0 
time_in_state = 0

print(f"Time {systime:03} State {state}")

while systime < maxtime:
  systime += 1
  time_in_state += 1
  if time_in_state == states[state]:
     index = (index + 1) % len(order)   
     state = order[index]
     time_in_state = 0

  
  print(f"Time {systime:03} State {state}")


