from structs import *
import discord
from discord.ext import commands

import os
import threading
import time
import random

def check_file(filename):
    if os.path.isfile(filename):
        if os.path.getsize(filename) > 0:
            return True
        else:
            return False
    else:
        return False

intents = discord.Intents.all()
client = commands.Bot(command_prefix="rambot ", intents = intents)
user_hashmap = UserHashMap(100)

botQueue = queue(None)
botQueue.pop()
def traverse_queue(queue):
    current_node = queue.first_node
    i = 0;
    while current_node != None:
        i+=1
        print(i, current_node.data)
        current_node = current_node.next_node

@client.after_invoke
async def after_any_command(ctx):
    traverse_queue(botQueue)
    node = botQueue.pop()
    if node is not None:
        process, data = node
        return await ctx.send(process(data))

@client.command(name="history.all")
async def history_all(ctx):
    def procedure(ctx):
        user_id = ctx.author.id
        user_hashmap.add_user(user_id)
        user_history = user_hashmap.get_user(user_id)
        if(check_file(f"history_{user_id}.json")) : user_history.command_history = user_history.command_history.load_from_file(f"history_{user_id}.json")

        if user_history.command_history is None:
            send = "Aucun historique trouvé."
        else:
            send = user_history.command_history.get_all()
            
        user_history.command_history.add("rambot history.all");
        user_history.command_history.save_to_file(f"history_{user_id}.json")
        return send
    return botQueue.push([procedure, ctx])

@client.command(name="history.last")
async def history_current(ctx):
    def procedure(ctx):
        user_id = ctx.author.id
        user_hashmap.add_user(user_id)
        user_history = user_hashmap.get_user(user_id)
        if(check_file(f"history_{user_id}.json")) : user_history.command_history = user_history.command_history.load_from_file(f"history_{user_id}.json")

        if user_history.command_history is None:
            send = "Aucun historique trouvé."
        else:
            send = user_history.command_history.get_last()

        user_history.command_history.add("rambot history.last");
        user_history.command_history.save_to_file(f"history_{user_id}.json")
        return send
    return botQueue.push([procedure, ctx])


@client.command(name="history.prev")
async def history_prev(ctx):
    def procedure(ctx):
        user_id = ctx.author.id
        user_hashmap.add_user(user_id)
        user_history = user_hashmap.get_user(user_id)
        if(check_file(f"history_{user_id}.json")) : user_history.command_history = user_history.command_history.load_from_file(f"history_{user_id}.json")

        if user_history.command_history is None:
            send = ("Aucun historique trouvé.")
        else:
            send = (user_history.command_history.move_backward())

        user_history.command_history.add("rambot history.prev");
        user_history.command_history.save_to_file(f"history_{user_id}.json")
        return send
    return botQueue.push([procedure, ctx])

@client.command(name="history.next")
async def history_next(ctx):
    def procedure(ctx):
        user_id = ctx.author.id
        user_hashmap.add_user(user_id)
        user_history = user_hashmap.get_user(user_id)
        if(check_file(f"history_{user_id}.json")) : user_history.command_history = user_history.command_history.load_from_file(f"history_{user_id}.json")

        if user_history.command_history is None:
            send = ("Aucun historique trouvé.")
        else:
            send = (user_history.command_history.move_forward())

        user_history.command_history.add("rambot history.next");
        user_history.command_history.save_to_file(f"history_{user_id}.json")
        return send
    return botQueue.push([procedure, ctx])

@client.command(name="history.clear")
async def history_clear(ctx):
    def procedure(ctx):
        user_id = ctx.author.id
        user_hashmap.add_user(user_id)
        user_history = user_hashmap.get_user(user_id)
        if(check_file(f"history_{user_id}.json")) : user_history.command_history = user_history.command_history.load_from_file(f"history_{user_id}.json")

        if user_history.command_history is None:
            send = "Aucun historique trouvé."
        else:
            user_history.command_history.clear()
            send = "Historique vidé"

        user_history.command_history.save_to_file(f"history_{user_id}.json")
        return send
    botQueue.push([procedure, ctx])









