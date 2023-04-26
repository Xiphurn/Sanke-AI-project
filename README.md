# Sanke-AI-project

Snake Game with AI
This repository contains a Python implementation of the classic Snake game with an AI that learns to play. The project consists of three modules:

1. main.py: Allows the user to choose between playing the game solo or launching the AI.

2. game_solo.py: Implements the classic Snake game that can be played solo.

3. game_class.py: The AI model that learns to play Snake.

# Requirements
- Python 3.x
- Pygame
- Numpy (required for the AI model, will be added when the model is ready)
- PyTorch (required for the AI model, will be added when the model is ready)

# How to Play
To play the game solo, simply run main.py and select option 1. Use the arrow keys to move the snake and try to eat as many apples as possible without colliding with the walls or your own body.

To launch the AI, select option 2 in main.py. This will start the AI model that will learn to play Snake over time. The AI will attempt to maximize its score by making moves based on what it has learned from its previous games.

# Future Improvements
Currently, the AI module is under development and not yet available. In the future, the AI will be trained using machine learning techniques such as reinforcement learning to improve its performance. Additionally, the code will be refactored and cleaned up to improve readability and maintainability.
