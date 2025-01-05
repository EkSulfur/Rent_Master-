import os
import subprocess


def create_virtual_env(env_name):
    # 获取脚本所在目录的路径
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # 完整的虚拟环境路径
    env_path = os.path.join(script_dir, "Web_ver", env_name)

    # 检查虚拟环境是否已存在
    if not os.path.exists(env_path):
        print(f"Creating virtual environment at: {env_path}")
        # 创建虚拟环境
        subprocess.run([os.sys.executable, '-m', 'venv', env_path])
        print(f"Virtual environment created at: {env_path}")
    else:
        print(f"Virtual environment already exists at: {env_path}")

    # 安装依赖
    pip_path = os.path.join(env_path, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(env_path, 'bin', 'pip')
    requirements_path = os.path.join(script_dir, 'requirements.txt')

    if os.path.exists(requirements_path):
        print("Installing dependencies...")
        subprocess.run([pip_path, 'install', '-r', requirements_path])
        print("Dependencies installed.")
    else:
        print("No requirements.txt file found. No dependencies were installed.")


# 虚拟环境的名称
env_name = 'venv'  # 您可以根据需要更改此名称
create_virtual_env(env_name)
