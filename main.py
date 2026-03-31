import json
import os

DATA_FILE = "game_notes.json"
GAMES = []

def find_game(game_name):
    return next((g for g in GAMES if g['name'] == game_name), None)

def get_input(prompt):
    return input(prompt).strip()

def load_data():
    global GAMES
    if not os.path.exists(DATA_FILE):
        print("No data file found. Starting fresh.")
        GAMES = []
        return
    try:
        with open(DATA_FILE, "r") as file:
            GAMES = json.load(file)
    except Exception as e:
        print(f"Error loading data: {e}")
        GAMES = []

def save_data():
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(GAMES, file, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def add_game_notes():
    name = get_input("Enter game name: ").lower()
    if find_game(name):
        print("Game already exists. Updating instead.")
        return update_game_notes()
    controls = get_input("Enter controls: ")
    objectives = get_input("Enter objectives: ")
    progress = get_input("Enter progress: ")
    GAMES.append({
        "name": name,
        "controls": controls,
        "objectives": objectives,
        "progress": progress
    })
    print("Game notes added.")
    save_data()

def update_game_notes():
    name = get_input("Enter game name to update: ").lower()
    game = find_game(name)
    if not game:
        print("Game not found.")
        return
    game['controls'] = get_input("Enter updated controls: ")
    game['objectives'] = get_input("Enter updated objectives: ")
    game['progress'] = get_input("Enter updated progress: ")
    print("Game notes updated.")
    save_data()

def view_notes():
    name = get_input("Enter game name to view: ").lower()
    game = find_game(name)
    if not game:
        print("No notes found for this game.")
        return
    print("\n--- Game Notes ---")
    print(f"Game: {game['name']}")
    print(f"Controls: {game['controls']}")
    print(f"Objectives: {game['objectives']}")
    print(f"Progress: {game['progress']}")

def list_all_games():
    if not GAMES:
        print("No games stored.")
        return
    print("\n--- Saved Games ---")
    for g in GAMES:
        print(f"- {g['name']}")

def main():
    load_data()
    menu = {
        "1": add_game_notes,
        "2": update_game_notes,
        "3": view_notes,
        "4": list_all_games
    }
    while True:
        print("\n===== Game Notes Tracker =====")
        print("1. Add Game Notes")
        print("2. Update Game Notes")
        print("3. View Notes")
        print("4. List All Games")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "5":
            print("Exiting program.")
            break
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
