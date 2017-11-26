class StateManager:
    
    def __init__(self):
        self.states = []

    def isEmpty(self):
        return self.states == []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        return self.states.pop()

    def peek(self):
        return self.states[len(self.states)-1]

    def size(self):
        return len(self.states)

    def set(self, state):
        self.pop()
        self.push(state)
        
    def update(self):
        return self.peek().update()
        
    def render(self, screen):
        self.peek().render(screen)
        
manager = StateManager()    
    
def getManager():
    return manager