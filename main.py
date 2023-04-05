# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = f'{scorer_1} {str(goal_0)}, {scorer_2} {str(goal_1)}'
report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'
player = "Jan Wouters"
x = player.find(" ")
first_name = player[0:x]
last_name = player[x+1:]
last_name_len = len(last_name)
first_name_len = len(first_name)
name_short = f'{player[0]}. {last_name}'
chant_with_space = f'{first_name}! ' * first_name_len
chant = chant_with_space[:-1]
good_chant = chant[-1] != " "

