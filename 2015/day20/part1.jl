function main()
    input = div(parse(Int64, String(read("input.txt"))), 10)

    presents = [0 for n in 1:input]

    for elf in 1:input
        for n in 1:input÷elf
            presents[n*elf] += elf
        end
    end

    println("len: ", length(presents), ", max: ", maximum(presents))

    for (i, n) in enumerate(presents)
        if n >= input
            println(n, ">=", input, " part1: ", i)
            break
        end
    end
end

main()
