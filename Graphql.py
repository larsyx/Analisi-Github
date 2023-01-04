import requests

class graphQL:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}
        super(graphQL, self).__init__()
    def run_query1(self, query):  # A simple function to use requests.post to make the API call. Note the json= section.
        request = requests.post('https://api.github.com/graphql', json={'query': query},headers=self.headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

    def run_query(self, query, variables):  # A simple function to use requests.post to make the API call. Note the json= section.
        request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables}, headers=self.headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


    def getClosedIssuesActors(self):
        listOfNames = []
        query = '''
                query($owner: String!, $name: String!) { 
				repository(owner: $owner, name: $name){
				  issues(states: CLOSED, first:10){
					edges{
					  node{
						... on Issue{
						  timeline(last: 100){
							edges{
							  node{
								__typename
								... on ClosedEvent{
								  actor{
									login
								  }
								}
							  }
							}
						  }
						}
					  }
					}
				  }
				}
			}'''

        variables = {
            "owner": "larsyx",
            "name": "Forza_4"
        }

        result = self.run_query(query, variables)  # execute query
        print(result)

    def getTotalNumberOfUser(self):
        query = '''
          query{
              user: search(type: USER, query: \"type:User\"){
                userCount
            }  
         }'''
        resultUser = self.run_query1(query)  # execute query
        print("Total number of Users:", resultUser["data"]["user"]["userCount"])
        query2 = '''
          query{
              org: search(type: USER, query: \"type:org\") {
                userCount
              }
         }'''
        resultOrg = self.run_query1(query2)  # execute query
        print("Total number of Organizzazion:", resultOrg["data"]["org"]["userCount"])

    def getTotalRepositoryByLanguage(self,language):
        query = '''
            query{
                search(type: REPOSITORY, query: \"language:'''+ language + '''\") {
                repositoryCount
              }
            }'''

        result = self.run_query1(query)  # execute query
        print("Repository in ",language, ":",result["data"]["search"]["repositoryCount"])

    def getUserByCountry(self,country):
        query = '''
          query($country: String!){
              user: search(type: USER, query: $country){
                userCount
            }  
          }'''

        variables = {
            "country": "location:" + country
        }

        result = self.run_query(query, variables)
        print("Total user in",country + ":",result["data"]["user"]["userCount"])

