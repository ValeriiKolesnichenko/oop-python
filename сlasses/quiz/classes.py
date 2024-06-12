class Participant:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self):
        self.score += 10
        print(f'{self.name} has {self.score}/100 points')

    def delete_points(self):
        if self.score == 0:
            print(f'{self.name} has {self.score}/100 points')
        else:
            self.score -= 5
            print(f'{self.name} has {self.score}/100 points')


