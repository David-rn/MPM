states = None
tree = None

with open('tracking.states', 'r') as state_file:
    states = state_file.readlines()

with open('tracking.tree', 'r') as tree_file:
    tree = tree_file.readlines()

def add_to_statedict(cell_id, frame):
    keys = state_dic.keys()
    exist = cell_id in keys
    if not exist:
        state_dic[cell_id] = [frame]
    else:
        state_dic[cell_id].append(frame)

def add_to_treedict(cell_id, parent):
    keys = tree_dic.keys()
    exist = cell_id in keys
    if not exist:
        tree_dic[cell_id] = [parent]
    else:
        tree_dic[cell_id].append(parent)

state_dic = {}
tree_dic = {}

for state in states:
    items = state.split(' ')
    add_to_statedict(items[1], items[0])

for t in tree:
    items = t.split(' ')
    add_to_treedict(items[0], items[1])

lines = []
keys = list(state_dic.keys())
keys.sort(key=int)

for key in keys:
    cell_id = key
    values = state_dic[key]
    init_frame = values[0]
    end_frame = values[-1]
    parent = tree_dic[cell_id][0]
    line = cell_id + " " + init_frame + " " + end_frame + " " + parent
    lines.append(line)

with open('res_track.txt', 'w') as f:
    f.writelines(lines)