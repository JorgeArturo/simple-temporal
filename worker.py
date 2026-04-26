import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activity import GreetingActivities
from workflow import GreetingWorkflow

TASK_QUEUE = "SIMPLE_TEMPORAL_TASK_QUEUE"


async def main() -> None:
    client = await Client.connect("localhost:7233", namespace="default")
    activities = GreetingActivities()
    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[GreetingWorkflow],
        activities=[activities.say_hello],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())