import turtle


# http://paulbourke.net/fractals/lsys/
class LSystem:

  def __init__(self, depth = 1, rules = {}, axiom = "", length = 30, angle = 0, actions = {}):
    self.depth = depth
    self.rules = rules
    self.axiom = axiom
    self.length = length
    self.angle = angle
    self.actions = actions

    self.turtle = turtle.Turtle()
    self.turtle.speed(10)
    self.turtle.setheading(90)

    ts = self.turtle.getscreen()
    ts.screensize(4000, 4000)
    ts.setup(width=1.0, height=1.0, startx=None, starty=None)

  def draw(self):
    instruction = self.axiom
    print(instruction)

    for current_depth in range(self.depth):
      
      inst_length = len(instruction)
      c_index = 0
      while c_index < inst_length:

        c = instruction[c_index]
        if (c in self.rules):
          replacement_inst = self.rules[c]
   
          instruction = instruction[:c_index] + \
                        replacement_inst + \
                        instruction[(c_index + 1):]

          inst_length = len(instruction)
          c_index += (len(replacement_inst))
        else:
          c_index += 1

    print("Final: ", instruction)

    saved_states = []

    for command in instruction:
      if command in self.actions:
        self.actions[command](self.turtle, self.length, self.angle, saved_states)

    # call mainloop to let the graphics window stay open after the turtle has finished drawing
    turtle.mainloop()


def forward(t, length, angle, saved_states):
    t.color('black')
    t.forward(length)

def leaf(t, length, angle, saved_states):
    t.color('red')
    t.forward(length)

def turn_left(t, length, angle, saved_states):
    t.left(angle)

def turn_right(t, length, angle, saved_states):
    t.right(angle)

def push(t, length, angle, saved_states):
    saved_states.append((t.pos(), t.heading()))

def pop(t, length, angle, saved_states):
    pos, angle = saved_states.pop()
    t.penup()
    t.setpos(pos)
    t.setheading(angle)
    t.pendown()

def push_and_turn_left(t, length, angle, saved_states):
    push(t, length, angle, saved_states)
    turn_left(t, length, angle, saved_states)

def pop_and_turn_right(t, length, angle, saved_states):
    pop(t, length, angle, saved_states)
    turn_right(t, length, angle, saved_states)


# variables : 0, 1
# constants: “[”, “]”
# axiom  : 0
# rules  : (1 → 11), (0 → 1[0]0)
def run_example_1():
    tree_system = \
        LSystem(depth = 7, rules = { "1" : "11", "0" : "1[0]0" }, axiom = "0", angle = 45, length = 15,
            actions = { 
                "1" : forward, "0" : leaf, 
                "[" : push_and_turn_left, "]" : pop_and_turn_right 
            }
        )
    tree_system.draw()

# axiom = FX
# X -> [-FX]+FX
# angle = 40
def run_example_2():
    tree_system = LSystem(depth = 2, rules = { "X" : "[-FX]+FX" }, axiom = "FX", length = 30, angle = 40, 
        actions = {
                "F" : forward, "X" : leaf, 
                "-" : turn_left, "+" : turn_right, 
                "[" : push, "]" : pop 
        }
    )
    tree_system.draw()

# axiom = X
# F -> FF
# X -> F[+X]F[-X]+X
# angle = 20
def run_example_3():
    tree_system = LSystem(depth = 5, rules = { "F" : "FF", "X" : "F[+X]F[-X]+X" }, axiom = "X", length = 30, angle = 20, 
        actions = { 
            "F" : forward, "X" : leaf, 
            "-" : turn_left, "+" : turn_right, 
            "[" : push, "]" : pop 
        }
    )
    tree_system.draw()

def run_example_4():
    tree_system = LSystem(depth = 2, rules = { "F" : "F+F-F-FF+F+F-F" }, axiom = "F+F+F+F", length = 30, angle = 90,
        actions = { "F" : forward, "-" : turn_left, "+" : turn_right })
    tree_system.draw()

