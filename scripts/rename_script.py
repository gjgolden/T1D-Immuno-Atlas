print ("Starting renaming program")

#import required module
import os
import re
import shutil

#set directory
directory = os.path.dirname(os.path.realpath(__file__))
#print(directory)

#set cell populations regex list
cellpops = ["CD3\\-CD19\\-", "CD4\\+", "CD8\\+", "CD45\\+", "PBMCs_B cells"]

#list cell population names, in order as above
cellpopsname = ["innate", "CD4", "CD8", "CD45", "B"]

#set up file names to sort into
sortingfiles = ["a-Innate", "a-CD4", "a-CD8", "a-CD45", "a-B-cell"]

#iterate over files in that directory

for filename in os.listdir(directory):
    x = os.path.join(directory, filename)
    print(x)
    
    if os.path.isfile(x):
        ref = -1

        for pattern in cellpops:
            ref = ref + 1
            #print(name)
            regexp = re.compile(pattern)

            if regexp.search(filename):
                #rename cell type
                new_filename = re.sub(pattern, cellpopsname[ref], str(filename))
                os.rename(filename, new_filename)

                #rename HPAP donor ID
                donorID = re.search("HPAP\\-*\d\d\d.*", new_filename)
                new_filename2 = donorID.group() #extracts string from the match
                os.rename(new_filename, new_filename2)

                #move the file to the appropriate folder
                shutil.move(new_filename2, os.path.join(directory, sortingfiles[ref]))

            else:
                continue

    else:
        continue
print("Done!")