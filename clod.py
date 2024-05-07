import cloudconvert
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("API_KEY2")

cloudconvert.configure(api_key=api_key, sandbox=False)

def convertPdf(link, file_name):
    job = cloudconvert.Job.create(
        payload={
            "tasks": {
                "import-my-file": {"operation": "import/url", "url": link},
                "convert-my-file": {
                    "operation": "convert",
                    "input": "import-my-file",
                    'filename':file_name,
                    "output_format": "pdf",
                    "some_other_option": "value",
                },
                "export-my-file": {
                    "operation": "export/url",
                    "input": "convert-my-file",
                },
            }
        }
    )

    job = cloudconvert.Job.wait(id=job["id"])

    for task in job["tasks"]:
        if task.get("name") == "export-my-file" and task.get("status") == "finished":
            export_task = task

    file = export_task.get("result").get("files")[0]
    return file["url"]
    # cloudconvert.download(filename=file_name, url=file["url"])
    # print(file["filename"])


# convertPdf(link,'eyub.pdf')
