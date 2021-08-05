#convert github link in to raw.githubusercontent
import requests

repo_name = "Gmod_CarSound" #repository name
repo_user = "ElTaistos"     #user name
repo_branch = "main"        #branch name
format_type = ".mp3"        #format

link = "https://api.github.com/repos/{0}/{1}/git/trees/{2}?recursive=1".format(repo_user, repo_name, repo_branch)
response = requests.get(link).json()

tree = response["tree"]

files_raw_path = []

for node in tree:
    if node["path"][-len(format_type):] == format_type:
        raw = "https://raw.githubusercontent.com/{0}/{1}/{2}/{3}".format(repo_user, repo_name, repo_branch, node["path"])
        files_raw_path.append(raw)

print("--- List of raw detected ---")
for raw in files_raw_path:
    print(raw)