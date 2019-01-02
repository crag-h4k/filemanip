iters=1000
outfile='./speed_results.txt'
echo 'os.walk ' >> $outfile
python -m timeit -n $iters 'from file_manip import find_files' 'find_files()'
echo 'system find ' >> $outfile
python -m timeit -n $iters 'from file_manip import _find_files' '_find_files()'
