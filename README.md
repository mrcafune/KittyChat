# 🐈 KittyChat - Terminal AI Assistant

https://kittentechnologies.com

KittyChat is an interactive Python application that integrates OpenAI's powerful GPT-3 model to create a highly engaging, AI-driven conversation interface. The application allows users to engage in dynamic conversations with a virtual assistant, right from the comfort of their terminal.

Built with Python and using OpenAI's API, KittyChat delivers thoughtful and contextually relevant responses, offering a unique and exciting conversational experience.

## 🔑 Key Features

- **Interactive Conversations:** Engage in real-time, dynamic conversations with the virtual assistant powered by GPT-3.

- **Color-coded Dialogue:** Messages are color-coded for a more visual and intuitive user experience.

- **Real-time Text Generation:** Experience real-time text generation, just as if you're chatting with a human.

- **Session Management:** Start a new conversation or continue from a saved session. The application can store your conversation history for later reference.

- **Command Options:** Use various commands (`-help`, `-alwaysask`, `-neverask`, `-exit`) for improved interactivity and control over the application.
  
## 🖥️ Usage

To use KittyChat, you will need to have an API key from OpenAI and will need to replace the "api_token" variable in the Main function.`(api_key = ("sk-YOUR-API-KEY-HERE")`

After starting the application, you can choose to start a new conversation or load a previous session. The application will guide you with the available commands and options by entering -help. During the conversation, type your message after the "Message:" prompt and the virtual assistant will respond accordingly.

<img width="862" alt="Screen Shot 2023-06-23 at 7 44 31 AM" src="https://github.com/mrcafune/KittyChat/assets/101951803/7e4bd39d-d2f6-4367-8f8f-1416c3d3b29c">



## 👩‍💻 Commands

- `-exit`: Exit the conversation. You'll be prompted to save the conversation.

- `-alwaysask`: Always ask at startup whether to start a new conversation or load a previous one.

- `-neverask`: Never ask at startup, always start a new conversation.

- `-help`: Display the help message. (lol)

- `-model`: Change the AI Model
  
- `-sessionsummary`: Prints the loaded sessions previous conversation

- `-reset`: Runs the first time setup, allowing you to change the API key & Model

- `-clearscreen`: Clears the screen of all previous text
  
## 🗺️ Roadmap 

- ✅ **[Complete]** Better Formatting of Responses<br />
Modify the response to be more readable and account for styles of information, like code and list

- ✅ **[Complete]** Improved Session System<br />
Provide tools to print the entire previous session, parts of it, set one or the other by default on load, etc.

- ✅ **[Complete]** Create 'First Time Setup'<br />
Allow users to enter API keys on initial setup rather than manually setting it, and choose what Model you want

- ✅ **[Complete]** Improved Help<br />
  Format the help command, add additional options for navigation

- ⏳ **Application Packagement**<br />
Deploy the finished application to Flatpak, Snap, Deb, and RPM
  
## 🗒️ Change Log

**6/27/2023**
- The `-model` command now allows you to change the language learning model.

- Added `-sessionsummary` so you can now print a summary of the previous session's conversation. It's a useful tool that provides a quick overview of the key points discussed, making it easier for you to review and understand past interactions.

- Added `-reset` command - encountered issues with your API key, language model, or just want to start fresh? No worries! The reset command now enables you to run the first time setup.

- Added `-clearscreen` command that clears the screen, providing a clean slate if things get too clutttered.

**6/23/2023**

- Improved the text generation rate to emulate GPT more accurately, resulting in faster and more appropriately formatted output

- Introduced functionality to color-code comments in the generated code for improved readability.

- Enhanced the Welcome Screen with additional, useful information for better user orientation.

- Revamped the formatting of the `-help` command to increase visual appeal and integrated the `-model` functionality.

- Optimized the feedback mechanism for Configuration Changes to detail the specific alterations made.

- Partially implemented support for additional models. There are still issues with consistent model switching that need to be resolved.

- The `-model` command is currently non-operational but is displayed in the `-help` command output. Work is in progress to make this fully functional.

## 🫰 API Access

This application is designed to use OpenAI's GPT-3 model. Please ensure you are aware of the costs associated with using OpenAI's API before using this application.
