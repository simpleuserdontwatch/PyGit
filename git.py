import os
import requests
import json
logintoken = None
def login(token="",method="var"):
    global logintoken
    if method == "var":
        print(os.environ)
        logintoken = os.environ.get("GIT_TOKEN",None)
        print(logintoken)
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
