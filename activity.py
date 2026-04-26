import asyncio

from temporalio import activity


class GreetingActivities:
    @activity.defn
    async def say_hello(self, name: str) -> str:
        try:
            return await asyncio.to_thread(self._build_greeting, name)
        except Exception:
            activity.logger.exception("Activity failure")
            raise

    def _build_greeting(self, name: str) -> str:
        return f"Hello, {name}! Welcome to simple-temporal."