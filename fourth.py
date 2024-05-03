import psycopg2

def get_paginated_data(limit_val, offset_val):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="JusticeForSaltanat"
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM get_paginated_data(%s, %s)', (limit_val, offset_val))
    records = cur.fetchall()
    cur.close()
    conn.close()
    return records

limit = 10  
offset = 0  
result = get_paginated_data(limit, offset)
print(result)
