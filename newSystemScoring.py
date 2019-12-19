def recalc_ranking(oldRankingA, oldRankingB, scoreA, scoreB, gameType, gameMonth):

    if scoreA > scoreB:
        matchResultA = 1
        matchResultB = 0
    elif scoreB > scoreA:
        matchResultA = 0
        matchResultB = 1
    else:
        matchResultA = 0.5
        matchResultB = 0.5

    matchImportance = 0
    nationsMatches = ["Cup", "Games", "Copa", "Nations", "Tournament"]
    confederationMatches = ["Championship", "AFC", "CAF", "CONCACAF", "CONMEBOL", "OFC", "UEFA"]

    if "friendly" in gameType:
        if gameMonth in range(3,12):
            matchImportance = 10
        else:
            matchImportance = 5
    elif "qualification" in gameType:
        matchImportance = 25
    for nationString in nationsMatches:
        if nationString in gameType:
            matchImportance = 20
    for confederationString in confederationMatches:
        if confederationString in gameType:
            matchImportance = 37.5
    if matchImportance == 0:
        matchImportance = 15

    ratingDifferenceA = oldRankingA - oldRankingB
    expectedResultA = 1 / (10**(-1*ratingDifferenceA/400) + 1)
    ratingDifferenceB = oldRankingB - oldRankingA
    expectedResultB = 1 / (10**(-1*ratingDifferenceB/400) + 1)

    newRankingA = oldRankingA + matchImportance * (matchResultA - expectedResultA)
    newRankingB = oldRankingB + matchImportance * (matchResultB - expectedResultB)
    return newRankingA, newRankingB
