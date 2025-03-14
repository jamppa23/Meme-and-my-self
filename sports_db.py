import sqlite3

def create_sports_betting_db(db_name="sports_betting.db"):
    """
    Creates a SQLite database for sports betting and initializes tables.

    Args:
        db_name (str): The name of the database file.
    """

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create tables
    create_tables(cursor)

    conn.commit()
    conn.close()

def create_tables(cursor):
    """
    Creates the necessary tables for the sports betting database.

    Args:
        cursor (sqlite3.Cursor): The database cursor object.
    """

    # Table for Sports (e.g., Football, Basketball)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sports (
            sport_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sport_name TEXT NOT NULL UNIQUE
        )
    """)

    # Table for Leagues (e.g., Premier League, NBA)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Leagues (
            league_id INTEGER PRIMARY KEY AUTOINCREMENT,
            league_name TEXT NOT NULL UNIQUE,
            sport_id INTEGER,
            FOREIGN KEY (sport_id) REFERENCES Sports(sport_id)
        )
    """)

    # Table for Teams
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Teams (
            team_id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_name TEXT NOT NULL UNIQUE,
            league_id INTEGER,
            FOREIGN KEY (league_id) REFERENCES Leagues(league_id)
        )
    """)

    # Table for Events (Matches)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Events (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            home_team_id INTEGER,
            away_team_id INTEGER,
            event_date DATETIME,
            league_id INTEGER,
            FOREIGN KEY (home_team_id) REFERENCES Teams(team_id),
            FOREIGN KEY (away_team_id) REFERENCES Teams(team_id),
            FOREIGN KEY (league_id) REFERENCES Leagues(league_id)
        )
    """)

    # Table for Bets
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Bets (
            bet_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,  -- Assuming you have a users table
            event_id INTEGER,
            bet_amount REAL,
            bet_type TEXT,  -- e.g., "Home Win", "Away Win", "Draw"
            odds REAL,
            bet_status TEXT,  -- e.g., "Pending", "Won", "Lost"
            FOREIGN KEY (event_id) REFERENCES Events(event_id),
            FOREIGN KEY (user_id) REFERENCES Users(user_id) -- If you have a users table
        )
    """)

    # Table for Users (Optional, if you want to track users)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            balance REAL DEFAULT 0.0
        )
    """)

if __name__ == "__main__":
    create_sports_betting_db()
    print("Sports betting database created successfully!")

Explanation:
 * create_sports_betting_db(db_name="sports_betting.db"):
   * This function creates a connection to the SQLite database (or creates it if it doesn't exist).
   * It calls create_tables() to define the database schema.
   * It commits the changes and closes the connection.
 * create_tables(cursor):
   * This function defines the structure of the database using SQL CREATE TABLE statements.
   * Sports Table: Stores different sports (e.g., Football, Basketball).
   * Leagues Table: Stores leagues associated with sports (e.g., Premier League for Football).
   * Teams Table: Stores teams participating in leagues.
   * Events Table: Stores information about matches or events (home team, away team, date, league).
   * Bets Table: Stores information about user bets (user, event, amount, type, odds, status).
   * Users Table (Optional): Stores user information (username, balance).
How to Use:
 * Save the code: Save the code as a Python file (e.g., sports_db.py).
 * Run the script: Open a terminal or command prompt, navigate to the directory where you saved the file, and run it using python sports_db.py.
 * Database created: This will create a file named sports_betting.db in the same directory.
Next Steps:
 * Populate the database: You'll need to write additional Python code to insert data into these tables (sports, leagues, teams, events).
 * Implement betting logic: You'll need to create functions to handle placing bets, calculating payouts, updating user balances, etc.
 * User interface: You can use a web framework (like Flask or Django) or a GUI library (like Tkinter or PyQt) to create a user interface for your sports betting application.
 * Error handling: Add error handling to your code to gracefully handle potential issues (e.g., database connection errors, invalid input).
 * Security: Consider security measures to protect user data and prevent unauthorized access.
This script provides a basic foundation for your sports betting database. You can expand upon it to create a more feature-rich application. Remember to adapt it to your specific requirements and add the necessary functionality.
