from flask import Flask, request, jsonify
import asyncio
from temporalio.client import Client
from workflow import GreetingWorkflow

app = Flask(__name__)

TEMPORAL_SERVER = "localhost:7233"
TASK_QUEUE = "SIMPLE_TEMPORAL_TASK_QUEUE"


# 👉 Servir HTML sin Jinja
@app.route("/")
def home():
    with open("templates/index.html") as f:
        return f.read()


# 👉 Endpoint para lanzar workflow
@app.route("/start", methods=["POST"])
def start_workflow():
    name = request.args.get("name")

    async def run():
        client = await Client.connect(TEMPORAL_SERVER)

        result = await client.execute_workflow(
            GreetingWorkflow.run,
            name,
            id=f"hello-{name}",
            task_queue=TASK_QUEUE,
        )
        return result

    result = asyncio.run(run())

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)