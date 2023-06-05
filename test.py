import psycopg2
import random
import string
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from statistics import median

# Constants
DB_NAME = "my_database"
DB_USER = "my_user"
DB_PASSWORD = ""
DB_HOST = "stressdb"
DB_PORT = "5432"
TABLE_NAME = "test_kv"
NUM_THREADS = 10
NUM_QUERIES = 1000

def stress__select_name(cur):
    cur.execute(f"SELECT * FROM {TABLE_NAME} WHERE name = %s", (f"Name{random.randint(0, 1000000)}",))
    cur.fetchall()

def stress__select_value(cur):
    cur.execute(f"SELECT * FROM {TABLE_NAME} WHERE value = %s", (random.randint(0, 1000000),))
    cur.fetchall()

def stress__insert(cur):
    cur.execute(f"INSERT INTO {TABLE_NAME} (name, value) VALUES (%s, %s)",
                    (f"Name{random.randint(0, 1000000)}", random.randint(0, 1000000)))

# Global variables
query_times = []
query_lock = threading.Lock()

# Function to generate random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Function to execute select queries
def execute_stress():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    with conn.cursor() as cur:
        start_time = time.time()
        name, func = random.choice(list(stresses.items()))
        func(cur)
        end_time = time.time()

        with query_lock:
            query_times.append((name, end_time - start_time))
            if not len(query_times) % 100:
                print(f"Executed {len(query_times)} queries")

    conn.close()

stresses = {}
for name in globals().copy():
    if name.startswith("stress__"):
        stresses[name.replace("stress__", "")] = globals()[name]

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    print("Starting stress test")
    select_times = executor.map(lambda _: execute_stress(), range(NUM_QUERIES))


for name in stresses.keys():
    print("=" * 10)
    times = [x[1] for x in query_times if x[0] == name]
    print(f"Stress test: {name}")
    print(f"Number of {name} queries: {len(times)}")
    if len(times):
        print(f"Average {name} execution time: {sum(times) / len(times):.6f} seconds")
        print(f'Max {name} execution time: {max(times):.6f} seconds')
        print(f'Median {name} execution time: {median(times):.6f} seconds')
