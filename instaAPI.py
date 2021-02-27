from InstagramAPI import InstagramAPI

'''

BY INSTAGRAM == @concepts.of.programming

                                        '''


userName = input("Enter your Username: ")
Pass = input("Enter your password: ")


def getTotalFollowers(api,
                      user_id):  # Returns the list of followers of the user. It should be equivalent of calling api.getTotalFollowers from InstagramAPI

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


def getTotal_followings(api, user_id):
    followers = []
    next_id = True
    while next_id:
        if next_id is True:
            next_id = ''

        _ = api.getUserFollowings(user_id, maxid=next_id)
        followers.extend(api.LastJson.get('users', []))
        next_id = api.LastJson.get('next_id', '')
    return followers


def nonFollowers(followers, followings):
    nonFollowers = {}
    dictFollowers = {}
    for follower in followers:
        dictFollowers[follower['username']] = follower['pk']

    for followedUser in followings:
        if followedUser['username'] not in dictFollowers:
            nonFollowers[followedUser['username']] = followedUser['pk']

    return nonFollowers


def unFollow(number: int):
    api = InstagramAPI(userName, Pass)
    api.login()
    user_id = api.username_id
    followers = getTotalFollowers(api, user_id)
    following = getTotal_followings(api, user_id)
    nonFollow = nonFollowers(followers, following)
    totalNonFollowers = len(nonFollow)
    print('Number of followers:', len(followers))
    print('Number of followings:', len(following))
    print('Number of nonFollowers:', len(nonFollow))


    # afterUnfollow = ["After unfollow who not following you: ", len(following) - len(user)]
    # print(afterUnfollow)

    for i in range(number):
        if i >= totalNonFollowers:
            break
        user = list(nonFollow.keys())[len(nonFollow) - 1]
        api.unfollow(nonFollow[user])
        nonFollow.pop(user)
        print(user)

if __name__ == "__main__":
    unFollow(2)

'''

BY INSTAGRAM == @concepts.of.programming

                                        '''




