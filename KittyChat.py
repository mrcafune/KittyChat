from colorama import Fore, init
import openai
import json
import time
import sys
import re
import os

def print_multiline(text):
    for line in text.split('\n'):
        print(line)

def clear_screen():
    if os.name == 'posix':  # for UNIX/Linux/MacOS
        _ = os.system('clear')
    else:  # for Windows
        _ = os.system('cls')

def choose_model():
    print(Fore.GREEN + "Please select your Model | Available Models:")
    print(Fore.WHITE + " ")
    print("(1) gpt-3.5-turbo: Most capable GPT-3.5 model optimized for chat at a reduced cost.\n")
    print("(2) gpt-3.5-turbo-16k: Same capabilities as gpt-3.5-turbo but with four times the context.\n")
    print("(3) GPT-4: More capable than any GPT-3.5 model, able to do more complex tasks, and optimized for chat.\n")
    
    user_choice = input(Fore.YELLOW + "Enter the corresponding number for the model (without parentheses): ")

    if user_choice == "1":
        print("Model: gpt-3.5-turbo")
        return 'gpt-3.5-turbo'
    elif user_choice == "2":
        print("Model: gpt-3.5-turbo-16k")
        return 'gpt-3.5-turbo-16k'
    elif user_choice == "3":
        print("Model: gpt-4")
        return 'gpt-4'
    else:
        print("Invalid choice. Defaulting to 'gpt-3.5-turbo'.")
        return 'gpt-3.5-turbo'

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

def load_and_print_session(filename, session_name):
    if not os.path.isfile(filename):
        print("No saved session found.")
        return None
    else:
        with open(filename, 'r') as f:
            sessions = json.load(f)
        if session_name in sessions:
            session = sessions[session_name]
            print(f"\nSession name: {session_name}")
            for message in session:
                if message['role'] == 'system':
                    print(f"System: {message['content']}")
                elif message['role'] == 'user':
                    print(f"\033[94mYou: {message['content']}\033[0m")
                else:  # message['role'] == 'assistant'
                    print(f"\033[92mKitten Technologies Virtual Assistant: {message['content']}\033[0m")
        else:
            print("No session found with this name.")

def load_config(filename):
    if not os.path.isfile(filename):
        config = {"first_time": True, "api_key": "", "model": ""}
        with open(filename, 'w') as f:
            json.dump(config, f)
        print("No previous configuration file found - configuration file generated.")
        return config
    with open(filename, 'r') as f:
        try:
            config = json.load(f)
            # Just making sure that the model key is present
            if 'model' not in config:
                config['model'] = ""
            return config
        except json.JSONDecodeError:
            print("Failed to decode the configuration file.")
            return None

def save_config(filename, config):
    with open(filename, 'w') as f:
        json.dump(config, f)

