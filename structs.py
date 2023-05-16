import json

class command:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

class history:
    def __init__(self):
        self.current_node = None
        self.first_node = None
        self.last_node = None
        self.all_commands = []
        self.position = 0

    def add(self, data):
        new_node = command(data)

        if self.first_node is None:
            self.first_node = new_node

        if self.current_node is not None:
            self.current_node.next_node = new_node
            new_node.previous_node = self.current_node

        self.current_node = new_node
        self.last_node = new_node
        self.all_commands.append(data)

    def get_last(self):
        if self.last_node is None:
            return "Pas d'historique"

        return self.last_node.data

    def get_all(self):
        if self.first_node is None:
            return "Pas d'historique"

        commands = []
        current_node = self.first_node
        while current_node is not None:
            commands.append(current_node.data)
            current_node = current_node.next_node

        return commands

    def move_forward(self):
        if self.current_node is None:
            return

        if self.current_node.next_node is not None:
            self.current_node = self.current_node.next_node
        else:
            return "Fin de l'historique"

        return self.current_node.data

    def move_backward(self):
        if self.current_node is None:
            return

        if self.current_node.previous_node is not None:
            self.current_node = self.current_node.previous_node
        else:
            return "Début de l'historique"

        return self.current_node.data

    def clear(self):
        self.current_node = None
        self.first_node = None
        self.last_node = None
        self.all_commands.clear()

    def to_dict(self):
        commands = []
        current_node = self.first_node
        while current_node is not None:
            commands.append(current_node.data)
            current_node = current_node.next_node

        return {
            "commands": commands,
            "current_position": self.position
        }
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def from_dict(cls, data):
        command_history = cls()
        for command in data["commands"]:
            command_history.add(command)
        command_history.position = data["current_position"]

        return command_history
    
    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        history = cls.from_dict(data)
        return history

class User:
    def __init__(self, id):
        self.id = id
        self.command_history = history()

class UserHashMap:
    def __init__(self, length):
        self.datas = []
        for i in range(length):
            self.datas.append([])

    def add_user(self, id):
        hashed_key = hash(id)
        indice = hashed_key % len(self.datas)
        self.datas[indice].append((id, User(id)))

    def get_user(self, id):
        hashed_key = hash(id)
        indice = hashed_key % len(self.datas)
        for key_datas, value_datas in self.datas[indice]:
            if id == key_datas:
                return value_datas
        return None

class CommandQueue:
    def __init__(self):
        self.command_queue = queue(None)
        self.command_history = history()

    def add_command(self, command):
        self.command_queue.append(command)
        self.command_history.add(command)

    def execute_command(self):
        command = self.command_queue.pop()
        # exécuter la commande ici
        return command

    def clear(self):
        self.command_queue = queue(None)
        self.command_history.clear()

class queueNode:
  def __init__(self,data):
    self.data = data
    self.next_node = None

class queue:
  def __init__(self, data):
    self.first_node = queueNode(data)

  def pop(self):
    if self.first_node == None:
      return

    data = self.first_node.data
    self.first_node = self.first_node.next_node
    return data

  def push(self,data):
    if self.first_node == None:
      self.first_node = queueNode(data)
      return
    
    current_node = self.first_node
    while current_node.next_node != None:
      current_node = current_node.next_node
    current_node.next_node = queueNode(data)

class fragenNode:
    def __init__(self, question, answers):
        self.question = question
        self.node = { question : {} }
        for answer in answers:
            self.node[question][answer] = fragenNode(None, [])
        self.empty = self.node == { None : {} }

    def size(self):
        count = 1
        node = self.node[self.question]
        for key in node:
            count += node[key].size()  
        return count
    
    def depth(self):
        Max = 0
        node = self.node[self.question]
        for key in node:
            if node[key].depth() > Max:
                Max = node[key].depth()
        return Max + 1

    def append(self, question, answers, reponse_mere):
        new_node = fragenNode(question, answers)
        self.node[self.question][reponse_mere] = new_node

    def get_node(self, reponse):
        return self.node[self.question][reponse]

class fragenBaum:
    def __init__(self, question, reponses):
        self.first_node = fragenNode(question, reponses)
        self.current_node = self.first_node

    def size(self):
        return self.first_node.size()

    def depth(self):
        return self.first_node.depth()

    def append(self, question, reponses, reponse_mere):
        self.first_node.append(question, reponses, reponse_mere)

    def get_question(self):
        return self.current_node.question
    
    def get_answers(self):
        return list(self.current_node.node[self.get_question()].keys())
    
    def get_node(self, reponse):
        return self.current_node.node[self.get_question()][reponse]
    
    def choice(self, reponse):
        self.current_node = self.current_node.node[self.get_question()][reponse]