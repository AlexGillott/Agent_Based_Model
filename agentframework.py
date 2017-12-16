import random

# Defining an agent class

class Agent():
    """
    Create the agent class and move and interact with environment.
    
    Create agents, position them randomly within the environment. Move
    around the environment, interact with environment and communicate
    with other agents.
    """
    def __init__ (self, environment, agents, neighbourhood, y = None, x = None):
        """
        Defines environment, agents, neighbourhood and initial 
        co-ordinates.
        
        Arguments:
        environment = (float:list) Area that agents move and interact 
        in.
        agents = (int) List of agents.
        neighbourhood = (int) If other agents within this area of an
                        will communicate.
        y = (int) starting position of none.
        x = (int) starting position of none.
        
        Returns:
        environment = (float:list), written in from CSV file.
        agents = (int) List of agents, number determined from 
                 num_of_agents variable in model.py.
        neighbourhood = Size determined from neighbourhood variable in
                        model.py.
        y = (int) Random number between 0 and 100.
        x = (int) Random number between 0 and 100.
        """
        self.environment = environment
        self.agents = agents
        self.neighbourhood = neighbourhood
        self.store = 0
        
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
            
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y

    # Agents changing the environment ("eating" it)        
    def eat(self):
        """
        Agents to eat the environment if environment value over 10.
        
        Arguments:
        Environment values (from CSV file)
        
        Returns:
        Changed environment values.
        Units added to agent store.
        """
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
            
    # Sharing with neighbours        
    def share_with_neighbours (self, neighbourhood):
        """
        Share store with neighbouring agents.
        
        Look at the distance between agents. If distance less than
        neighbourhood variable average sum of both agents stores. Set 
        both agents stores to average of the two stores.
        
        Arguments:
        Distance - (float) Distance between the agents.
        Neighbourhood - (int) Variable determined in model.py.
        Self store - (int) Number of units stored.
        Agents store - (int) Number of units stored.
        
        Returns:
        Distance - (float) Distance between the agents.
        Neighbourhood - (int) Action if distance less than neighbourhood
                        variable.
        Self and agents store - (int) Sum of self and agents store.
        Self store - (int) Average of self and agents store.
        Agents store - (int) Average of self and agents store.
        
        """
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
   
    # Distance between agents             
    def distance_between(self, agent):
        """
        Determine distance between agents.
        
        Use pythagoras euclidean formula to determine distance between
        agents.
        
        Arguments:
        agent x - position
        agent y - position
        
        Returns:
        Distance between agent x and agent y
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
            
    # Get and set    
    def getx(self):
        """
        Get the value for x (int).
        
        Argument:
        Get the x value (int).
        
        Return:
        _x value (int).
        """
        return self._x
        
    
    def gety(self):
        """
        Get the value for y (int).
        
        Argument:
        Get the y value (int).
        
        Return:
        _y value (int).
        """
        return self._y
    
    def setx(self, value):
        """
        Set value of x as read only.
        
        Argument:
        _x (int) value.  
        
        Return:
        _x value as read only.
        """
        self._x = value
        
    def sety(self, value):
        """
        Set value of y as read only.
        
        Argument:
        _y (int) value.  
        
        Return:
        _y value as read only.
        """
        self._y = value

    x = property(getx, setx, "I'm the 'x' property.")
    y = property(gety, sety, "I'm the 'y' property.")
    
# moving the agents
    def move (self):
        """
        Move the agent x and y co-ordinates randomly.
        
        X and y co-ordinates moved randomly within the environment and 
        kept within the boundary using torus method.
        
        Arguments:
        y = Random number.
        x = random number.
        
        Returns:
        y = if random number < 0.5 + 1, if random number > 0.5 - 1.
        x = if random number < 0.5 + 1, if random number > 0.5 - 1.
        """
        
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        
        
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
            
