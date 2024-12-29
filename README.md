# 🌇 KittyChat (Archived)

KittyChat is now **Quari**! Moving forward, all updates, features, and improvements will be made exclusively to the [Quari repository](https://github.com/mrcafune/Quari). This repository will remain archived and will no longer receive updates or maintenance


# 🐈 KittyChat - Terminal AI Assistant

<img width="523" alt="Screen Shot 2023-06-27 at 10 24 54 AM" src="https://github.com/mrcafune/KittyChat/assets/101951803/56bbcbea-4312-4c55-982e-6485e35cf18a">

https://kittentechnologies.com

KittyChat is an interactive Python application that integrates OpenAI's powerful GPT-3 model to create a highly engaging, AI-driven conversation interface. The application allows users to engage in dynamic conversations with a virtual assistant, right from the comfort of their terminal.

Built with Python and using OpenAI's API, KittyChat delivers thoughtful and contextually relevant responses, offering a unique and exciting conversational experience.

## 🔑 Key Features

- **Interactive Conversations:** Engage in real-time, dynamic conversations with the virtual assistant powered by GPT-3.

- **Color-coded Dialogue:** Messages are color-coded for a more visual and intuitive user experience.

- **Real-time Text Generation:** Experience real-time text generation, just as if you're chatting with a human.

- **Session Management:** Start a new conversation or continue from a saved session. The application can store your conversation history for later reference.

- **Command Options:** Use various commands for improved interactivity and control over the application.
  
## 🖥️ Usage

To use KittyChat, you will need to have an API key from OpenAI.  On first time setup, you will be prompted for your API Key and desired model.

<img width="735" alt="Screen Shot 2023-06-27 at 10 17 03 AM" src="https://github.com/mrcafune/KittyChat/assets/101951803/d7839b0b-285b-4404-b275-d87f6ef5702c">

After starting the application, you can choose to start a new conversation or load a previous session. The application will guide you with the available commands and options by entering -help. During the conversation, type your message after the "Message:" prompt and the virtual assistant will respond accordingly.

<img width="737" alt="Screen Shot 2023-06-27 at 10 21 16 AM" src="https://github.com/mrcafune/KittyChat/assets/101951803/dc7d9ab8-c140-4f61-8875-154aea59a37e">

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

- I've created an interactive setup process to make it easier for users to get started with our app. During the first time setup, you will be prompted to provide your Chat Model and API key.

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

This application is designed to use OpenAI's GPT-3 model. Please ensure you are aware of the costs associated with using OpenAI's API before using this application.  Note that KittyChat does not send any of your information to any remote servers, etc. ChatGPT will log your conversations, including any personal data you share, and will use it as training data.
