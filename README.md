# 🐈 KittyChat - Your Terminal AI Assistant

KittyChat is an interactive Python application that integrates OpenAI's powerful GPT-3 model to create a highly engaging, AI-driven conversation interface. The application allows users to engage in dynamic conversations with a virtual assistant, right from the comfort of their terminal.

Built with Python and using OpenAI's API, KittyChat delivers thoughtful and contextually relevant responses, offering a unique and exciting conversational experience.

## Key Features

- **Interactive Conversations:** Engage in real-time, dynamic conversations with the virtual assistant powered by GPT-3.

- **Color-coded Dialogue:** Messages are color-coded for a more visual and intuitive user experience.

- **Real-time Text Generation:** Experience real-time text generation, just as if you're chatting with a human.

- **Session Management:** Start a new conversation or continue from a saved session. The application can store your conversation history for later reference.

- **Command Options:** Use various commands (`-help`, `-alwaysask`, `-neverask`, `-exit`) for improved interactivity and control over the application.

## Usage

![screenshot](https://github.com/mrcafune/KittyChat/assets/101951803/fe8de2ec-ee43-4643-96fc-8f85b82b4b20)

To use KittyChat, you will need to have an API key from OpenAI and will need to replace the "api_token" variable in the Main function.`(api_key = ("sk-YOUR-API-KEY-HERE")`

After starting the application, you can choose to start a new conversation or load a previous session. The application will guide you with the available commands and options by entering -help. During the conversation, type your message after the "Message:" prompt and the virtual assistant will respond accordingly.

## Commands

- `-exit`: Exit the conversation. You'll be prompted to save the conversation.

- `-alwaysask`: Always ask at startup whether to start a new conversation or load a previous one.

- `-neverask`: Never ask at startup, always start a new conversation.

- `-help`: Display the help message. (lol)

**NOTE**: This application is designed to use OpenAI's GPT-3 model. Please ensure you are aware of the costs associated with using OpenAI's API before using this application.
