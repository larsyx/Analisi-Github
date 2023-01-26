from github import Github
from github.GithubException import GithubException
import matplotlib.pyplot as plt
import numpy as np
import Graphql
from classFile import LanguageStatistics, UserCountry

access_token = ""
g = Github(access_token)
larsyx = g.get_user()
graph = Graphql.graphQL(access_token)

countries = []
language = []
users = []
repositories = []
MAX_PRINT = 15
path = "ResultsAnalysis/images/"

def creaArray(path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()

    temp = []
    for line in lines:
        if line[len(line)-1 : len(line)] == "\n":
            temp.append(line[0: (len(line) - 1)])
        else:
            temp.append(line)

    return temp;

def analysisRepository(repo, file):
    try:
        commits = repo.get_commits()
        contributors = repo.get_contributors()
        languages = repo.get_languages()
        brench = repo.get_branches()
        forks = repo.get_forks()
        stars = repo.stargazers_count
        releases = repo.get_releases()
        pullRequest = repo.get_pulls()
        issues = repo.get_issues()

        file.write("\n")
        print("\nANALISI REPOSITORY")
        print(repo.name)
        file.write(repo.name + ", ")
        print("#Commit:" + str(commits.totalCount))
        file.write(str(commits.totalCount) + ", ")
        print("#Contributori: " + str(contributors.totalCount))
        file.write(str(contributors.totalCount) + ", ")
        print("#Linguaggi: " + str(len(languages)))
        file.write(str(len(languages)) + ", ")
        print("#Brench: " + str(brench.totalCount))
        file.write(str(brench.totalCount) + ", ")
        print("#Forks: " + str(forks.totalCount))
        file.write(str(forks.totalCount) + ", ")
        print("#Stars: " + str(stars))
        file.write(str(stars) + ", ")
        print("#Releases: " + str(releases.totalCount))
        file.write(str(releases.totalCount) + ", ")
        print("#Pull request: " + str(pullRequest.totalCount))
        file.write(str(pullRequest.totalCount)+ ", ")
        print("#Iusses: " + str(issues.totalCount))
        file.write(str(issues.totalCount))
    except GithubException:
        print("null ")
        file.write("Repository null")

    #analysisRepository2(repo)


def analysisRepository2(repo):
    print("\nPeriodi di attività: ")

    commitActivity = repo.get_stats_commit_activity()
    codeFrequency = repo.get_stats_code_frequency()
    languages =  repo.get_languages()

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
        if r.additions > 0 or r.deletions > 0:
            weekCode.append(r.week.date())
            codeAdded.append(r.additions)
            codeRemoved.append(r.deletions)

    fig, ax = plt.subplots()
    ax.bar(weekCommit, totalComm)
    ax.set_ylabel('#Commits')
    ax.set_xlabel('Settimane')
    ax.set_title('Periodi di attività')
    plt.savefig(path +"Repository_commits_" + repo.name +".png", format="png", dpi =300)
    plt.show()

    x = range(583)
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.bar(weekCode, codeRemoved, width=1, color='r')
    ax.bar(weekCode, codeAdded, width=1, color='b')
    plt.savefig(path + "Repository_codeActivity_" + repo.name +".png", format="png", dpi =300)
    plt.show()

    # linguaggi
    print("\nLinguaggi: ")
    for language in languages:
        print("\t" + language)

    contributors = repo.get_contributors()
    commitsContributors = []
    for contributor in contributors:
        try:
            commitsContributors.append(repo.get_commits(author=contributor.login).totalCount)
        except GithubException:
            print("Repository vuoto ")

    height = np.arange(contributors.totalCount)
    plt.bar(height, commitsContributors, align='center')
    plt.xticks(height)
    plt.xlabel("Users")
    plt.ylabel("Commits")
    plt.savefig(path + "ContributorsStatistics_" +repo.name + ".png", format="png")
    plt.show()

def analysisUser(user, file):
    repository = user.get_repos()
    file.write("\n")
    print("\nANALISI UTENTE")
    print("Login:" + user.login)
    file.write(user.login + ", ")
    print("Nome: ", user.name)
    if user.name == None:
        file.write("NoName, ")
    else:
        file.write(user.name + ", ")
    print("Profilo creato il: " + str(user.created_at))
    print("#Repository: " + str(repository.totalCount))
    file.write(str(repository.totalCount) + ", ")
    print("#Followers: " + str(user.followers))
    file.write(str(user.followers) + ", ")

    tot_commits = 0
    for repo in repository:
        try:
            tot_commits += repo.get_commits(author=user.login).totalCount
        except GithubException:
            print("Repository vuoto ")

    print("#Commits: " + str(tot_commits))
    file.write(str(tot_commits))
    return tot_commits

def analysisUsers():
    file = open("ResultsAnalysis/UsersStatistics.csv", "w+")
    file.write("Login, Nome, #Repository, #Followers, #Commits")

    commits = []
    for user in users:
        try:
            commits.append(analysisUser(g.get_user(user), file))
        except GithubException:
            print("users null: " + user)
            file.write("\nUsers null: " + user)

    file.close()

    height = np.arange(len(users))
    plt.bar(height, commits, align='center')
    plt.xticks(height)
    plt.xlabel("Users")
    plt.ylabel("Commits")
    plt.savefig(path + "UsersStatistics.png", format="png")
    plt.show()

def smallAnalysisRepositories():
    print("\n\n\nRepository in Python")
    repositories = g.search_repositories(query='language:Python')
    print(repositories.totalCount)
    i = 0
    for r in repositories:
        print(str(i) + " " + r.name + " " + r.url + "total commit: " + str(r.get_commits().totalCount))
        i += 1
        for l in r.get_languages():
            print("\t" + l)

def analysisRepositories():
    file = open("ResultsAnalysis/RepositoriesAnalysis.csv", "w+")
    file.write("Name, #Commits, #Contributors, #Languages, #Brench, #Forks, #Stars, #Releases, #Pull request, #Iusses")
    for repo in repositories:
        try:
            analysisRepository(g.get_repo(repo), file)
        except GithubException:
            print("null "+ repo)
            file.write("\nrepository null " + repo )


    file.close()

def analysisProgrammingLanguages():
    resultLanguages = []
    for lang in language:
        p1 = LanguageStatistics(lang, graph.getTotalRepositoryByLanguage(lang))
        resultLanguages.append(p1)

    file = open("ResultsAnalysis/LanguageStatistics.csv", "w+")
    file.write("Language, Repository\n")
    for res in resultLanguages:
        file.write(res.name +", " + str(res.value) + "\n")
    file.close()

    resultLanguages.sort(key=lambda x: x.value, reverse=True)
    values, names = [], []
    maxPlot = MAX_PRINT
    if len(resultLanguages) < MAX_PRINT:
        maxPlot = len(resultLanguages)

    for i in range(0, maxPlot):
        values.append(resultLanguages[i].value)
        names.append(resultLanguages[i].name)

    plt.pie(values)
    plt.legend(names, title="Language", bbox_to_anchor=(1, 0.5), loc="center right", bbox_transform=plt.gcf().transFigure)
    plt.savefig(path + "ProgrammingLanguage.png", format="png")
    plt.show()

def analysisUserForCountry():
    result = []
    for country in countries:
        p = UserCountry(country, graph.getUserByCountry(country))
        result.append(p)

    file = open("ResultsAnalysis/UsersForCountry.csv", "w+")
    file.write("Country, #Users\n")
    for res in result:
        file.write(res.country +", " + str(res.value) + "\n")
    file.close()

    result.sort(key=lambda x: x.value, reverse=True)
    values, names = [], []
    maxPlot = MAX_PRINT
    if len(result) < MAX_PRINT:
        maxPlot = len(result)

    for i in range(0, maxPlot):
        values.append(result[i].value)
        names.append(result[i].country)
    plt.figure()
    plt.pie(values)
    plt.legend(names, title="Country", bbox_to_anchor=(1, 0.5), loc="center right", bbox_transform=plt.gcf().transFigure)
    plt.savefig(path + "UsersForCountry.png", format="png")
    plt.show()

def main():
    #analysisUsers()
    #analysisRepositories()
    #analysisProgrammingLanguages()
    #analysisUserForCountry()

    print("\n\n\n" + str(g.get_rate_limit()))

if __name__ == "__main__":
    language = creaArray("InputAnalysis/LanguageList.txt")
    countries = creaArray("InputAnalysis/CountriesList.txt")
    users = creaArray("InputAnalysis/UsersLogin.txt")
    repositories = creaArray("InputAnalysis/RepositoryList.txt")
    main()

