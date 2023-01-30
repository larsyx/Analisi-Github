import pandas as pd
import os
import matplotlib.pyplot as plt
import collections
import seaborn as sns

datapath = os.path.join("ResultsAnalysis", "")
datasetUsers = pd.read_csv(datapath + "UsersStatistics.csv")
datasetRepositories = pd.read_csv(datapath + "RepositoriesAnalysis.csv")

path = "ResultsAnalysis/images/"


def getCommitsCategories():
    mapCommitsMap = {}
    for commit in datasetUsers[" #Commits"]:
        if mapCommitsMap.get(commit):
            mapCommitsMap[commit] = mapCommitsMap[commit] + 1
        else:
            mapCommitsMap[commit] = 1

    mapCommitsMap = collections.OrderedDict(sorted(mapCommitsMap.items()))

    categories = {}
    for map in mapCommitsMap:
        if map == 0:
            categories["0"] = mapCommitsMap[map]
        elif map >= 1 and map <= 50:
            num = 0
            if categories.get("1-50"):
                num = categories["1-50"]
            categories["1:50"] = num + mapCommitsMap[map]
        elif map >= 51 and map <= 100:
            num = 0
            if categories.get("51-100"):
                num = categories["51-100"]
            categories["51-100"] = num + mapCommitsMap[map]
        elif map >= 101 and map <= 150:
            num = 0
            if categories.get("101-150"):
                num = categories["101-150"]
            categories["101-150"] = num + mapCommitsMap[map]

        elif map >= 151 and map <= 200:
            num = 0
            if categories.get("151-200"):
                num = categories["151-200"]
            categories["151-200"] = num + mapCommitsMap[map]
        elif map >= 201 and map <= 250:
            num = 0
            if categories.get("201-250"):
                num = categories["201-250"]
            categories["201-250"] = num + mapCommitsMap[map]
        elif map >= 251 and map <= 300:
            num = 0
            if categories.get("251-300"):
                num = categories["251-300"]
            categories["251-300"] = num + mapCommitsMap[map]
        elif map >= 301 and map <= 350:
            num = 0
            if categories.get("301-350"):
                num = categories["301-350"]
            categories["301-350"] = num + mapCommitsMap[map]
        elif map >= 351 and map <= 400:
            num = 0
            if categories.get("351-400"):
                num = categories["351-400"]
            categories["351-400"] = num + mapCommitsMap[map]
        elif map >= 401 and map <= 450:
            num = 0
            if categories.get("401-450"):
                num = categories["401-450"]
            categories["401-450"] = num + mapCommitsMap[map]
        elif map >= 451 and map <= 500:
            num = 0
            if categories.get("451-500"):
                num = categories["451-500"]
            categories["451-500"] = num + mapCommitsMap[map]
        elif map >= 501 and map <= 600:
            num = 0
            if categories.get("501-600"):
                num = categories["501-600"]
            categories["501-600"] = num + mapCommitsMap[map]
        elif map >= 601 and map <= 700:
            num = 0
            if categories.get("601-700"):
                num = categories["601-700"]
            categories["601-700"] = num + mapCommitsMap[map]
        elif map >= 701 and map <= 800:
            num = 0
            if categories.get("701-800"):
                num = categories["701-800"]
            categories["701-800"] = num + mapCommitsMap[map]
        elif map >= 801 and map <= 900:
            num = 0
            if categories.get("801-900"):
                num = categories["801-900"]
            categories["801-900"] = num + mapCommitsMap[map]
        elif map >= 901:
            num = 0
            if categories.get("901+"):
                num = categories["901+"]
            categories["901+"] = num + mapCommitsMap[map]

    return categories


def getRepositoriesUserCategories():
    mapCommitsMap = {}
    for commit in datasetUsers[" #Repository"]:
        if mapCommitsMap.get(commit):
            mapCommitsMap[commit] = mapCommitsMap[commit] + 1
        else:
            mapCommitsMap[commit] = 1

    mapCommitsMap = collections.OrderedDict(sorted(mapCommitsMap.items()))

    categories = {}
    for map in mapCommitsMap:
        if map == 0:
            categories["0"] = mapCommitsMap[map]
        elif map >= 1 and map <= 50:
            num = 0
            if categories.get("1-50"):
                num = categories["1-50"]
            categories["1-50"] = num + mapCommitsMap[map]
        elif map >= 51 and map <= 100:
            num = 0
            if categories.get("51-100"):
                num = categories["51-100"]
            categories["51-100"] = num + mapCommitsMap[map]
        elif map >= 101 and map <= 150:
            num = 0
            if categories.get("101-150"):
                num = categories["101-150"]
            categories["101-150"] = num + mapCommitsMap[map]

        elif map >= 151 and map <= 200:
            num = 0
            if categories.get("151-200"):
                num = categories["151-200"]
            categories["151-200"] = num + mapCommitsMap[map]
        elif map >= 201 and map <= 250:
            num = 0
            if categories.get("201-250"):
                num = categories["201-250"]
            categories["201-250"] = num + mapCommitsMap[map]
        elif map >= 251 and map <= 300:
            num = 0
            if categories.get("251-300"):
                num = categories["251-300"]
            categories["251-300"] = num + mapCommitsMap[map]
        elif map >= 301 and map <= 350:
            num = 0
            if categories.get("301-350"):
                num = categories["301-350"]
            categories["301-350"] = num + mapCommitsMap[map]
        elif map >= 351 and map <= 400:
            num = 0
            if categories.get("351-400"):
                num = categories["351-400"]
            categories["351-400"] = num + mapCommitsMap[map]
        elif map >= 401:
            num = 0
            if categories.get("401+"):
                num = categories["401+"]
            categories["401+"] = num + mapCommitsMap[map]
    return categories


