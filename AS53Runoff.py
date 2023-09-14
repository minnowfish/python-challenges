from collections import defaultdict

def runoff(candidates, ballots):
    while True:
        vote_counts = defaultdict(int)

        for ballot in ballots:
            for candidate in ballot:
                print("y")
                if candidate in candidates:
                    vote_counts[candidate] += 1
                    break 

        for candidate, votes in vote_counts.items():
            if votes > len(ballots) // 2:
                return candidate  
    
        min_votes = min(vote_counts.values())
        for candidate in list(vote_counts.keys()):
            if vote_counts[candidate] == min_votes:
                candidates.remove(candidate)

        if len(candidates) == 0:
            return "No winner"

candidates = ["Alice", "Bob", "Charlie"]
ballots = [["Alice", "Bob", "Charlie"], ["Alice", "Charlie", "Bob"], ["Bob", "Charlie", "Alice"], ["Bob", "Alice", "Charlie"], ["Charlie", "Alice", "Bob"]]
winner = runoff(candidates, ballots)
print("Winner:", winner)
