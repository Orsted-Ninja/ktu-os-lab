
domain_colors = ['Red', 'Blue', 'Green']


variable_states = ['wa', 'nt', 'sa', 'q', 'nsw', 'v', 't']


neighbors = {}
neighbors['wa'] = ['nt', 'sa']
neighbors['nt'] = ['wa', 'sa', 'q']
neighbors['sa'] = ['wa', 'nt', 'q', 'nsw', 'v']
neighbors['q'] = ['nt', 'sa', 'nsw']
neighbors['nsw'] = ['q', 'sa', 'v']
neighbors['v'] = ['sa', 'nsw']
neighbors['t'] = []


finalstateswithcolor = {}

def getthecolor(state):
    
    for color in domain_colors:
        if assigncolor(state, color):
            return color

def assigncolor(state, color):
    
    for neighbor in neighbors.get(state, []):
        color_of_neighbor = finalstateswithcolor.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def main():
   
    
    sorted_states = sorted(neighbors.keys(), key=lambda state: len(neighbors[state]), reverse=True)
    
    
    for state in sorted_states:
        finalstateswithcolor[state] = getthecolor(state)
        
    print("The states with colors are:", finalstateswithcolor)


main()




