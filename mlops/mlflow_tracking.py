import mlflow
import time


mlflow.set_experiment("AegisFlow")


def log_llm_run(question: str, prompt: str, answer: str, model: str = "llama3.2"):
    """
    Logs an LLM inference run to MLflow.
    """

    start_time = time.time()

    with mlflow.start_run():

        mlflow.log_param("model", model)
        mlflow.log_param("question", question)

        mlflow.log_text(prompt, "prompt.txt")
        mlflow.log_text(answer, "answer.txt")

        duration = time.time() - start_time
        mlflow.log_metric("response_time_seconds", duration)