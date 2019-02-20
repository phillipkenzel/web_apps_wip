# Liberaries
import webbrowser

# Variablen
bot_template = 'ALFONS : {0}'
user_template = 'USER : {0}'
altes_essen = ['Pizza', 'Nudeln mit Pesto', 'Sauerbraten']
neues_essen = []

# Funktionen
def respond(message):
    bot_message = 'Aha. Du planst also ' + message + ' zu kochen.'
    neues_essen.append(message)
    bot_message = 'Das ist doch eine Idee. Falls du dir unsicher bist, habe ich auch alternative Vorschläge für dich: '
    return bot_message

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

# Interface
print(bot_template, 'Hallo, ich bin Alfons und helfe dir. Was willst du heute kochen?')
message = input()
send_message(message)
print(altes_essen)
print(bot_template, 'Sag mir bitte, ist da ein interessantes Gericht für dich dabei?')
decision = input()
if decision == 'Ja' or 'ja':
    print(bot_template, 'Was denn genau?')
    answer = input()
    if answer in altes_essen and answer == 'Pizza':
        webbrowser.open('https://www.chefkoch.de/rs/s0/Pizza/Rezepte.html')
    if answer in altes_essen and answer == 'Nudeln mit Pesto':
        webbrowser.open('https://www.chefkoch.de/rs/s0/Nudeln+mit+Pesto/Rezepte.html')
    if answer in altes_essen and answer == 'Sauerbraten':
        webbrowser.open('https://www.chefkoch.de/rs/s0/Sauerbraten/Rezepte.html')
else:
    print(bot_template, 'Na dann kann ich dir leider auch nicht helfen. Such doch mal ein Kochbuch auf!')
