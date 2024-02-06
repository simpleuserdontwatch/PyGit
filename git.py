import os
import requests
import json
from zipfile import ZipFile
import tempfile
import base64

logintoken = None
def login(token="",method="var"):
    global logintoken
    if method == "var":
        logintoken = os.environ.get("GIT_TOKEN",None)
        if not logintoken:
            raise Exception('No variable found "GIT_TOKEN".')
        
    elif method == "token":
        logintoken = token
    else:
        raise Exception("Invalid login method")

def getrepos():
    req = requests.get("https://api.github.com/user/repos",headers={"Authorization":f"token {logintoken}"})

    return req.json()

def getmyuser():
    req = requests.get("https://api.github.com/user",headers={"Authorization":f"token {logintoken}"})

    return req.json()

def getuser(user):
    req = requests.get(f"https://api.github.com/users/{user}")

    return req.json()

def getfollowers():
    req = requests.get("https://api.github.com/user/followers",headers={"Authorization":f"token {logintoken}"})

    return req.json()

def isfollowing(user):
    req = requests.get(f"https://api.github.com/user/following/{user}",headers={"Authorization":f"token {logintoken}"})
    try:
        req.json()
        return False
    except: return True

def getissues():
    req = requests.get("https://api.github.com/user/issues",headers={"Authorization":f"token {logintoken}"})

    return req.json()

def createissue(repo,title,body=""):
    req = requests.post(f"https://api.github.com/repos/{repo}/issues",headers={"Authorization":f"token {logintoken}"},json={
        "title": title,
        "body": body
    })

    return req.json()

def comment(repo,issue,body=""):
    req = requests.post(f"https://api.github.com/repos/{repo}/issues/{issue}/comments",headers={"Authorization":f"token {logintoken}"},json={
        "body": body
    })

    return req.json()

def getcomments(repo,issue):
    req = requests.get(f"https://api.github.com/repos/{repo}/issues/{issue}/comments",headers={"Authorization":f"token {logintoken}"})

    return req.json()

def reopenissue(repo,issue):
    req = requests.patch(f"https://api.github.com/repos/{repo}/issues/{issue}",headers={"Authorization":f"token {logintoken}"},json={
        "state": "open"
    })

def closeissue(repo,issue):
    req = requests.patch(f"https://api.github.com/repos/{repo}/issues/{issue}",headers={"Authorization":f"token {logintoken}"},json={
        "state": "close"
    })

def createrepo(name,desc="",private=False,homepage="",template=False):
    req = requests.post(f"https://api.github.com/user/repos",headers={"Authorization":f"token {logintoken}"},json={
        "name": name,
        "description": desc,
        "private": private,
        "homepage": homepage,
        "is_template": template
    })

def saverepo(repo, info=False):
    temp = tempfile.NamedTemporaryFile()
    temp.close()
    with open(temp.name, "wb") as f:
        req = requests.get(f"https://github.com/{repo}/archive/master.zip", stream=True)
        if info:
            print(f"Downloading {repo}")
        size = int(req.headers.get("Content-Length", 0))
        if not size:
            size = len(req.content)
        if info:
            print(f"Repo Size: {size}B")
        downloaded = 0
        for chunk in req.iter_content(chunk_size=2048):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                percent = int((downloaded / size) * 100)
                if info:
                    print(f"<{'='*(percent//2)}{' '*(50-(percent//2))}>{percent}%")
        if info:
            print("Extracting..")
    zf = ZipFile(temp.name, 'r')
    zf.extractall()
    zf.close()

def listfiles(repo,branch="main"):
    req = requests.get(f"https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1")

    return req.json()

def createfile(repo,path,file,commitmsg=""):
    with open(file,"rb") as f:
        data = base64.b64encode(f.read()).decode()
    req = requests.put(f"https://api.github.com/repos/{repo}/contents/{path}",headers={"Authorization":f"Bearer {logintoken}"},json={
        "message":commitmsg,
        "content":data
    })
    return req.json()
def updatefile(repo,path,file,sha,commitmsg=""):
    with open(file,"rb") as f:
        data = base64.b64encode(f.read()).decode()
    req = requests.put(f"https://api.github.com/repos/{repo}/contents/{path}",headers={"Authorization":f"Bearer {logintoken}"},json={
        "message":commitmsg,
        "content":data,
        "sha": sha
    })
    return req.json()
def deletefile(repo,path,sha,commitmsg=""):
    req = requests.delete(f"https://api.github.com/repos/{repo}/contents/{path}",headers={"Authorization":f"token {logintoken}"},json={
        "message":commitmsg,
        "sha":sha
    })
