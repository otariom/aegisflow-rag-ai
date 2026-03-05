import subprocess
import sys
import os


def run_backend():
    return subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "backend.main:app", "--reload", "--port", "8000"]
    )


def run_frontend():
    return subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "frontend/app.py", "--server.port", "8501"]
    )


def main():
    print("Starting AegisFlow System...")

    backend = run_backend()
    frontend = run_frontend()

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\nShutting down services...")
        backend.terminate()
        frontend.terminate()


if __name__ == "__main__":
    main()