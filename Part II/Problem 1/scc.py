import gc

def construct_graph(source_file, reverse = False):
    with open(source_file, 'r') as file:
        data = file.readlines()
        file.close()
    
    graph = {}
    
    for line in data:
        numbers = line.rstrip().split(' ')
        tail = int(numbers[0])
        head = int(numbers[1])
        
        if tail not in graph:
            graph[tail] = [False]
        if head not in graph:
            graph[head] = [False]
        
        if reverse is False:
            graph[tail].append(head)
        else:
            graph[head].append(tail)
            
    return graph

def output_graph(output_file, graph):
    with open(output_file, 'w+') as file:
        for tail in graph:
            file.write('{}:'.format(tail))
            for head in graph[tail]:
                file.write(' {}'.format(head))
            file.write('\n')
        file.close()

def compute_topo_order(graph):
    topo_order = []
    order_list = []
    temp_order = []
    
    for node in graph:
        if graph[node][0] is False:
            temp_order = []
            stack = [node]
            graph[node][0] = True
            
            while len(stack) > 0:
                tail = stack.pop()
                
                for head in graph[tail][1:]:
                    if graph[head][0] is False:
                        graph[head][0] = True
                        stack.append(head)
                        
                temp_order.append(tail)
                
            order_list.append(temp_order)
        
    del temp_order
    gc.collect()
    
    for i in range(len(order_list) - 1, -1, -1):
        topo_order.extend(order_list[i])
    del order_list
      
    return topo_order

def output_topo_order(output_file, topo_order):
    with open(output_file, 'w+') as file:
        order = 0
        for node in topo_order:
            file.write('{}, {}\n'.format(order, node))
            order += 1
        file.close()

def compute_scc(graph, rev_topo_order):
    scc_sizes = []
    
    for node in rev_topo_order:        
        if graph[node][0] is False:
            stack = [node]
            graph[node][0] = True
            size = 0
            
            while len(stack) > 0:
                tail = stack.pop()
                size += 1
                
                for head in graph[tail][1:]:
                    if graph[head][0] is False:
                        graph[head][0] = True
                        stack.append(head)
        
            scc_sizes.append(size)
            
    return scc_sizes

def output_scc(output_file, scc_sizes):
    with open(output_file, 'w+') as file:
        for size in scc_sizes:
            file.write('{}\n'.format(size))
        file.close()
        
rev_graph = construct_graph('./scc_data.txt', reverse=True)
output_graph('./rev_graph.txt', rev_graph)
print('Reversed graph contructed')
    
rev_topo_order = compute_topo_order(rev_graph)
output_topo_order('./rev_topo_order.txt', rev_topo_order)
print('Topological order of the reversed graph computed')

del rev_graph
gc.collect()

graph = construct_graph('./scc_data.txt')
output_graph('./graph.txt', graph)
print('Graph constructed')

scc_sizes = compute_scc(graph, rev_topo_order)
output_scc('./scc_sizes.txt', scc_sizes)
print('SCC sizes computed')

scc_sizes.sort(reverse=True)
print(scc_sizes[:5])
print('---end---')


