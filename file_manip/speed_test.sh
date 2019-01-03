#!/usr/bin/env bash
iters=$1
outfile=$2
func0='_remove_flag'
func1='remove_flag'
echo $(date) $func0 >> $outfile
python3 -m timeit -n $iters 'import file_manip' 'file_manip._remove_flag()' >> $outfile 
echo '' >> $outfile
rm ./test_logs/new_other_log.log
#
echo $(date) $func1 >> $outfile
python3 -m timeit -n $iters 'import file_manip' 'file_manip.remove_flag()' >> $outfile 
echo '' >> $outfile
rm ./test_logs/new_other_log.log
#
tail -n 15 $outfile
