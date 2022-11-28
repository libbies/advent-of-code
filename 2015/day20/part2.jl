function main()
    input = parse(Int64, String(read("input.txt")))

    presents = [0 for n in 1:div(input, 11)]

    total = 0
    for elf in 1:div(input, 11)
        for n in 1:50
            if n.*elf >= div(input, 11)
                break
            end
            presents[n*elf] += elf * 11
        end
    end

    println("len: ", length(presents), ", max: ", maximum(presents))

    for (i, n) in enumerate(presents)
        if n >= input
            println(n, ">=", input, " part2: ", i, " chk:", presents[1053360])
            break
        end
    end
end

main()
