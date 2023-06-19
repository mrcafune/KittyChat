from colorama import Fore, init
import openai
import json
import time

def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def chat_with_gpt(api_key, conversation):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )
    return response['choices'][0]['message']['content']

def print_slowly(text, delay=0.05):
    for word in text.split():
        print(word, end=' ', flush=True)
        time.sleep(delay)
    print()

def main():
    api_key = ("sk-YOUR-API-KEY-HERE")
    print('''\
  _  ___ _   _               _______        _                 _             _           
 | |/ (_) | | |             |__   __|      | |               | |           (_)          
 | ' / _| |_| |_ ___ _ __      | | ___  ___| |__  _ __   ___ | | ___   __ _ _  ___  ___ 
 |  < | | __| __/ _ \ '_ \     | |/ _ \/ __| '_ \| '_ \ / _ \| |/ _ \ / _` | |/ _ \/ __|
 | . \| | |_| ||  __/ | | |    | |  __/ (__| | | | | | | (_) | | (_) | (_| | |  __/\__|
 |_|\_\_|\__|\__\___|_| |_|    |_|\___|\___|_| |_|_| |_|\___/|_|\___/ \__, |_|\___||___/
                                                                       __/ |            
                                                                      |___/ ''')
    print("CLI Virtual AI Assistant - Powered by ChatGPT\nType -help for additional commands")
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
        print(Fore.LIGHTCYAN_EX, end="")
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
            save_json(config_filename, config)
            continue
        elif user_message.lower() == '-neverask':
            config['alwaysask'] = False
            config['neverask'] = True
            save_json(config_filename, config)
            continue
        elif user_message.lower() == '-help':
            print(Fore.YELLOW + "Available Commands")
            print(Fore.YELLOW + "\n-exit:" + Fore.WHITE +"  Exit the conversation. You'll be prompted to save the conversation.")
            print(Fore.YELLOW + "-alwaysask:" + Fore.WHITE + "  Always ask at startup whether to start a new conversation or load a previous one.")
            print(Fore.YELLOW + "-neverask" + Fore.WHITE + "  Never ask at startup, always start a new conversation.")
            print(Fore.YELLOW + "-help:" + Fore.WHITE + "  Display this help message.")
            continue
        elif user_message.lower()[0] == '-':
            print("Unrecognized command. Available commands are -exit, -alwaysask, -neverask, -help.")
            continue
            
        conversation.append({"role": "system", "content": "You just said: "+ user_message})
        conversation.append({"role": "user", "content": user_message})
        
        bot_message = chat_with_gpt(api_key, conversation)
        print(Fore.GREEN + "\nKitten Technologies Virtual Assistant: ", end='')
        print(Fore.WHITE, end=' ')
        print_slowly(bot_message)
        conversation.append({"role": "assistant", "content": bot_message})

if __name__ == "__main__":
    main()
