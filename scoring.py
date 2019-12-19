def recalc_score(oldRankingA, oldRankingB, scoreA, scoreB, gameType, gameMonth):

    if scoreA > scoreB:
        matchResultA = 1
        matchResultB = 0
    elif scoreB > scoreA:
        matchResultA = 0
        matchResultB = 1
    else:
        matchResultA = 0.5
        matchResultB = 0.5

    matchImportance = #Look at gameType, determine the imporatnce factor,
    # factor in gameMonth for within league windows 

    ratingDifference = oldScoreA - oldscoreB
    expectedResult = 1 / (10*(ratingDifference/600) + 1))

    newRankingA = oldScoreA + matchImportance * (matchResultA - expectedResult)
    newRankingB = oldScoreB + matchImportance * (matchResultB – expectedResult)

    return newRankingA, newRankingB
