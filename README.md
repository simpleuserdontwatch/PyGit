# PyGit
Github api for python!
# Requirements
- requests. Thats all.
# How to use
First, log in into your account using [token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), using `login(token="",method="var")`, like this
```
login(token="<YOUR TOKEN HERE>", method="token")
```
Or login through a variable
```
C:\>setx GIT_TOKEN <YOUR TOKEN HERE>
C:\>python
>>> login()
```
And yea, its 10x easier to login with variable, and more secure.

I dont really know how to describe how to use it, so heres documentation:

- `login(token="",method="var")`\
  Login using token.
- `getrepos()`\
  Get all your repo's
- `getmyuser()`\
  Get your user details.
- `getuser(user)`\
  Get details of a user.
- `getfollowers()`\
  Get your followers.
- `isfollowing(user)`\
  Check if `user` is following you
- `getissues()`\
  Get all issues.
- `createissue(repo,title,body="")`\
  Create an issue.
- `comment(repo,issue,body="")`\
  Comments on a repo's issue
- `getcomments(repo,issue)`\
  Get comments of a issue.
- `reopenissue(repo,issue)`\
  Reopen an issue.
- `closeissue(repo,issue)`\
  Closes issue.
- `createrepo(name,desc="",private=False,homepage="",template=False)`\
  Create a repo.
