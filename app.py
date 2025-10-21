tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    def add_task(task_name):
    """Add a new task to the list"""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: {task_name}")

def complete_task(task_index):
    """Mark a task as completed"""
    if 1 <= task_index <= len(tasks):
        tasks[task_index-1]['completed'] = True
        print(f"Đã đánh dấu công việc {task_index} là hoàn thành")
    else:
        print("Chỉ số công việc không hợp lệ!")

def list_tasks():
    """Print all tasks with numbered ordering and completion status"""
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")

if __name__ == "__main__":
    tasks = []
    
    # Add some initial tasks
    add_task("Học bài Git")
    add_task("Làm bài tập")
    add_task("Đọc sách")
    
    # List tasks
    list_tasks()
    
    # Mark first task as completed
    complete_task(1)
    
    # List tasks again to see the change
    list_tasks()
    