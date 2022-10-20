
search = "hello farm goods hospital"
search_contents =search.split(' ')
search_content_list =[]
for i in search_contents:
  search_content_list.append(i)

def search_str(file_path, word):
    with open(file_path, 'r') as file:
  # read all content of a file
      content = file.read()
  # check if string present in a file
      for i in word:
         if i in content:
            print(i)



search_str("item.txt",search_content_list)