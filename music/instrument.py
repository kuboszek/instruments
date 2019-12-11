class Instrument:
    def __init__(self, name):
        self.name = name
        self.exercises = []
        self.octaves = []

    def print(self):
        print('Instrument: ' + self.name)
        for ex in self.exercises:
            ex.print()

    def addExercise(self, ex):
        self.exercises.append(ex)

    def addOctave(self, octave):
        self.exercises.append(octave)