playlist = [
    "Eight Reasons Why I Love You - The Precisions",
    "The Look of Love - ABC",
    "Come Home Soon - The Intruders",
    "Soulicious - Sarah Connor",
    "679 - Fetty Wap",
    "Houdini - Kaaris",
    "Last Time (ft. Snoh Alegra) - Giveon",
    "Good Morning Gorgeous - Mary J. Blige",
    "Ligne 11 - Werrason",
    "Lovestory - Meryl",
    "Come - Jain",
    "Où les anges brulent - Lino",
    "Temps Mort 2.0 (ft. Lino) - Booba",
]


q1 = fragenBaum("t'es là ?", ["oui", "non", "je ne sais pas"])
q1.append("tu vas bien ?", ["oui", "non"], "oui")
q1.append("oulà, t'es un esprit ?", ["oui", "non"], "non")
q1.append("j'ai l'impression que c'est plus ironique que métaphysique, chef... ça va ?", ["oui", "non"], "je ne sais pas")

q1.get_node("oui").append("Que cela continue ainsi !", [], "oui")
q1.get_node("oui").append("Force à toi, chef, ça ira, chef... T'écoutes de la musique, pas vrai ?", ['oui', 'non'], "non")
q1.get_node("non").append("Et t'es encore coincé sur Terre avec nous ? HAHAHAHA, force à toi", [], "oui")
q1.get_node("non").append("Hmm, dans ce cas, je pense que t'es là, mon reuf", [], "non")
q1.get_node("je ne sais pas").append("Continue à être heureux", [], "oui")
q1.get_node("je ne sais pas").append("Ryan RAÏS a eu bonne playlist pour toi, ça devrait te remettre sur pied", [], "non")

q1.get_node("oui").get_node('non').append("Bon, écoute Soulicious de Sarah Connor, tu vas pas t'en remettre (en fait si, tu vas t'en remettre, c'est justement le but de la manoeuvre)", [], "oui")
q1.get_node("oui").get_node('non').append("Tu es quelqu'un de simple, j'aime bien... Essaie de mater un sketch de Thomas Ngijol, ça te rendra le sourire !", [], "non")

# Fonction qui retourne une liste de réponses possibles pour une question donnée
def get_answers(question):
    return list(q1.current_node.node[question].keys())

# Événement qui se déclenche lorsque le bot se connecte à Discord
@client.event
async def on_ready():
    print('Connecté en tant que {0.user}'.format(client))

def start_tree_interaction():
    return "Bonjour! Je suis un bot qui va vous poser quelques questions pour déterminer votre état d'esprit actuel. Êtes-vous prêt à commencer? (répondez avec 'oui' ou 'non')"

# Événement qui se déclenche lorsque le bot reçoit un message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('rambot hey'):
        response = start_tree_interaction()
        await message.channel.send(response)

    # Vérifier si le message contient la question actuelle
    if message.content == q1.get_question():
        # Obtenir les réponses possibles et envoyer un message pour les afficher
        answers = get_answers(q1.get_question())
        await message.channel.send('Réponses possibles : ' + ', '.join(answers))
    else:
        # Vérifier si le message est une réponse valide à la question actuelle
        answers = get_answers(q1.get_question())
        if message.content in answers:
            # Aller au nœud suivant
            q1.choice(message.content)
            random_song = random.choice(playlist)
            random_song = f" - [random playlist recommandation > {random_song}]"

            # Vérifier si le nœud actuel est une feuille
            if q1.get_answers() == []:
                # Envoyer un message avec la réponse finale et réinitialiser l'arbre
                await message.channel.send(random_song + '\nMa réponse est : ' + q1.get_question())
                q1.current_node = q1.first_node
            else:
                # Envoyer la prochaine question
                await message.channel.send(random_song + '\n' + q1.get_question() + " (" + ', '.join(q1.get_answers()) + ")")









# client.run()
