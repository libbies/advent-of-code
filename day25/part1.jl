using LRUCache

const lru = LRU{Int64, Int64}(maxsize=1)
function recurse(iterations::Int64)
    get!(lru, iterations) do
        uncached_recurse(iterations)
    end
end

function uncached_recurse(iterations::Int64)
    return 7 * recurse(iterations - 1) % 20201227
end

function transform(sn::Int64, iterations::Int64)
    result = 1
    for n in 1:iterations
        result = sn * result % 20201227
    end
    return result
end

card_pub_key, door_pub_key = map(v -> parse(Int, v), readlines("input.txt"))

loop = 1
setindex!(lru, 7, 1)
while true
    global loop
    key = recurse(loop)
    if key == card_pub_key
        println("card loop: ", loop)
        println("part1: ", transform(door_pub_key, loop))
        break
    end
    if key == door_pub_key
        println("door loop: ", loop)
        println("part1: ", transform(card_pub_key, loop))
        break
    end
    loop += 1
end
