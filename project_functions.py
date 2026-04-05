from db_connection import conn, cursor

def add_project():
    client_id = int(input("Enter client ID: "))
    project_name = input("Enter project name: ")
    project_type = input("Enter project type: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    budget = float(input("Enter project budget: "))

    query = """
    INSERT INTO Projects(client_id, project_name, project_type, start_date, deadline, status, budget)
    VALUES (%s, %s, %s, CURDATE(), %s, 'Pending', %s)
    """

    values = (client_id, project_name, project_type, deadline, budget)

    cursor.execute(query, values)
    conn.commit()

    print("Project added successfully!")

def view_projects():
    query = """
    SELECT project_id, project_name, project_type, deadline, status, budget
    FROM Projects
    """

    cursor.execute(query)
    result = cursor.fetchall()

    print("\n===== PROJECT LIST =====")
    for row in result:
        print(row)