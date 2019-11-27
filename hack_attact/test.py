
# with open('test','r') as f:
#     while True:
#         line = f.readline()
#         if line:
#             print(line.strip(),end=' ')
#         else:
#             print('no more line')
#             break

# defaut_page_patter_li = ['.php','.html','.htm','.asp']
# # page_li = ['index.html','reee','first.jsp','index.asp']
# #
# # res_li = []
# # for page in page_li:
# #     for dpp in defaut_page_patter_li:
# #         if page.endswith(dpp):
# #             res_li.append(page)
# #
# # print(res_li)

new_file = open('newfile','w')
new_file.write('./test')
new_file.close()