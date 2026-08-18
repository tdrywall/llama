import os

from dotenv import load_dotenv
from llama_index.core.workflow import Event, StartEvent, StopEvent, Workflow, step
from llama_parse import LlamaParse

load_dotenv()


class ParseResultEvent(Event):
    result: str


class LlamaParseWorkflow(Workflow):
    """A simple workflow that parses a document using LlamaParse."""

    @step
    async def parse(self, ev: StartEvent) -> StopEvent:
        file_path: str = ev.get("file_path", "")
        if not file_path:
            return StopEvent(result="No file_path provided.")

        parser = LlamaParse(
            api_key=os.environ["LLAMA_CLOUD_API_KEY"],
            result_type="markdown",
        )
        documents = await parser.aload_data(file_path)
        combined = "\n\n".join(doc.text for doc in documents)
        return StopEvent(result=combined)
