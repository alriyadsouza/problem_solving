class Solution:
    @staticmethod
    def grid(rows,col):
        print(")")

n = int(input("Enter the number of rows: "))
col = 2
print("Enter values as space-separated numbers for each row:")

graph = []

for i in range(n):
    row = []
    values = input(f"Enter values for row {i+1} (space-separated): ").split()
    # Convert the values to integers and append to the row list
    for value in values:
        row.append(int(value))
    # Ensure the row has the expected number of columns
    if len(row) != col:
        print(f"Warning: Row {i+1} does not have {col} values. It will be filled with 0s.")
        row.extend([0] * (col - len(row)))
    # Append the row to the graph
    graph.append(row)

print(graph)

Solution.grid(n,col)