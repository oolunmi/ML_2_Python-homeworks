mat = [[1,2],[3,4]]
r = 1
c = 5

def reshape(mat,r,c):
    if r*c==len(mat)*len(mat[0]):
      list=[]
      reshaped=[[0 for j in range(c)] for i in range(r)]
      for i in range(len(mat)):
          for j in range(len(mat[i])):            
              list.append(mat[i][j])
      print(list)
      for i in range(r):
          for j in range(c):
              if (i+1)==1:
                  reshaped[i][j]=list[j]
              else:
                  reshaped[i][j]=list[(((i+1)-1)*c)+(j+1)]
      return reshaped
    else:
        print("It is impossible to resahpe given matrix to a matrix with given parameters")

print(reshape(mat,r,c))

