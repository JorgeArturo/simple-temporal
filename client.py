import asyncio

from temporalio.client import Client

from workflow import GreetingWorkflow

TASK_QUEUE = "SIMPLE_TEMPORAL_TASK_QUEUE"


async def main() -> None:
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        GreetingWorkflow.run,
        "World",
        id="greeting-workflow-1",
        task_queue=TASK_QUEUE,
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())