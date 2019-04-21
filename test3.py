
# # file reading and writting                                                                                                                    
# # read
# file = open('filereadtest.txt','r');
# print(file.readlines())
# file.close()
# write(add from start)
# data = ['sa','re','ga','ma']
# file = open ('writetext.txt', 'w')
# for s in data:
#     file.write(s + "\n")
#
# file.close()
# # append(add to the last text position)
# data = ['sa','re','ga','ma']
# file = open ('writetext.txt', 'w')
# for s in data:
#     file.write(s + "\n")
#
# file.close()
# #  with method(doesnt require a close). consised way of working on file
# with open('writetext.txt','+a') as file:
#     content = file.read();
#     file.seek(0);
#     file.write('pa')
#     print(content)
