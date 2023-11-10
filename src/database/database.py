# Importing module
import mysql.connector

# Class for Database
class DataBase():
    def __init__(self, host: int, username: str, password, database):
        self._host = host
        self._username = username
        self._password = password
        self._database = database
        self._connection = None
        self._cursor = None
    
    # Function to establish database connection
    def connect(self):
        try:
            self._connection = mysql.connector.connect(
                host = self._host,
                username = self._username,
                password = self._password,
                database = self._database   
            )   
            # check if connection is established
            if self._connection.is_connected():
                # set cursor
                self._cursor = self._connection.cursor()
        # print out error if connection failed
        except mysql.connector.Error as error:
            print(f' Connection Failed! ,"{error}"')

    def select_tables(self):
        try:
            query = "SHOW TABLES"
            if self._cursor is not None:
                self._cursor.execute(query)
                tables = self._cursor.fetchall()
                return tables
        except mysql.connector.Error as mysql_error:
            print(f"Error:  {mysql_error}")
    

    def select_content(self, table_name):
        try:
            # can be modified later to prevent sql injection attack
            query = f"SELECT * FROM {table_name}"
            if self._cursor is not None:
                self._cursor.execute(query)
                result = self._cursor.fetchall()
                self._connection.commit()
                return result
        except mysql.connector.Error as mysql_error:
            print(f"Error:  {mysql_error}")
            return False
    
    # used for fill up database with demo data
    def fill_up(self):
        try:
             # Iterate over the 8 tables
            for i in range(1, 9):
                table_name = f"Sample{i}"
                start_index = (i - 1) * 5
                end_index = i * 5
                players_data = [
                    ('LeBron James', 'The King', 'SF/PF'),
                    ('Kevin Durant', 'Durantula', 'SF/PF'),
                    ('Stephen Curry', 'Chef Curry', 'PG/SG'),
                    ('Giannis Antetokounmpo', 'The Greek Freak', 'PF/C'),
                    ('Kawhi Leonard', 'The Klaw', 'SF/PF'),
                    ('Luka Dončić', 'The Matador', 'PG/SG'),
                    ('Anthony Davis', 'The Brow', 'PF/C'),
                    ('James Harden', 'The Beard', 'SG/PG'),
                    ('Joel Embiid', 'The Process', 'C/PF'),
                    ('Damian Lillard', 'Dame Time', 'PG/SG'),
                    ('Jayson Tatum', 'Taco Jay', 'SF/PF'),
                    ('Jimmy Butler', 'Jimmy Buckets', 'SF/SG'),
                    ('Kyrie Irving', 'Uncle Drew', 'PG/SG'),
                    ('Russell Westbrook', 'Brodie', 'PG/SG'),
                    ('Chris Paul', 'CP3', 'PG'),
                    ('Paul George', 'PG13', 'SF/SG'),
                    ('Karl-Anthony Towns', 'KAT', 'C/PF'),
                    ('Trae Young', 'Ice Trae', 'PG/SG'),
                    ('Zion Williamson', 'Zanos', 'PF/C'),
                    ('Devin Booker', 'D-Book', 'SG/PG'),
                    ('Ben Simmons', 'Fresh Prince', 'PG/SF'),
                    ('Ja Morant', 'Headband 12', 'PG'),
                    ('Brandon Ingram', 'Slenderman', 'SF/SG'),
                    ('Jaylen Brown', 'JB', 'SG/SF'),
                    ('De\'Aaron Fox', 'Swipa', 'PG'),
                    ('Donovan Mitchell', 'Spida', 'SG/PG'),
                    ('Bam Adebayo', 'Bam Bam', 'C/PF'),
                    ('Jrue Holiday', 'The Holiday', 'PG/SG'),
                    ('DeMar DeRozan', 'DeMarvulous', 'SF/SG'),
                    ('Nikola Jokic', 'The Joker', 'C/PF'),
                    ('CJ McCollum', 'CJ2K', 'SG/PG'),
                    ('Myles Turner', 'The Blocksmith', 'C/PF'),
                    ('Kristaps Porziņģis', 'The Unicorn', 'PF/C'),
                    ('John Wall', 'Wall-Star', 'PG/SG'),
                    ('D\'Angelo Russell', 'D-Lo', 'PG/SG'),
                    ('LaMelo Ball', 'Meloball', 'PG/SG'),
                    ('Jamal Murray', 'Blue Arrow', 'PG/SG'),
                    ('Deandre Ayton', 'Stix', 'C'),
                    ('Tobias Harris', 'Tobi Wan Kenobi', 'SF/PF'),
                    ('Christian Wood', 'Woodbeast', 'PF/C'),
                    ]
                players_data_for_table = players_data[start_index:end_index]
                insert_query = f"INSERT INTO `{table_name}` (`Name`, `Nickname`, `Position(s)`) VALUES (%s, %s, %s)"
                self._cursor.executemany(insert_query, players_data_for_table)
                self._connection.commit()
            print(f"Inserted demo data into {table_name}")

        except mysql.connector.Error as mysql_error:
            print(f"Error: {mysql_error}")

    # Function for disconnecting from database
    def disconnect(self):
        if self._cursor is not None and self._connection.is_connected():
            self._cursor.close()
            self._connection.close()