def usersCommit():
    print("Commit")

    plt.figure(figsize=(12,9))

    categories = getCommitsCategories()
    plt.bar(categories.keys(), categories.values(), width=1, edgecolor="white", linewidth=0.7)
    plt.xticks(rotation=45)
    plt.xlabel("Commits")
    plt.ylabel("Users")
    plt.savefig(path + "/UsersCommit" + ".png", format="png", dpi=300)
    plt.show()


def usersRepository():
    print("User repository")

    plt.figure(figsize=(12,9))

    categories = getRepositoriesUserCategories()
    plt.bar(categories.keys(), categories.values(), width=1, edgecolor="white", linewidth=0.7)
    plt.xticks(rotation=45)
    plt.xlabel("Repositories")
    plt.ylabel("Users")
    plt.savefig(path + "/UsersRepositories" + ".png", format="png", dpi=300)
    plt.show()


def userScatter():
    print("Scatter")

    datasetUsers.plot(x=' #Repository', y=' #Followers', kind='scatter')
    plt.savefig(path + "UsersScatterplot" + ".png", format="png", dpi=300)
    plt.show()


def userHeatmap():
    print("heatmap")
    fig = plt.figure()
    ax = fig.add_subplot()

    ax = sns.heatmap(datasetUsers.iloc[:, 2:5].corr().round(2), annot=True)

    fig.savefig(path + "/UserHeatmap" + ".png", format="png", dpi=300)
    plt.show()


def users():
    print(datasetUsers.describe())
    print(datasetUsers.isnull().sum())
    usersCommit()
    usersRepository()
    userScatter()
    userHeatmap()


def repositoriesHeatmap():
    print("heatmap")
    fig = plt.figure()
    fig.set_size_inches(9, 10)

    ax = fig.add_subplot()

    ax = sns.heatmap(datasetRepositories.iloc[:, 1:10].corr().round(2), annot=True)

    fig.savefig(path + "/RepositoriesHeatmap" + ".png", format="png", dpi=300)
    plt.show()


def repositoriesScatter():
    print("Scatter")

    datasetRepositories.plot(x=' #Commits', y=' #Contributors', kind='scatter')
    plt.savefig(path + "RepositoryScatterplot_1" + ".png", format="png", dpi=300)
    plt.show()

    datasetRepositories.plot(x=' #Commits', y=' #Iusses', kind='scatter')
    plt.savefig(path + "RepositoryScatterplot_2" + ".png", format="png", dpi=300)
    plt.show()

    datasetRepositories.plot(x=' #Contributors', y=' #Stars', kind='scatter')
    plt.savefig(path + "RepositoryScatterplot_3" + ".png", format="png", dpi=300)
    plt.show()


def getCommitsCategoriesRepo():
    mapCommitsMap = {}
    for commit in datasetRepositories[" #Commits"]:
        if mapCommitsMap.get(commit):
            mapCommitsMap[commit] = mapCommitsMap[commit] + 1
        else:
            mapCommitsMap[commit] = 1

    mapCommitsMap = collections.OrderedDict(sorted(mapCommitsMap.items()))

    categories = {}
    for map in mapCommitsMap:
        if map >= 0 and map <= 500:
            num = 0
            if categories.get("0-500"):
                num = categories["0-500"]
            categories["0-500"] = num + mapCommitsMap[map]
        elif map >= 501 and map <= 1000:
            num = 0
            if categories.get("501-1000"):
                num = categories["501-1000"]
            categories["501-1000"] = num + mapCommitsMap[map]
        elif map >= 1001 and map <= 2000:
            num = 0
            if categories.get("1001-2000"):
                num = categories["1001-2000"]
            categories["1001-2000"] = num + mapCommitsMap[map]
        elif map >= 2001 and map <= 3000:
            num = 0
            if categories.get("2001-3000"):
                num = categories["2001-3000"]
            categories["2001-3000"] = num + mapCommitsMap[map]

        elif map >= 3001 and map <= 4000:
            num = 0
            if categories.get("3001-4000"):
                num = categories["3001-4000"]
            categories["3001-4000"] = num + mapCommitsMap[map]
        elif map >= 4001 and map <= 5000:
            num = 0
            if categories.get("4001-5000"):
                num = categories["4001-5000"]
            categories["4001-5000"] = num + mapCommitsMap[map]
        elif map >= 5001 and map <= 8000:
            num = 0
            if categories.get("5001-8000"):
                num = categories["5001-8000"]
            categories["5001-8000"] = num + mapCommitsMap[map]
        elif map >= 8001 and map <= 11000:
            num = 0
            if categories.get("8001-11000"):
                num = categories["8001-11000"]
            categories["8001-11000"] = num + mapCommitsMap[map]
        elif map >= 11001 and map <= 14000:
            num = 0
            if categories.get("11001-14000"):
                num = categories["11001-14000"]
            categories["11001-14000"] = num + mapCommitsMap[map]
        elif map >= 14001 and map <= 17000:
            num = 0
            if categories.get("14001-17000"):
                num = categories["14001-17000"]
            categories["14001-17000"] = num + mapCommitsMap[map]
        elif map >= 17001 and map <= 20000:
            num = 0
            if categories.get("17001-20000"):
                num = categories["17001-20000"]
            categories["17001-20000"] = num + mapCommitsMap[map]
        elif map >= 20001:
            num = 0
            if categories.get("20001+"):
                num = categories["20001+"]
            categories["20001+"] = num + mapCommitsMap[map]


    return categories


