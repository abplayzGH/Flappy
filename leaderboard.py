import json
import os

LEADERBOARD_FILE = 'leaderboard.json'

# Function to load leaderboard data from the JSON file
def load_leaderboard():
    """Load the leaderboard from the JSON file."""
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading leaderboard file: {e}")
            return []  # Return an empty leaderboard in case of error
    else:
        return []

# Function to save leaderboard data to the JSON file
def save_leaderboard(leaderboard):
    """Save the leaderboard to the JSON file."""
    try:
        with open(LEADERBOARD_FILE, 'w') as file:
            json.dump(leaderboard, file, indent=4)
    except IOError as e:
        print(f"Error saving leaderboard file: {e}")

# Function to add a new player and score to the leaderboard
def add_score(name, score):
    """Add a score for a player and update the leaderboard."""
    if not isinstance(score, int) or score < 0:
        print("Error: The score must be a non-negative integer.")
        return  # Do not add the score if it's invalid

    leaderboard = load_leaderboard()
    leaderboard.append({"name": name, "score": score})
    leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)  # Sort by score in descending order
    save_leaderboard(leaderboard)



# Function to get the current leaderboard (sorted by score)
def get_leaderboard():
    """Get the sorted leaderboard."""
    leaderboard = load_leaderboard()
    return sorted(leaderboard, key=lambda x: x['score'], reverse=True)

# Function to display the leaderboard
def display_leaderboard():
    """Display the leaderboard in a formatted way."""
    leaderboard = get_leaderboard()
    print("Leaderboard:")
    print("{:<20} {:<10}".format("Player", "Score"))
    print("-" * 30)
    for entry in leaderboard:
        print("{:<20} {:<10}".format(entry["name"], entry["score"]))
