from app.database import add_goal
from app.objects import Goal

# food, car, home, kids, fun, health, other: oszczędzanie (budżet domowy)
# challenges: travel, dining out, tech gadgets, fashion
# challenge to są wybrane, że jak zaoszczędzisz to oszczędności so rozdysponowane pomiędzy wybrane challenge

add_goal(Goal(user_id=7, spent_money=0.0, category="food"))
add_goal(Goal(user_id=7, spent_money=0.0, category="car"))
add_goal(Goal(user_id=7, spent_money=0.0, category="home"))
add_goal(Goal(user_id=7, spent_money=0.0, category="kids"))
add_goal(Goal(user_id=7, spent_money=0.0, category="fun"))
add_goal(Goal(user_id=7, spent_money=0.0, category="health"))
add_goal(Goal(user_id=7, spent_money=0.0, category="other"))
