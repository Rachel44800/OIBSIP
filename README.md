# OIBSIP
Chat Application

 # Simple Chat App

This is a basic client-server chat application implemented in Python using sockets. The application allows multiple clients to connect to a server, send messages, and receive replies.

# Files

  Server.py: Contains the server-side implementation.
  Client.py: Contains the client-side implementation.

# How to Run

1. Open two terminal windows.
2. In one terminal, run the server script:   
    python Server.py

3. In the other terminal, run the client script: 
    python Client.py
    
4. Enter a username when prompted.
5. Start typing messages to communicate with the server.

# Commands

  To end the conversation, type 'bye' in the client terminal.
  The server will prompt you for a reply after receiving a message.

# Features

  Threading: The server handles multiple clients simultaneously using threads.
  Usernames: Clients provide a username for identification.
  Timestamp: Messages display timestamps for better tracking.
  Graceful Shutdown: The server allows connected clients to finish conversations before exiting.
