import cloudconvert
import base64
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("API_KEY")

cloudconvert.configure(api_key=api_key, sandbox=False)

f = open("Notes_from_Underground.epub", "rb")
encoded_string = base64.b64encode(f.read()).decode('utf-8')
#decf = encoded_string.decode('utf-8')

job = cloudconvert.Job.create(
    payload={
        "tasks": {
            'import-my-file': {
                "file": encoded_string,
                "filename": "Notes_from_Underground.epub",
            },
            "convert-my-file": {
                "operation": "convert",
                "input": "import-my-file",
                "output_format": "pdf",
            },
            "export-my-file": {"operation": "export/url", "input": "convert-my-file"},
        }
    }
)

job = cloudconvert.Job.wait(id=job["id"])

for task in job["tasks"]:
    if task.get("name") == "export-it" and task.get("status") == "finished":
        export_task = task

file = export_task.get("result").get("files")[0]
res = cloudconvert.download(filename=file["filename"], url=file["url"])
print(type(res))
