import PyGithub
# or using an access token
g = Github("bc6de7e390d28b8ad7f7b7c325eaa9b64bf59d9a")

#test
for repo in g.get_user().get_repos():
    print (repo.name)
    repo.edit(has_wiki=False)