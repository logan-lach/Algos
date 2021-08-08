class ESG:

    def __init__(self):
        self.values = {
            'C': 0,
            'CC': 1,
            'CCC': 2,
            'B': 3,
            'BB': 4,
            'BBB': 5,
            'A': 6,
            'AA': 7,
            'AAA': 8,
            'F': 9
        }
        self.graph = dict()

    def insert(self,line: str):
        issuer = line[0]
        parent = line[1]

        # If we've seen this issuer before
        if issuer not in self.graph.keys():

            # By default, lets assume our new issuer points at itself
            self.graph[issuer] = {
                'value': line[2],
                'children': dict()
            }

            # If the issuer doesn't point at itself, give it the value F and have it point at its child
            if line[1] != "":
                self.graph[issuer]['value'] = 'F'
                self.graph[issuer]['children'] = [line[1]]

        # If we've seen this parent before, give the minimum value to the parent
        if parent != "":
            if parent in self.graph.keys():
                self.graph[parent]['value'] = line[2]

            # If we haven't seen this parent before, add it to our graph and give it the value our issuer gave it
            else:
                self.graph[parent] = {
                    'value': line[2],
                    'children': []
                }
        else:
            self.graph[issuer]['value'] = line[2]
            self.graph[issuer]['children'] = []

    def answer_question(self):
        '''
        We are gonna solve this through Depth First search!

        As we go travese our graph, we will look frot the following things

        '''


        is_cyclical = False
        curr_max = "C"
        holder = None

        visited = set()

        def dfs(node):
            stack = [node]
            nonlocal is_cyclical
            nonlocal visited
            nonlocal curr_max
            nonlocal holder

            while len(stack) != 0:
                node = stack.pop()
                if node in visited:
                    is_cyclical = True
                    continue
                value, children = self.graph[node].values()
                if value != 'F':
                    if self.values[value] > self.values[curr_max]:
                        holder = node
                        curr_max = value

                for x in children:
                    stack.append(x)


        for i in self.graph.keys():
            if i not in visited:
                dfs(i)
        print('cyclic' if is_cyclical else 'noncyclic' + '\n' + curr_max + '\n' + holder)






t = ESG()

for x in [['A54365', 'B34454', 'CCC'],
['B34454', 'C34563', 'A'],
['D45747', 'B34454', 'B'],
['E36547', 'D45747', 'AAA'],
['G34657', 'D45747', 'CCC'],
['H84464', 'C34563', 'BB'],
['I76474', 'H84464', 'AA'],
['C34563', '', 'BBB'],
['F34654', '', 'BB'],
['J74576', 'K46565', 'C'],
['K46565', '', 'CC'],
['L54334', 'I76474', 'AA'],
['H84464', '', 'BB']]:
    t.insert(x)
t.answer_question()
