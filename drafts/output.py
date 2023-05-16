""" def infinite_loop():
    while True:
        node = botQueue.pop()
        print(node if node is not None else "", end="" if node is None else None)
        if node is not None:
            process, data = node
            loop = asyncio.get_event_loop()
            loop.run_until_complete(data.send(process(data)))

thread = threading.Thread(target=infinite_loop)
thread.start() """



""" @client.event
async def on_message(ctx):
    node = botQueue.pop()
    print(node if node is not None else "", end="" if node is None else None)
    if node is not None:
        process, data = node
        await ctx.send(process(data)) """

""" @client.event
async def on_message(ctx):
    user_id = ctx.author.id
    if ctx.author == client.user:
        return
    if ctx.content.startswith("/history"):
        print(f"{user_id}")
        await ctx.send(user_id)
        return """

""" def infinite_loop():
    while True:
        node = botQueue.pop()
        # print(node if node is not None else "", end="" if node is None else None)
        if node is not None:
            process, data = node
            return client.loop.create_task(process(data))

# thread = threading.Thread(target=infinite_loop)

#@client.before_invoke
#async def after_any_command(ctx):
    # thread.stop() """

""" @client.event
async def on_ready():
    async def procedure():
        await channel.send(f"{client.user.name} has connected to Discord!")
    botQueue.push([procedure, channel]) """