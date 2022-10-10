#--multiplication table
table   =int(input("Enter the table :"))
start   =int(input("Enter the starting number : "))
limit   =int(input("Enter the limit :"))
while(start<=limit):
  print(start,"*",table,"=",start*table)
  start=start+1
  