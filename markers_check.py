import re
from collections import OrderedDict


def create_marker_dict(InputFileName):
    # create dict to put data into.
    markers_dict = OrderedDict()

    # open markers file
    with open('data_markers/'+InputFileName+'.vmrk') as f:

        for line in f:
            line_list = re.split('=|,', line)
            if line_list[0][:2] == 'Mk' and line_list[1] == 'Stimulus':
                mk_description = line_list[2]
                mk_position = int(line_list[3])
                mk_id = line_list[0]
                if mk_description not in markers_dict.keys():
                    markers_dict[mk_description]=[(mk_id,mk_position)]
                else:
                    old = markers_dict[mk_description]
                    old.append((mk_id,mk_position))
                    markers_dict[mk_description] = old

    return markers_dict

# write results in file
def write_into_file(created_dict, InputFileName, OutputFileName='markersfile.txt'):
    outputFile = open(OutputFileName, 'a')
    outputFile.write('\n\n\n'+InputFileName+'\n\n')
    for (k,v) in created_dict.iteritems():
        outputFile.write(str(k)+str(v)+'\n')
    outputFile.close()
#------------------------------------------------------------------------------------------------

# open data file
#inputFileName = raw_input("Please input name of data file. Example format: 2OTPH_19        ")

# todo iterate through files
# because of name inconsistency with participant 02, we will write data manually prom participants 01 and 02

inputFileName = 'OTPH_01'
created_dict = create_marker_dict(inputFileName)
write_into_file(created_dict, inputFileName)

inputFileName = '2OTPH_01'
created_dict = create_marker_dict(inputFileName)
write_into_file(created_dict, inputFileName)

inputFileName = '2OTPH_02'
created_dict = create_marker_dict(inputFileName)
write_into_file(created_dict, inputFileName)

inputFileName = '3OTPH_02'
created_dict = create_marker_dict(inputFileName)
write_into_file(created_dict, inputFileName)

# now iterate through filenames
for participant_id in ['03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20']:
    # 1st trial
    inputFileName = 'OTPH_'+participant_id
    created_dict = create_marker_dict(inputFileName)
    write_into_file(created_dict, inputFileName)
    #2nd trial
    inputFileName = '2OTPH_'+participant_id
    created_dict = create_marker_dict(inputFileName)
    write_into_file(created_dict, inputFileName)