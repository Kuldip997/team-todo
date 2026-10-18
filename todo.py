tasks = []

def add_task(name):
    tasks.append(name)
    print(f"Addd: {name}")

def list_tasks():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

# ---- new commands go below this line ----

if __name__ == "__main__":
    add_task("Learn Git")
    list_tasks() 

def mark_done(index):
    tasks[index - 1] = tasks[index - 1] + "[done]"
    print(f"Marked done: {tasks[index - 1]}")

    list_tasks()

def delete_task(index):
    removed = tasks.pop(index - 1)
    print(f"Deleted: {removed}")
