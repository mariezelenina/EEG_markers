import re
from collections import OrderedDict

# open data file
# todo: name should be given by user
inputFileName = raw_input("Please input name of data file. Example format: 2OTPH_19        ")

# create dict to put data into.
markers_dict = OrderedDict()

# open markers file
with open('data_markers/'+inputFileName+'.vmrk') as f:

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



# dictionary now looks like: markers_2OTPH_19: {marker decription: [all its position]}

#print markers_2OTPH_19
print inputFileName
for (k,v) in markers_dict.iteritems():
    print k, v


