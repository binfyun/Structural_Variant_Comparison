#!/usr/bin/env python

from os import system
import gzip
import glob
import pickle
from sys import argv

database = glob.glob('/data/dbVar/Homo_Sapiens/by_study/*/tab/*variant_call.*.germline.tab.gz')

def read_file(file1,save):
    file1 = gzip.open(file1)
    for Line in file1:
        if Line[0]!='#':
            col = Line.split('\t')
            if col[6]=='GRCh38':
                save.write('\t'.join([col[0],col[2],col[7],col[9],col[10],col[11],col[12],col[13],col[14],col[45],col[8]])+'\n')

def main():
    system('mkdir merge_data')
    
    all_study_id = []
    for name in database:
        name = name.split('/')[-1].split('_')[0]
        if name not in all_study_id:
            all_study_id.append(name)

    for study_id in all_study_id:
        print 'reading study',study_id
        output_file = 'merge_data/'+study_id+'.txt'
        save = open(output_file,'w')
        save.write('#accession_num\tvar_type\tchr\touter_start\tstart\tinner_start\tinner_stop\tstop\touter_stop\tremap_alignment\tcontig\n')
        file_in_study = glob.glob('/data/dbVar/Homo_Sapiens/by_study/'+study_id+'*/tab/*variant_call.*.germline.tab.gz')
        for file1 in file_in_study:
            read_file(file1,save)
        save.close()

main()
