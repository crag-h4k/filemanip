#!/usr/bin/env bash
iters=$1
outfile=$2
echo $(date) >> $outfile
python3 -m timeit -n $iters 'import file_manip' 'file_manip.find_files()' >> $outfile 
echo '' >> $outfile
tail -n 15 $outfile