def main():
    config_filename = 'config.json'
    config = load_config(config_filename)
    if config is None:
        print("Unable to access or parse the config file.")
        print("Please check your permissions to the file.  Exiting program")
        exit()
    elif "first_time" in config and not config["first_time"]:
        api_key = config["api_key"]
        model = config["model"]
        print("Config file loaded.")
    else:
        print(Fore.GREEN, " ")
        print('''
██╗  ██╗██╗████████╗████████╗██╗   ██╗ ██████╗██╗  ██╗ █████╗ ████████╗
██║ ██╔╝██║╚══██╔══╝╚══██╔══╝╚██╗ ██╔╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝
█████╔╝ ██║   ██║      ██║    ╚████╔╝ ██║     ███████║███████║   ██║   
██╔═██╗ ██║   ██║      ██║     ╚██╔╝  ██║     ██╔══██║██╔══██║   ██║   
██║  ██╗██║   ██║      ██║      ██║   ╚██████╗██║  ██║██║  ██║   ██║   
╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝      ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                     ''')
        print(Fore.WHITE, "🐈 KittyChat - Terminal AI Assistant | Written by Brandon K.")
        print(Fore.YELLOW + "*** Please note that KittyChat does not store any of your personal information ***")
        print(Fore.WHITE + "Visit https://kittentechnologies.com or https://github.com/mrcafune/kittychat for more information.")
        print("-------------------------------------------------------------------\n")
        print(Fore.GREEN + "Welcome to the first time setup!  In order to use this program you will:\n")
        print(Fore.WHITE + "- Enter your API Key (You can find your Secret API key in your User settings.)\n- Choose your Chat model\n")
        api_key = input(Fore.YELLOW + "Please enter your OpenAI API without quotes: ")
        print(Fore.WHITE + "\n-------------------------------------------------------------------\n")
        model = choose_model()
        print("\nTesting API Key - this will take a few seconds")
        try:
            test_message = chat_with_gpt(api_key, [{"role": "system", "content": "Please reply with just the word, success"}], model)
            print(test_message)
        except Exception as e:
            print("An error occurred: ", e)
            print(Fore.RED, "API key seems to be incorrect. Please re-enter the API key or type " + Fore.YELLOW, "-exit" + Fore.WHITE, "to exit.")
            user_input = input()
            if user_input == '-exit':
                return
        config["first_time"] = False
        config["api_key"] = api_key
        config["model"] = model
        save_config(config_filename, config)
        print(Fore.GREEN, "\nSuccess!")
        print("Exiting Setup & KittyChat - you can revisit this setup by typing" + Fore.YELLOW + " -reset")
        time.sleep(10)
        print(Fore.WHITE, "")
        clear_screen()

    current_model = model
    print(Fore.GREEN, " ")
    print('''
██╗  ██╗██╗████████╗████████╗██╗   ██╗ ██████╗██╗  ██╗ █████╗ ████████╗
██║ ██╔╝██║╚══██╔══╝╚══██╔══╝╚██╗ ██╔╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝
█████╔╝ ██║   ██║      ██║    ╚████╔╝ ██║     ███████║███████║   ██║   
██╔═██╗ ██║   ██║      ██║     ╚██╔╝  ██║     ██╔══██║██╔══██║   ██║   
██║  ██╗██║   ██║      ██║      ██║   ╚██████╗██║  ██║██║  ██║   ██║   
╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝      ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                     ''')
    print(Fore.WHITE, "Version 1.0 | Written by Brandon K.\n" + Fore.GREEN, "Powered by Love ❤️ & Python 🐍")
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
        elif user_message.lower() == '-clearscreen':
            clear_screen()
            continue
        elif user_message.lower() == '-neverask':
            config['alwaysask'] = False
            config['neverask'] = True
            print("Configuration Changed: -neverask" + Fore.GREEN," [ON]" + Fore.WHITE, "")
            print("Configuration Changed: -alwaysask" + Fore.RED," [OFF]")
            save_json(config_filename, config)
            continue
        elif user_message.lower() == '-reset':
            config["first_time"] = True
            save_config(config_filename, config)
            print("Reset complete. You'll be asked for API key the next time you open this program\n KittyChat will now close.")
            exit()
        elif user_message.lower() == '-help':
            print(Fore.YELLOW + "Available Commands")
            print(Fore.YELLOW + "\n-exit:" + Fore.WHITE +"             Exit the conversation. You'll be prompted to save the conversation")
            print(Fore.YELLOW + "-alwaysask:" + Fore.WHITE + "        Always ask at startup whether to start a new conversation or load a previous one")
            print(Fore.YELLOW + "-neverask" + Fore.WHITE + "          Never ask at startup, always start a new conversation")
            print(Fore.YELLOW + "-clearscreen" + Fore.WHITE + "       Clears the terminal of text")
            print(Fore.YELLOW + "-help:" + Fore.WHITE + "             Display this help message")
            print(Fore.YELLOW + "-model:" + Fore.WHITE + "            Changes the language learning model")
            print(Fore.YELLOW + "-sessionsummary:" + Fore.WHITE + "   Prints the previous sessions conversation")
            print(Fore.YELLOW + "-reset:" + Fore.WHITE + "            Clears your API Key, runs first time setup")
            continue
        elif user_message.lower() == '-model':
            choose_model()
            continue
        elif user_message.lower() == '-sessionsummary':
            if session_name is not None:
                load_and_print_session(session_filename, session_name)
            else:
                print("No session has been started yet.")
            continue
        elif user_message.lower()[0] == '-':
            print("Unrecognized command. Available commands are -exit, -alwaysask, -neverask, -help.")
            continue
            
        conversation.append({"role": "system", "content": "You just said: "+ user_message})
        conversation.append({"role": "user", "content": user_message})
        
        bot_message = chat_with_gpt(api_key, conversation, current_model)
        print('\033[92m' + Fore.GREEN + 'Kitten Technologies Virtual Assistant: ' + '\033[0m')
        print(Fore.WHITE, end=' ')
        slow_print_multiline(bot_message)
        conversation.append({"role": "assistant", "content": bot_message})

if __name__ == "__main__":
    main()
