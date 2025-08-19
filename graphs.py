adjacency_matrix = []
while True:
    try:
        line = input().strip()
        if not line:  # Empty line indicates end
            break
        row = list(map(int, line.split()))
        adjacency_matrix.append(row)
    except EOFError:
        break