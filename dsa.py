def largest_rectangle(heights):
    max_area = 0
    stack = [-1]
    heights.append(0)


    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1

            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop()
    return max_area


def max_rectangle(matrix):
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                heights[j] += 1 
            else:
                heights[j] = 0

        max_area = max(max_area, largest_rectangle(heights))

    return max_area


matrix = [ 

  ["1","0","1","0","0"], 

  ["1","0","1","1","1"], 

  ["1","1","1","1","1"], 

  ["1","0","0","1","0"] 

]

print(max_rectangle(matrix))