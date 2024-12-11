from clearml import Task
from clearml.automation import PipelineController

# Создаем ClearML пайплайн
pipeline = PipelineController(
    name="Simple Pipeline",
    project="Demo Project",
    version="1.0"
)

# Определяем первую задачу
def step_one():
    task = Task.init(project_name="Demo Project", task_name="Step One")
    print("Step One Complete!")
    task.close()

# Определяем вторую задачу
def step_two():
    task = Task.init(project_name="Demo Project", task_name="Step Two")
    print("Step Two Complete!")
    task.close()

# Добавляем шаги в пайплайн
pipeline.add_function_step(name="Step One", function=step_one)
pipeline.add_function_step(name="Step Two", function=step_two, parents=["Step One"])

# Запускаем пайплайн
pipeline.start_locally(run_pipeline_steps_locally = True)
