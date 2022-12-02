import pandas as pd

def to_dataframe(graph: dict):
    n = len(graph)
    d = {i: [0]*n for i in range(n)}
    for node in graph:
        for x in graph[node]:
            d[int(node)][int(x)] = graph[node][x]
        for i in range(n):
            if not d[int(node)][i]:
                d[int(node)][i] = ''
    return pd.DataFrame(d).transpose()


def save_to_file(list_graphs: list, file_name: str):
    with pd.ExcelWriter(file_name) as writer:
        # worksheet = writer.sheets['graphs']
        row = 1
        while list_graphs:
            current_graph = list_graphs.pop(0)
            current_graph.to_excel(writer, sheet_name='graphs', startrow=row, startcol=1)
            # for i in range(len(current_graph)):
                # writer.sheets['graphs'].set_row_pixels(row+i, 25)
            row += len(current_graph.index) + 3
        # worksheet.set_column(0, 20, 3)
