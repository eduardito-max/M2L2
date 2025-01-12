import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$Explicame que es la contaminación?'):
        await message.channel.send(" cuando en un entorno ingresan elementos o sustancias que normalmente no deberían estar en él y que afectan el equilibrio del ecosistema.")
    elif message.content.startswith('$Como podemos detenerla?'):
        await message.channel.send("podemos disminuir al máximo el uso del automóvil y la motocicleta; preferir caminar, usar bicicleta o el transporte público")   
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("Ingresa tu token:")