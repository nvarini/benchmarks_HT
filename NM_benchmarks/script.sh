#!/bin/bash
hpcfile=hpc.json
hpcfile_sirius=hpc-sirius.json
pwfile=pw.json
dirname=$(awk 'NR==2 {print $3}' ${hpcfile}| grep -o '".*"'| sed 's/"//g')
scale=$(grep scale ${hpcfile} |awk '{print $3}')
a=$(verdi run submit_benchmarks.py qe-6.2@bellatrix  ${hpcfile} ${pwfile})
b=$(verdi run submit_benchmarks.py qe-6.2@deneb_ivy  ${hpcfile} ${pwfile})
c=$(verdi run submit_benchmarks.py qe-6.2@fidis  ${hpcfile} ${pwfile})
d=$(verdi run submit_benchmarks.py qe-6.1-gpu@PizDaintGPU ${hpcfile} ${pwfile})
e=$(verdi run submit_benchmarks.py qe-6.2-sirius@PizDaintGPU ${hpcfile_sirius} ${pwfile})
f=$(date +%F-%k-%m-%S)
echo $a $b $c $d $e  > workflow_list
mkdir -p ${scale}
mv workflow_list ${scale}

