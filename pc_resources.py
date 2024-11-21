import psutil

print(f"Загрузка CPU: {psutil.cpu_percent(interval=1, percpu=True)}%")
print(f"Использование RAM: {psutil.virtual_memory().percent}%")