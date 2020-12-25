using LRUCache

const lru = LRU{Int64, Int64}(maxsize=1)
lru[0] = 1
function recurse(iterations)
    get!(lru, iterations) do
        return 7 * recurse(iterations - 1) % 20201227
    end
end

function main()
    card_pub_key, door_pub_key = map(v -> parse(Int, v), readlines("input.txt"))
    key = 1
    for loop in 1:door_pub_key
        # key = powermod(7, loop, 20201227)
        # key = recurse(loop)
        key = 7 * key % 20201227
        if key == card_pub_key
            println("card loop: ", loop)
            println("part1: ", powermod(card_pub_key, loop, 20201227))
            break
        elseif key == door_pub_key
            println("door loop: ", loop)
            println("part1: ", powermod(card_pub_key, loop, 20201227))
            break
        end
    end
end

main()
