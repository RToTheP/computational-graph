def find_head_node(edges, nodes) -> int:
    """Loop over the edges and find the node that has no outward edges"""
    candidates = {n for n in nodes}
    for a,_ in edges:
        if a in candidates:
            candidates.discard(a)

    if len(candidates) == 0:
        raise Exception("No head node")

    if len(candidates) > 1:
        raise Exception("Multiple head nodes")

    return list(candidates)[0]


def multiply(values):
    result = 1
    for v in values:
        result *= v
    return result

def divide(values):
    result = values[0]
    for v in values[1:]:
        result /= v
    return result


def add(values):
    return sum(values)

def subtract(values):
    result = values[0]
    for v in values[1:]:
        result -= v
    return result


def evaluate_node(edges, nodes, node, inputs=None):
    # find the edges and nodes incident to the target node
    # sort these to node id order to work out handed-ness of the incident edges
    incident_nodes = sorted(a for a,b in edges if b == node)

    # find out what this node does, i.e. is it a constant, variable, or operator
    n = nodes[node]
    # firstly, check if the node is a variable and, if so, substitute the value
    if inputs is not None and n in inputs:
        n = inputs[n]

    # if there aren't any incident edges then it can't be an operator
    if len(incident_nodes) == 0:
        return n

    evaluated_nodes = [evaluate_node(edges, nodes, n, inputs) for n in incident_nodes]

    # then check if the node is an operator
    result = None
    if n == "*":
        result = multiply(evaluated_nodes)
    elif n == "/":
        result = divide(evaluated_nodes)
    elif n == "+":
        result = add(evaluated_nodes)
    elif n == "-":
        result = subtract(evaluated_nodes)
    else:
        result = n
    
    return result


def evaluate_graph(edges, nodes, inputs=None):
    """Evaluate graph by stepping through and applying operators"""
    head = find_head_node(edges, nodes)

    # Start from the head node and build a dictionary of incident nodes
    result = evaluate_node(edges, nodes, node=head, inputs=inputs)

    return result

def write_dot_file(path: str, edges, nodes):
    with open(path, 'w') as f:
        f.write("digraph G {\n")
        # write nodes
        for k,v in nodes.items():
            f.write(f"node_{k} [label=\"{v}\"]\n")

        f.write("\n")
        # write edges
        for t in edges:
            f.write(f"node_{t[0]}->node_{t[1]}\n")

        f.write("}\n")

