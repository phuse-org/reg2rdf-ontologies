# get the all parts' sectno and paragraphs
# input: 21 CFR XML files
# output: csv files contain the section No., section title, and section content .

from xml.etree.cElementTree import ElementTree
import re

for i in range(1,10):
    file = "/home/yu.lin/21CFR/title-21/CFR-2015-title21-vol"+str(i)+".xml"
    tree = ElementTree()
    tree.parse(file)
    root = tree.getroot()
    root.findall(".")

    t = 0
    for SECTION in root.iter('SECTION'):
        if SECTION.findall('./*') is not None:
            t = t+1
            section_list = SECTION.findall('./*')
            filename = "/home/yu.lin/21CFR/output/section/vol"+str(i)+"_"+str(t)+".csv"
            updateFile = open(filename,'w')
            for section in section_list:
                section_list = section.itertext() # in a section_list, one block is 
                sect_content = []
                for sect in section_list:        # each small element inside SECTION as a sect.     
                    sect = sect.encode('utf-8').strip()
                    if len(sect) > 1:
                        sect = "\""+sect+"\","
                        sect_content.append(sect)
                sect_1 = '|'.join(sect_content).strip()
                updateFile.write(sect_1)
            updateFile.close()
