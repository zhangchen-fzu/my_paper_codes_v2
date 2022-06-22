##将所有的人名的“.”都紧挨上
# import os
# import re
# subdirs = os.walk(r'D:\my paper xiugai\es背景语料库\3es处理序号')
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\es背景语料库\4es人名圈小a的处理\人名\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         eachline=eachline.strip()
#                         if re.search("Sr. ",eachline)!=None and re.search("Sra. ",eachline)==None :
#                             eachline= re.sub("Sr. ", 'Sr.', eachline)
#                             f2.write(eachline+'\n')
#                         else:
#                             if re.search("Sr. ",eachline)==None and re.search("Sra. ",eachline)!=None:
#                                 eachline = re.sub("Sra. ", 'Sra.', eachline)
#                                 f2.write(eachline+'\n')
#                             else:
#                                 if re.search("Sr. ",eachline)!=None and re.search("Sra. ",eachline)!=None:
#                                     eachline = re.sub("Sra. ", 'Sra.', eachline)
#                                     eachline = re.sub("Sr. ", 'Sr.', eachline)
#                                     f2.write(eachline + '\n')
#                                 else:
#                                     if re.search("Sr. ",eachline)==None and re.search("Sra. ",eachline)==None:
#                                         eachline=eachline
#                                         f2.write(eachline+'\n')

##将所有的圈都分开所有的小a都分开
# import os
# import re
# subdirs = os.walk(r'D:\my paper xiugai\es背景语料库\4es人名圈小a的处理\人名')
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\es背景语料库\4es人名圈小a的处理\圈小a\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         eachline=eachline.strip()
#                         if re.search("º", eachline) != None and re.search("ª", eachline) == None:
#                             eachline = re.sub("º", ' º', eachline)
#                             f2.write(eachline + '\n')
#                         else:
#                             if re.search("º", eachline) == None and re.search("ª", eachline) != None:
#                                 eachline = re.sub("ª", ' ª', eachline)
#                                 f2.write(eachline + '\n')
#                             else:
#                                 if re.search("º", eachline) == None and re.search("ª", eachline) == None:
#                                     eachline=eachline
#                                     f2.write(eachline + '\n')
#                                 else:
#                                     if re.search("º", eachline) != None and re.search("ª", eachline) != None:
#                                         eachline = re.sub("º", ' º', eachline)
#                                         eachline = re.sub("ª", ' ª', eachline)
#                                         f2.write(eachline + '\n')

##处理中文的人名，将“.”紧挨上
# import os
# import re
# subdirs = os.walk(r'D:\my paper xiugai\2es处理序号zh处理联合国\zh')
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\3es人名圈小a的处理\zh\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         eachline=eachline.strip()
#                         if re.search("Ms. ",eachline)!=None and re.search("Mr. ",eachline)==None :
#                             eachline= re.sub("Ms. ", 'Ms.', eachline)
#                             f2.write(eachline+'\n')
#                         else:
#                             if re.search("Ms. ",eachline)==None and re.search("Mr. ",eachline)!=None:
#                                 eachline = re.sub("Mr. ", 'Mr.', eachline)
#                                 f2.write(eachline+'\n')
#                             else:
#                                 if re.search("Ms. ",eachline)!=None and re.search("Mr. ",eachline)!=None:
#                                     eachline = re.sub("Ms. ", 'Ms.', eachline)
#                                     eachline = re.sub("Mr. ", 'Mr.', eachline)
#                                     f2.write(eachline + '\n')
#                                 else:
#                                     if re.search("Ms. ",eachline)==None and re.search("Mr. ",eachline)==None:
#                                         eachline=eachline
#                                         f2.write(eachline+'\n')
