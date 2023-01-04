from threading import Thread
from github import Github
from github.GithubException import GithubException
import matplotlib.pyplot as plt
import numpy as np
import Graphql

access_token = "<your token>"
g = Github(access_token)
larsyx = g.get_user()
graph = Graphql.graphQL(access_token)

countries = []
language = []


def creaArrayLanguage():
    file = open("LanguageList.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        language.append(line[0: (len(line) - 1)])


def creaArrayCountries():
    file = open("CountriesList.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        countries.append(line[0: (len(line) - 1)])


def trovaThread(repository, author):
    tot_commits = 0
    for repo in repository:
        try:
            tot_commits += repo.get_commits(author=author).totalCount
        except GithubException:
            print("Repository vuoto ")

    print("#Commits: " + str(tot_commits))


def analysisRepository(repo):
    commits = repo.get_commits()
    contributors = repo.get_contributors()
    languages = repo.get_languages()
    brench = repo.get_branches()
    forks = repo.get_forks()
    stars = repo.stargazers_count
    releases = repo.get_releases()
    pullRequest = repo.get_pulls()
    issues = repo.get_issues()

    commitActivity = repo.get_stats_commit_activity()
    codeFrequency = repo.get_stats_code_frequency()

    print("\nANALISI REPOSITORY")
    print(repo.name)
    print("#Commit:" + str(commits.totalCount))
    print("#Contributori: " + str(contributors.totalCount))
    print("#Linguaggi: " + str(len(languages)))
    print("#Brench: " + str(brench.totalCount))
    print("#Forks: " + str(forks.totalCount))
    print("#Stars: " + str(stars))
    print("#Releases: " + str(releases.totalCount))
    print("#Pull request: " + str(pullRequest.totalCount))
    print("#Iusses: " + str(issues.totalCount))

    print("\nPeriodi di attività: ")
    weekCommit = []
    totalComm = []
    for comm in commitActivity:
        print("\tsettimana del: " + str(comm.week.date()) + " #Commits: " + str(comm.total))
        weekCommit.append(comm.week.date())
        totalComm.append(comm.total)

    weekCode = []
    codeAdded = []
    codeRemoved = []
    print("\nFrequenza di codice: ")
    for r in codeFrequency:
        print("\t" + str(r.week.date()) + " Linee di codice aggiunti: " + str(
            r.additions) + "\t Linee di codice rimossi " + str(r.deletions))
        if r.additions>0 or r.deletions>0 :
            weekCode.append(r.week.date())
            codeAdded.append(r.additions)
            codeRemoved.append(r.deletions)

    fig, ax = plt.subplots()
    ax.bar(weekCommit, totalComm)
    ax.set_ylabel('#Commits')
    ax.set_xlabel('Settimane')
    ax.set_title('Periodi di attività')
    plt.show()

    x = range(583)
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.bar(weekCode, codeRemoved, width=1, color='r')
    ax.bar(weekCode, codeAdded, width=1, color='b')

    plt.show()

    # linguaggi
    print("\nLinguaggi: ")
    for language in languages:
        print("\t" + language)

    # contributori


# print("\nContributori: ")
# for coll in contributors:
#   print("\t" + coll.login + " " + str(coll.contributions))

def analysisUser(user):
    repository = user.get_repos()
    thread = Thread(target=trovaThread, args=(repository, user.login))
    thread.start()
    print("\nANALISI UTENTE")
    print("Login:" + user.login)
    print("Nome: " + user.name)
    print("Profilo creato il: " + str(user.created_at))
    print("#Repository: " + str(repository.totalCount))
    print("#Followers: " + str(user.followers))
    thread.join()


def analysisRepositories():
    print("\n\n\nRepository in Python")
    repositories = g.search_repositories(query='language:Python')
    print(repositories.totalCount)
    i = 0
    for r in repositories:
        print(str(i) + " " + r.name + " " + r.url + "total commit: " + str(r.get_commits().totalCount))
        i += 1
        for l in r.get_languages():
            print("\t" + l)

def analysisProgrammingLanguages():
    resultLanguages = []
    for lang in language:
        resultLanguages.append(graph.getTotalRepositoryByLanguage(lang))

    plt.pie(resultLanguages)
    plt.legend(language,title="Language",bbox_to_anchor=(1,0.5), loc="center right", bbox_transform=plt.gcf().transFigure)
    plt.show()

def main():
    # analysisRepository(g.get_repo("apache/kibble-1"))
    analysisRepository(g.get_repo("apache/dubbo"))
    # analysisUser(g.get_user("taowen"))
    # analysisRepositories()
    analysisProgrammingLanguages()


    print("\n\n\n" + str(g.get_rate_limit()))

if __name__ == "__main__":
    creaArrayLanguage()
    creaArrayCountries()
    main()
