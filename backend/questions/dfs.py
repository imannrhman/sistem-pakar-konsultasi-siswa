import collections

graph = {
  '' : ['Q18','Q7', 'Q8', 'Q10'],
  'Q1': ['B1'],
  'Q2': ['Q1', 'B1'],
  'Q3': ['Q2', 'Q17', 'Q19'],
  'Q4': ['B2'],
  'Q5': ['B2'],
  'Q6': ['B2'],
  'Q7': ['Q4','Q5','Q6','Q15'],
  'Q8': ['Q15','Q7'],
  'Q9': ['B3'],
  'Q10': ['B4'],
  'Q11': ['B4'],
  'Q12': ['B4'],
  'Q13': ['B4'],
  'Q14': ['B5'],
  'Q15': ['Q14', 'Q16', 'Q9'],
  'Q16': ['B5'],
  'Q17': ['B6'],
  'Q18': ['Q3'],
  'Q19': ['B6'],
  'Q20': ['B7'],
  'Q21': ['B7'],
  'Q22': ['B7'],
  'Q23': ['B7'],
  'B1': [],
  'B2': [],
  'B3': [],
  'B4': [],
  'B5': [],
  'B6': [],
  'B7': [],
}


def dfs(code,codes):   
          node = graph[code]
          if len(node) == 1:
               return node[0]
          else:
               for c in codes:
                  if c in node:
                        dfs(c,codes)
                






def calculate_dfs(codes):
        data = []
        realResult = []
        for x in codes:
                temp = dfs(x,codes)
                if temp:
                        data.append(temp) 
        print(data)
        frequency = collections.Counter(data)
        for b in dict(frequency):
                if dict(frequency)[b] >= 3 :
                        realResult.append(b) 
        return realResult 