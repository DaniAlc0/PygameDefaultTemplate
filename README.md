# Pygame Default Template

This repository contains a default template for projects developed with Pygame. The goal of this template is to provide a solid and modular base for game development, allowing you to focus on the specific mechanics of the game without needing to redo essential logic, such as screen resizing, game state management, and data persistence.

## Key Features

### 1. Modularity
The template is designed to be highly modular, allowing easy replacement or modification of individual components, such as the menu system, sprite management, and settings control.

### 2. Data Persistence
Game settings, such as screen resolution, audio volume, language, and player data (playtime, high score, etc.), are stored in a JSON file. These settings are automatically loaded when the game starts, ensuring that player preferences are maintained between sessions.

### 3. Game State Management
The template includes a structure for managing different game states, such as menus, levels, and pauses. This makes it easier to create and navigate between different screens and modes within the game.

### 4. Screen Resizing
The logic for screen resizing is integrated, allowing the game to automatically adjust the resolution and aspect ratio according to the player's preferences.

### 5. Multilingual Support
The template includes support for multiple languages, which can be easily expanded by adding new translations in the JSON settings file.

## Project Structure

```bash
Pygame-Default-Template/
│
├── config/
│ └── settings.json # Game settings file (resolution, audio, language, etc.)
│
├── images/ # Directory to store sprites and other graphics
│
├── scripts/
│ ├── game.py # Main game logic
│ ├── menu.py # Main menu implementation
│ ├── screen.py # Screen management and resizing
│ ├── settings.py # Loading and saving settings
│ └── sprites.py # Sprite loading
│ └── text.py # Text management
│ └── button.py # Button management
│
└── main.py # Main script to start the game
```

## Settings
Game settings are managed through the settings.json file located in the config/ directory. This file allows customization of various options, including screen resolution, language, volume, and key mappings.
