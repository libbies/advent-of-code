using LRUCache

const lru = LRU{Int64, Int64}(maxsize=1)
lru[0] = 1
function recurse(iterations)
    get!(lru, iterations) do
        return 7 * recurse(iterations - 1) % 20201227
    end
end

function transform(sn, iterations)
    result = 1
    for n in 1:iterations
        result = sn * result % 20201227
    end
    return result
end

card_pub_key, door_pub_key = map(v -> parse(Int, v), readlines("input.txt"))
key = 1
for loop in 1:door_pub_key
    # key = recurse(loop)
    global key = 7 * key % 20201227
    if key == card_pub_key
        println("card loop: ", loop)
        println("part1: ", transform(door_pub_key, loop))
        break
    elseif key == door_pub_key
        println("door loop: ", loop)
        println("part1: ", transform(card_pub_key, loop))
        break
    end
end
