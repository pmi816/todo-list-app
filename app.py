tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    add_task("Học bài Git ")
    add_task("Làm bài tập ")
def list_tasks():
    """Print all tasks with numbered ordering"""
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

if __name__ == "__main__":
    tasks = [
        "Học bài Git",
        "Làm bài tập",
        "Đọc tài liệu Python",
        "Viết documentation"
    ]
    
    # Call list_tasks after adding tasks
    list_tasks()

