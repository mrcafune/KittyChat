from colorama import Fore, init
import openai
import json
import time
import sys
import re

def print_multiline(text):
    for line in text.split('\n'):
        print(line)

def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def chat_with_gpt(api_key, conversation, model_name):
    global current_model
    current_model = model_name
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=current_model,
        messages=conversation,
    )
    return response['choices'][0]['message']['content']

def color_comments(text, comment_color='\033[91m', default_color='\033[0m'):
    # Replace comments with colored versions
    def color_comment(match):
        return comment_color + match.group(0) + default_color
    text = re.sub(r'#.*', color_comment, text)
    return text

def slow_print_multiline(text, delay=0.01):
    text = color_comments(text)
    for line in text.split('\n'):
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write('\n')

def main():
    # define model options
    models = ["text-davinci-002","text-curie-003","gpt-3.5-turbo"]

# default model
    current_model = models[2]
    print(Fore.GREEN, " ")
    api_key = ("sk-YOUR-KEY-HERE")
    print('''
██╗  ██╗██╗████████╗████████╗██╗   ██╗ ██████╗██╗  ██╗ █████╗ ████████╗
██║ ██╔╝██║╚══██╔══╝╚══██╔══╝╚██╗ ██╔╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝
█████╔╝ ██║   ██║      ██║    ╚████╔╝ ██║     ███████║███████║   ██║   
██╔═██╗ ██║   ██║      ██║     ╚██╔╝  ██║     ██╔══██║██╔══██║   ██║   
██║  ██╗██║   ██║      ██║      ██║   ╚██████╗██║  ██║██║  ██║   ██║   
╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝      ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                     ''')
    print(Fore.WHITE, "Version 0.2 | Written by Brandon K.\n" + Fore.GREEN, "Powered by Love ❤️ & Python 🐍")
    print(Fore.WHITE, " ")
    print("-------------------------------------------------------------------")
    print("Please type" + Fore.YELLOW, "-help" + Fore.WHITE, "for switches and additional options")
    print("Visit" + Fore.RED, "https://kittechnologies.com" + Fore.WHITE, " for more Software!\n-------------------------------------------------------------------")
    session_filename = 'saved_sessions.json'
    config_filename = 'config.json'
    
    
    saved_sessions = load_json(session_filename)
    config = load_json(config_filename)
    
    alwaysask = config.get('alwaysask', False)
    neverask = config.get('neverask', False)
    conversation = []

    while alwaysask or (not neverask and saved_sessions):
        action = input("Do you want to start a new session (N) or continue a previous session (P)? ")
        if action.lower() == 'p':
            print("Previous sessions:")
            for name in saved_sessions:
                print(name)
            session_name = input("Enter the name of the session you want to continue: ")
            conversation = saved_sessions.get(session_name, [])
            break
        elif action.lower() == 'n':
            break
    
    while True:
        print(Fore.BLUE + "\nMessage:", end=' ')
        print(Fore.LIGHTCYAN_EX, end=" ")
        user_message = input()
        print(Fore.WHITE)

        if user_message.lower() == '-exit':
            if input("Do you want to save this conversation (Y/N)? ").lower() == 'y':
                session_name = input("Enter a name for this session: ")
                saved_sessions[session_name] = conversation
                save_json(session_filename, saved_sessions)
            break
        elif user_message.lower() == '-alwaysask':
            config['alwaysask'] = True
            config['neverask'] = False
            print("Configuration Changed: -alwaysask" + Fore.GREEN," [ON]" + Fore.WHITE, "")
            print("Configuration Changed: -neverask" + Fore.RED," [OFF]")
            save_json(config_filename, config)
            continue
        elif user_message.lower() == '-neverask':
            config['alwaysask'] = False
            config['neverask'] = True
            print("Configuration Changed: -neverask" + Fore.GREEN," [ON]" + Fore.WHITE, "")
            print("Configuration Changed: -alwaysask" + Fore.RED," [OFF]")
            save_json(config_filename, config)
            continue
        elif user_message.lower() == '-help':
            print(Fore.YELLOW + "Available Commands")
            print(Fore.YELLOW + "\n-exit:" + Fore.WHITE +"          Exit the conversation. You'll be prompted to save the conversation.")
            print(Fore.YELLOW + "-alwaysask:" + Fore.WHITE + "     Always ask at startup whether to start a new conversation or load a previous one.")
            print(Fore.YELLOW + "-neverask" + Fore.WHITE + "       Never ask at startup, always start a new conversation.")
            print(Fore.YELLOW + "-help:" + Fore.WHITE + "          Display this help message.")
            print(Fore.YELLOW + "-model: " + Fore.RED + "        [BETA]" + Fore.WHITE, "Changes the language learning model of the app.")
            continue
        elif user_message.lower() == '-model':
            print("Current Model: " + current_model)
            print(" ")
            print("Available models:\n")
            print("1 - GPT 3.5 Turbo")
            print("2 - Davinci-002")
            print("3 - Currie-003")
            print(" ")
            model_number_st = input("[BETA][NOT ALWAYS FUNCTIONAL] Please enter your desired Model by entering just the corresponding number: ")
            model_number = int(model_number_st)
            model_number -= 1
            current_model = models[model_number -1]
            print("Model changed to: " + current_model)
            continue
        elif user_message.lower()[0] == '-':
            print("Unrecognized command. Available commands are -exit, -alwaysask, -neverask, -help.")
            continue
            
        conversation.append({"role": "system", "content": "You just said: "+ user_message})
        conversation.append({"role": "user", "content": user_message})
        
        bot_message = chat_with_gpt(api_key, conversation, current_model)
        print('\033[92m' + Fore.GREEN, 'Kitten Technologies Virtual Assistant: ' + '\033[0m')
        print(Fore.WHITE, end=' ')
        slow_print_multiline(bot_message)
        conversation.append({"role": "assistant", "content": bot_message})

if __name__ == "__main__":
    main()
