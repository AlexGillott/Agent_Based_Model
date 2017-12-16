# Final model for GEOG5990M online portfolio. Model created in practical
# sessions during the 1st semester.

"""
Create agents to interact with each other and their environment.

Build agents in random location in environment. Give agents list of 
other agents. Move agents around environment. Agents eat environment
and Agents communicate with nearby agents. Share resources with
neighbours. Display the environment in animation.

Arguments: 
num_of_agents = Number of Agents in the model
num_of_iterations = Number of steps agents move
neighbourhood = Distance around each agent. If other agents within this
                distance communicate and share resources.

Returns:
Animation of inputted agents interacting with the environment. 
"""

# importing modules
import requests
import csv
import random
import datetime

import bs4
import tkinter
import matplotlib
import matplotlib.backends.backend_tkagg
import matplotlib
import matplotlib.pyplot
import matplotlib.animation

import agentframework

# Web scraping
r = requests.get\
("http://www.geog.leeds.ac.uk/courses/computing/practicals/python/\
agent-framework/part9/data.html")
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


# Function for getting time
def getTimeMS():
    """
    Record length of time for code to run.
    
    Returns:
    Length of time code took to run.
    """
    dt = datetime.datetime.now()
    return dt.microsecond + (dt.second * 1000000) + \
    (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)
    
start = getTimeMS()

# Start of Agent Based Modelling code

# Import csv file
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)
 

# Creating number of agents, iterations and neighbourhood variables
num_of_agents = 10
num_of_iterations = 10
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Make the agents
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, neighbourhood,\
                                         y, x))
    

# 1st part of stopping condition code. Continued line ""
carry_on = True    
    
def update(frame_number):
    """
    Create frames for animation.
    
    Argument:
    frame_number
    
    Returns:
    A frame for each iteration of the model.
    """
    fig.clear()
    global carry_on

    # Moving agents   
    for j in range(num_of_iterations):
        random.shuffle(agents)
        
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
            
    # Stopping condition    
    total = 0    
    for agent in agents:
        total += agent.store
    if total >= 100000 :
        carry_on = False
        print ("stopping conditon met")

  
    # plotting co-ordinates
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].x,agents[i].y)
     
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)    
    matplotlib.pyplot.imshow(environment)


# For stopping condition to work.
def gen_function(b = [0]): 
    """
    Stop model when a < num_of_interations and carry_on = false.
    
    Requires no setup
    """
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			
        a = a + 1

    # Total amount stored by agents saved to file "store.txt"
    total = 0

    for agent in agents:
        total +=agent.store
    
    with open('store.txt', 'a') as f3:
        f3.write (str(total) + "\n")
        
    # Write out the enviroment as a file
    f2 = open('Environment.txt', 'w', newline='')
    writer = csv.writer(f2, delimiter=',')
    for row in environment:
        writer.writerow(row)
    f2.close()

# Function to run model animation
def run():
    """
    Run the animation.
    
    Requires no setup
    """
    animation = matplotlib.animation.FuncAnimation(fig, update,\
                frames=gen_function, repeat=False)
    canvas.show()

# Main window GUI
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 


# End of Agent Based Modelling code

# Second part of get time code
end = getTimeMS()
print ("time =" + str(end - start))

# Proving that list of agents put into each agent
print (agents[2])
print (num_of_iterations)

   
tkinter.mainloop()