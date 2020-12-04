# Trivia

[![Build Status](https://travis-ci.com/daguirrez/trivia.svg?branch=master)](https://travis-ci.com/daguirrez/trivia)

Proyecto de la materia de **Calidad y pruebas de software**.

### Arbol de dependencias
- init_game
	- get_initial_data
		- **MyStorage**.load_players
		- **MyStorage**.load_categories
	- title_screen
		- **builtins**.input
		- **builtins**.print
		- **MyStorage**.save_player
		- **MyStorage**.load_players
	- menu_screen
		- **builtins**.input
		- **builtins**.print
	- player_stats_screen
		- **builtins**.input
		- **builtins**.print
	- categories_screen
		- **builtins**.input
		- **builtins**.print
	- game_screen
		- **builtins**.input
		- **builtins**.print
	- final_screen
		- **builtins**.input
		- **builtins**.print
		- **MyStorage**.save_match