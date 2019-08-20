# An algorithm for counting the number of triangles that can be constructed from a list of edge lengths.
def count_triangles(lengths):
    lengths.sort()
    count = 0
    # Use he middle-length edge as a pivot
    for mid in range(len(lengths)):
        small = 0
        long = mid + 1
        if small == mid or long == len(lengths):
            continue
        grid = [[0] * (len(lengths) - mid - 1) for i in range(mid - small)]
        subcount = 0
        # Find the first small edge that can be used to make a triangle with the smallest long edge.
        while small < mid and (lengths[small] + lengths[mid]) <= lengths[long]:
            small = small + 1
        # Iterate over remaining small edges
        while small < mid:
            # Find the longest long edge that can be used to make a triangle with current small and mid-length edges
            while (long + 1) < len(lengths) and (lengths[small] + lengths[mid]) > lengths[long + 1]:
                long = long + 1
            # Mark the (small, long) pair in our output grid
            grid[small][(long - mid - 1)] = long - mid
            # We can make a triangle out of our current small edge, middle edge, and all long edges up to the longest long edge.
            subcount = subcount + long - mid
            small = small + 1
        
        # Display output
        print('(' + '{:>2}'.format(str(lengths[mid])) + ') ' + ' '.join('{:>3}'.format(str(elem)) for elem in lengths[mid+1:]))
        for i in range(len(grid)):
            print('{:>3}'.format(str(lengths[i])) + ': ' + ' '.join('{:>3}'.format(str(elem)) for elem in grid[i]))
        print('count: ' + str(subcount))
        print('---' * (len(lengths) + 1))
        count = count + subcount
    return count

count = count_triangles([2, 5, 7, 8, 10, 11, 14, 16])
print("final count: " + str(count))