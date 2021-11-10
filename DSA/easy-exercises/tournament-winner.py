def tournamentWinner(competitions, results):
    """
    For each competition add in the dictionary the winner with their score.
    After add all the winners, return the name who have the max score on the dictionary.
    Time: O(n), wheren is the number of competitions
    Space: O(k), where  k is the number of winner teams
    """
    scores = {}
    home_team = 1
    away_team = 0
    for competition in range(len(competitions)):
        if results[competition] == 0:
            # Increasing the value of the dictionary in 3 if home_team is the winner
            scores[competitions[competition][home_team]] = scores.get(competitions[competition][home_team], 0) + 3
        else:
            # Increasing the value of the dictionary in 3 if away_team is the winner
            scores[competitions[competition][away_team]] = scores.get(competitions[competition][away_team], 0) + 3
        
    return max(scores, key=scores.get)


competitions = [["Java", "C"],["C", 'Python'],["Java", "Python"]]
results = [0, 1, 1 ]


print(tournamentWinner(competitions, results))