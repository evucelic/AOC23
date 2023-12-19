input_path = "input.txt"

def process_input(filename):
    with open(filename) as file:
        input = file.read().splitlines()

    workflows = {}
    parts = []

    for line in input:
        if len(line) == 0: continue

        # parts
        if line[0] == '{':
            part = line
            for cat in 'xmas':
                part = part.replace(cat+"=", "'"+cat+"':")
            exec('parts.append('+part+')')
            continue

        # workflows
        line = line.replace('}','')
        token = line.split('{')
        workflow_name = token[0]
        workflow_rules = []
        rules = token[1].split(',')
        for rule in rules[:-1]:
            token = rule.split(':')
            next_workflow = token[1]
            attrib = token[0][0]
            op = token[0][1]
            rating = int(token[0][2:])
            workflow_rules.append((attrib,op,rating,next_workflow))
        workflow_rules.append(('L','=',-1,rules[-1]))
        workflows[workflow_name] = workflow_rules

    return workflows, parts

workflows, ratings = process_input(input_path)
 
def eval(part):
    state = "in" # starting state
    while True:
        statement = workflows[state]
        for d in statement:
            valid = True
            new = d[3]
            var = d[0]
            op = d[1]
            num = d[2]
            if op == ">":
                valid = part[var] > num
            if op == "<":
                valid = part[var] < num
            if valid:
                if new == "A":
                    return True
                if new == "R":
                    return False
                state = new
                break

    
ans = 0
for rating in ratings:
    if eval(rating):
        ans += rating["x"] + rating["m"] + rating["a"] + rating["s"]

print(ans)