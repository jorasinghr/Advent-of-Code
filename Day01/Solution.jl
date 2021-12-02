#=
Solution:
- Julia version: 1.7.0
- Author: Jora Singh Randhawa
- Date: 2021-12-01
=#

input = open("Day01/input.txt", "r")
depths = parse.(Int, readlines(input))

# Task 1
function looping(depth)
    count = 0
    for (ind, val) in enumerate(depths)
        if ind != 1
            if val > depths[ind-1]
                count += 1
            end
        end
    end
    println("Task 1: ", count)
end
looping(depths)


# Task 2
function looping(depth)
    count = 0
    for (ind, val) in enumerate(depths)
        if ind < (size(depths, 1) - 2)
            A = val + depths[ind + 1] + depths[ind + 2]
            B = depths[ind + 1] + depths[ind + 2] + depths[ind + 3]
            if B > A
                count += 1
            end
        end
    end
    println("Task 2: ", count)
end
looping(depths)

