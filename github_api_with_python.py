from github import Github
g = Github("rushantnarula", "rishuri1")
g = Github('1eaa3fc8f83c16b1d35b601637f69247202b11b5')

#Access to our repositories
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    #print names of our repositories
    print(dir(repo))

#get user name
user = g.get_user()
user.login
print(user)

#Get readme of a repo
readme = repo.get_readme()

#Get releases of a repo
releases = repo.get_releases()
releases_id_list = []
for release in releases:
	releases_id_list.append(release.id)

#Get pull requests for a repo
pulls = repo.get_pulls()
pulls_numbers_list = []
for pull in pulls:
	pulls_numbers_list.append(pull.number)
print(pulls_numbers_list)

#create new Repo
#user = g.get_user()
#repo = user.create_repo('NewRepo')

repo = g.get_repo("Pygithub/Pygithub")
contents = repo.get_contents("")
for content_file in contents:
     print(content_file)

#create a new file in a repo
repo = g.get_repo("PyGithub/NewRepo")
repo.create_file("test.txt", "test", "test", branch="test")

#Get list of branches
repo = g.get_repo("PyGithub/NewRepo")
list(repo.get_branches())

#get Pull reques
repo = g.get_repo("PyGithub/NewRepo")
pr = repo.get_pull(664)
pr