function crt(n::Array, a::Array)
    p = prod(n)
    mod(sum(ai * invmod(p ÷ ni, ni) * (p ÷ ni) for (ni, ai) in zip(n, a)), p)
end

function main()
    input = [
        tryparse(Int, i)!=nothing ? parse(Int, i) : nothing
        for i in split(readlines("input.txt")[end], ",")
    ]

    buses = Dict{Int, Int}()
    for (offset, bus) in enumerate(input)
        if bus != nothing
            buses[bus] = offset-1 # julia is not zero-indexed :D
        end
    end

    println("part2: ", prod(keys(buses))
        - crt(collect(keys(buses)), collect(values(buses))))
end

main()