def getContributorsCategories():
    mapCommitsMap = {}
    for commit in datasetRepositories[" #Contributors"]:
        if mapCommitsMap.get(commit):
            mapCommitsMap[commit] = mapCommitsMap[commit] + 1
        else:
            mapCommitsMap[commit] = 1

    mapCommitsMap = collections.OrderedDict(sorted(mapCommitsMap.items()))

    categories = {}
    for map in mapCommitsMap:
        if map >= 0 and map <= 50:
            num = 0
            if categories.get("0-50"):
                num = categories["0-50"]
            categories["0-50"] = num + mapCommitsMap[map]
        elif map >= 51 and map <= 100:
            num = 0
            if categories.get("51-100"):
                num = categories["51-100"]
            categories["51-100"] = num + mapCommitsMap[map]
        elif map >= 101 and map <= 150:
            num = 0
            if categories.get("101-150"):
                num = categories["101-150"]
            categories["101-150"] = num + mapCommitsMap[map]
        elif map >= 151 and map <= 200:
            num = 0
            if categories.get("151-200"):
                num = categories["151-200"]
            categories["151-200"] = num + mapCommitsMap[map]
        elif map >= 201 and map <= 250:
            num = 0
            if categories.get("201-250"):
                num = categories["201-250"]
            categories["201-250"] = num + mapCommitsMap[map]
        elif map >= 251 and map <= 300:
            num = 0
            if categories.get("251-300"):
                num = categories["251-300"]
            categories["251-300"] = num + mapCommitsMap[map]
        elif map >= 301 and map <= 350:
            num = 0
            if categories.get("301-350"):
                num = categories["301-350"]
            categories["301-350"] = num + mapCommitsMap[map]
        elif map >= 351 and map <= 400:
            num = 0
            if categories.get("351-400"):
                num = categories["351-400"]
            categories["351-400"] = num + mapCommitsMap[map]
        elif map >= 401 and map <= 450:
            num = 0
            if categories.get("401-450"):
                num = categories["401-450"]
            categories["401-450"] = num + mapCommitsMap[map]
        elif map >= 461 :
            num = 0
            if categories.get("461+"):
                num = categories["461+"]
            categories["461+"] = num + mapCommitsMap[map]

    return categories


def repositoriesCommits():
    print("commits")
    plt.figure(figsize=(12,10))

    categories = getCommitsCategoriesRepo()
    plt.bar(categories.keys(), categories.values(), width=1, edgecolor="white", linewidth=0.7)
    plt.xticks(rotation=45)
    plt.xlabel("Commits")
    plt.ylabel("Repositories")
    plt.savefig(path + "/RepositoriesCommit" + ".png", format="png", dpi=300)
    plt.show()


def repositoriesContributors():
    print("contributors")
    plt.figure(figsize=(12, 10))

    categories = getContributorsCategories()
    plt.bar(categories.keys(), categories.values(), width=1, edgecolor="white", linewidth=0.7)
    plt.xticks(rotation=45)
    plt.xlabel("Contributors")
    plt.ylabel("Repositories")
    plt.savefig(path + "/RepositoriesContributors" + ".png", format="png", dpi=300)
    plt.show()


def repositories():
    print(datasetRepositories.isnull().sum())
    print(datasetRepositories.describe())

    print("Repository languages")
    print(datasetRepositories[" #Languages"].describe())

    repositoriesCommits()
    repositoriesContributors()
    repositoriesHeatmap()
    repositoriesScatter()


def main():
    users()
    repositories()


if __name__ == "__main__":
    main()
