class PathFinder:

    def readInput(self, path):
        lines = []

        with open(path) as file:
            for line in file:
                line = line.replace(".", "0").replace("#", "1").replace("\n","")
                lines.append(line)

        return lines

    def countTrees(self, input):
        counter = 0;
        index = 0;

        for line in input:
            counter += int(line[index]);
            index = (index + 3) % len(line)

        return counter;

if __name__ == '__main__':
    pathFinder = PathFinder()
    print(pathFinder.countTrees(pathFinder.readInput("../../input/day3")))