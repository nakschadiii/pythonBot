from structs import *

q1 = fragenBaum("t'es là ?", ["oui", "non", "je ne sais pas"])

q1.append("tu vas bien ?", ["oui", "non"], "oui")
q1.append("oulà, t'es un esprit ?", ["oui", "non"], "non")
q1.append("j'ai l'impression que c'est plus ironique que metaphysique, chef... ça va ?", ["oui", "non"], "je ne sais pas")

q1.get_node("oui").append("ok", [])


interro = q1
print(interro.size())
print(interro.depth())
# print(interro.get_question())
# interro.choice("oui")
# print(interro.get_question())

while interro is not None:
    if not interro.current_node.empty:
        key = input(interro.get_question() + " : ")
        while key not in interro.get_answers(): key = input(interro.get_question() + " : ")
        interro.choice(key)
    else:
        break
