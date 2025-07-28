import cloudconvert
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("API_KEY")

cloudconvert.configure(api_key=api_key, sandbox=False)


def convertPdf(link, file_name):
    try:
        job = cloudconvert.Job.create(
            payload={
                "tasks": {
                    "import-my-file": {"operation": "import/url", "url": link},
                    "convert-my-file": {
                        "operation": "convert",
                        "input": "import-my-file",
                        "filename": file_name,
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
    except cloudconvert.exceptions.ClientError as e:
        return False, ""

    job = cloudconvert.Job.wait(id=job["id"])

    for task in job["tasks"]:
        if task.get("name") == "export-my-file" and task.get("status") == "finished":
            export_task = task

    file = export_task.get("result").get("files")[0]
    return True, file["url"]
    # cloudconvert.download(filename=file_name, url=file["url"])
    # print(file["filename"])


def mergeFiles(urls,file_name):
    merge_tasks = {}
    inputs = []

    for i, url in enumerate(urls):
        name = f"import-{i}"
        merge_tasks[name] = {"operation": "import/url", "url": url}
        inputs.append(name)

    merge_tasks["merge"] = {
        "operation": "merge",
        "input": inputs,
        "filename":file_name,
        "output_format": "pdf",
    }
    merge_tasks["export"] = {"operation": "export/url", "input": ["merge"]}
    job = cloudconvert.Job.create(payload={"tasks": merge_tasks})
    job = cloudconvert.Job.wait(id=job["id"])
    file_url = ""
    for task in job["tasks"]:
        if task["name"] == "export" and task["status"] == "finished":
            file_url = task["result"]["files"][0]["url"]
            break
    return file_url


# convertPdf(link,'eyub.pdf')
def getMe():
    client =  cloudconvert.cloudconvertrestclient.default_client() 
    result = client.get('v2/users/me')
    usename = result['data']['email'].split('@')[0]
    points = result['data']['credits']
    return usename,points