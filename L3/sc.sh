possible=( "sse4.2" "sse4.1" "sse3" "sse2" "ssse" "avx")
for p in "${possible[@]}"; do
    for O in {1..3}; do
        icpc -O$O -m$p cs.cpp -o Temp
        echo
        echo $p " " $O
        time `./Temp`
    done
done
