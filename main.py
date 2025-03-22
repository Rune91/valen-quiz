from create_html import create_table

class Team:
    def __init__(self, name, scores_list):
        """
        score: score from a given quiz
        points: total points for the season
        """
        self.name = name
        self.scores_list = scores_list
        self.points_list = []
        self.points_total = 0
    
    def __str__(self):
        return f"{self.points_total:2} {self.name}"
    
    def give_points(self, points):
        self.points_list.append(points)
        self.points_total = sum(self.points_list)


def assign_team_points(teams, quiz_num):
    sorted_teams = sorted(teams, key = lambda t: t.scores_list[quiz_num])
    i = 0
    while i < len(sorted_teams):
        team = sorted_teams[i]
        team_score = team.scores_list[quiz_num]        

        # is the team tied with any of the following teams?
        tied_search_index = i + 1
        tied_teams = [team]
        while (tied_search_index < len(teams)
               and sorted_teams[tied_search_index].scores_list[quiz_num] == team_score):
            tied_team = sorted_teams[tied_search_index]
            tied_teams.append(tied_team)
            tied_search_index += 1
        
        points = 0
        for t in range(len(tied_teams)):
            points += i + 1 + t
        points /= len(tied_teams)

        for team in tied_teams:
            team.give_points(points)
        i = tied_search_index


def read_data(filename):
    teams = []
    with open(filename, 'r', encoding='utf-8') as file:
        header_line = file.readline()
        dates = [d.strip() for d in header_line.split(',')[1:]]
        for line in file.readlines():
            data = line.split(',')
            team_name = data[0]
            team_scores = [float(p.strip()) for p in data[1:]]
            teams.append(Team(team_name, team_scores))
    return teams, dates

def main():
    teams, dates = read_data('resultater.csv')
    assign_team_points(teams, 0)
    teams.sort(key = lambda t: t.points_total, reverse=True)
    #[print(t) for t in teams]
    print(create_table(teams, dates))

if __name__ == '__main__':
    main()