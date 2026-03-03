import copy

class Agent:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks  # mutable list

    def __copy__(self):
        print("Shallow copy called!")
        return Agent(self.name, self.tasks)

    def __deepcopy__(self, memo):
        print("Deep copy called!")
        copied_tasks = copy.deepcopy(self.tasks, memo)
        return Agent(self.name, copied_tasks)

    def display(self):
        print(f"Agent: {self.name}, Tasks: {self.tasks}")

# Original agent
original = Agent("Reshma", ["debug", "refactor", "deploy"])

# Shallow copy
shallow = copy.copy(original)
shallow.tasks.append("monitor") # this will affect original as well along with shallow copy

# Deep copy
deep = copy.deepcopy(original)
deep.tasks.append("benchmark") #this will not affect original or shallow copy

# Display all
original.display()  # Affected by shallow copy, here already "monitor" field added even though not added explicitly in original
shallow.display()
deep.display()      # Independent copy