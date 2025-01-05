import subprocess
import webbrowser

# 打开项目目录（示例路径，需根据实际情况更改）
project_path = "C:/code/py/Rent_Master/Web_ver"
webbrowser.open("http://127.0.0.1:8000/")
# 使用虚拟环境的 Python 解释器运行命令
python_executable = "C:/code/py/Rent_Master/Web_ver/ll_env/Scripts/python.exe"  # 虚拟环境的 Python 解释器路径
command = f"{python_executable} manage.py runserver"

subprocess.run(command, cwd=project_path, shell=True)

