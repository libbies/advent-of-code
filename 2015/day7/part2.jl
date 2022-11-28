using DataStructures

function run(wires, queue)
    while !isempty(queue)
        l = popfirst!(queue)
        v = split(l[1])

        if v[1] == "NOT"
            # pass
        elseif haskey(wires, v[1])
            v1 = wires[v[1]]
        elseif tryparse(UInt16, v[1]) isa Number
            v1 = parse(UInt16, v[1])
        else
            push!(queue, l)
            continue
        end

        if haskey(wires, v[end])
            vend = wires[v[end]]
        elseif tryparse(UInt16, v[end]) isa Number
            vend = parse(UInt16, v[end])
        else
            push!(queue, l)
            continue
        end

        if length(v) == 1
            wires[l[end]] = vend
        elseif v[1] == "NOT"
            wires[l[end]] = ~vend
        elseif v[2] == "AND"
            wires[l[end]] = v1 & vend
        elseif v[2] == "OR"
            wires[l[end]] = v1 | vend
        elseif v[2] == "LSHIFT"
            wires[l[end]] = v1 << vend
        elseif v[2] == "RSHIFT"
            wires[l[end]] = v1 >> vend
        end
    end
end

function main()
    wires = Dict{String, Int}()
    queue = map(v -> rsplit(v, limit=3), readlines("input.txt"))
    run(wires, queue)
    println("part1: ", wires["a"])

    wires, wires["b"] = Dict{String, Int}(), wires["a"]
    queue = map(v -> rsplit(v, limit=3), readlines("input.txt"))
    run(wires, [q for q in queue if q[end] != "b"])
    println("part2: ", wires["a"])
end

main()
