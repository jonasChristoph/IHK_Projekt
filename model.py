import sqlite3
import queue
import threading


class ConnectionPool:
    def __init__(self, max_connections, **kwargs):
        self.max_connections = max_connections
        self.connection_args = kwargs
        self.connections = queue.Queue(maxsize=max_connections)
        self.lock = threading.Lock()

    def get_connection(self):
        with self.lock:
            if not self.connections.empty():
                return self.connections.get()

        return self.create_connection()

    def release_connection(self, conn):
        try:
            # Attempt to execute a simple query to check if the connection is still open
            conn.execute("SELECT 1")
        except sqlite3.ProgrammingError:
            # If a ProgrammingError is raised, the connection is closed
            pass
        else:
            # If no error occurred, put the connection back into the pool
            self.connections.put(conn)

    def create_connection(self):
        return sqlite3.connect(**self.connection_args)

    def close(self):
        with self.lock:
            while not self.connections.empty():
                conn = self.connections.get()
                conn.close()


class Database:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool

    def create_image_groups(self):
        conn = self.connection_pool.get_connection()
        try:
            conn.execute('''CREATE TABLE ImageGroups (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);''')
            conn.commit()
        finally:
            self.connection_pool.release_connection(conn)

    def create_images(self):
        conn = self.connection_pool.get_connection()
        try:
            conn.execute('''CREATE TABLE Images (
            id INTEGER PRIMARY KEY,
            name TEXT,
            dataset_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (dataset_id) REFERENCES ImageGroups(id));''')
            conn.commit()
        finally:
            self.connection_pool.release_connection(conn)

    def create_results(self):
        conn = self.connection_pool.get_connection()
        try:
            conn.execute('''CREATE TABLE Results (
            id INTEGER PRIMARY KEY,
            name TEXT,
            dataset_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (dataset_id) REFERENCES ImageGroups(id));''')
            conn.commit()
        finally:
            self.connection_pool.release_connection(conn)

    def create(self, data, database):
        pass

    def read_dataset(self, id):
        conn = self.connection_pool.get_connection()
        try:
            data = conn.execute(f'SELECT * FROM Images WHERE dataset_id = {id}')
            conn.commit()
        finally:
            self.connection_pool.release_connection(conn)
        return data

    def read_single_image(self, id):
        conn = self.connection_pool.get_connection()
        try:
            data = conn.execute(f'SELECT * FROM Images WHERE id = {id}')
            conn.commit()
        finally:
            self.connection_pool.release_connection(conn)
        return data

    def update_results(self, name, dataset_id):
        conn = self.connection_pool.get_connection()
        try:
            conn.execute(f'INSERT INTO ResultDatasets (name, dataset_id) VALUES ({name}, {dataset_id})')
            conn.commit()
        finally:
            self.connection_pool.release_connection(conn)

    def update_images(self, name, dataset_id):
        conn = self.connection_pool.get_connection()
        try:
            # Use parameter binding to safely insert values into the query
            conn.execute("INSERT INTO Images (name, dataset_id) VALUES (?, ?)", (name, dataset_id))
            conn.commit()
        finally:
            self.connection_pool.release_connection(conn)

    def delete(self, id):
        conn = self.connection_pool.get_connection()
        try:
            conn.execute(f'DELETE FROM Images WHERE id = {id}')
            conn.commit()
        finally:
            self.connection_pool.release_connection(conn)


if __name__ == '__main__':
    # Initialize the ConnectionPool
    connection_pool = ConnectionPool(max_connections=10, database='C:/Users/Jonas/Downloads/SQLiteSpy_v1.9.17/win64/Image_database.db3')

    # Initialize the Database instance with the ConnectionPool
    database = Database(connection_pool)

    # Call database methods to create tables, perform operations, etc.
    data = database.read_single_image("2")

    for row in data:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("DATASET_ID = ", row[2])
        print("TIMESTAMP = ", row[3], "\n")

    print("________________________________")
    dataset = database.read_dataset("1")

    for row in dataset:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("DATASET_ID = ", row[2])
        print("TIMESTAMP = ", row[3], "\n")

    # Close the connections when done
    connection_pool.close()
