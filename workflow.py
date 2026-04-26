from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from activity import GreetingActivities


@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        retry_policy = RetryPolicy(maximum_attempts=3, maximum_interval=timedelta(seconds=2))

        greeting = await workflow.execute_activity_method(
            GreetingActivities.say_hello,
            name,
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy,
        )
        return greeting
