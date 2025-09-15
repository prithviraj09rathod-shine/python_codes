#two ways to achiveve generator in python
#1. using function and yield keyword
#2. using generator expression
#generator is used to iterate a sequence of values, it generates values on the fly and does
#not store them in memory, hence it is memory efficient
#once a value is generated it is not stored, so we can only iterate through it once
#we can use next() function to get the next value from the generator
#once all values are generated, it raises StopIteration exception

def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
print(next(gen))  #1
print(next(gen))  #2
print(next(gen))  #3

lits2 = (x*x for x in range(1,4)) #generator expression
print(next(lits2))  #1
print(next(lits2))  #4
print(next(lits2))  #9

#example of list comprehension
list3 = [x*x for x in range(1,4)] #list comprehension
print(list3)  #[1, 4, 9]
#list comprehension stores all values in memory,
# so we can iterate through it multiple times  
# eg: we can use for loop to iterate through it multiple times
# but generator can be iterated only once
for i in list3:
    print(i)  #1 4 9 

#generator for reading line one by one using yield keyword
def read_file_line_by_line(file_path):
    with open(file_path, 'r') as fileptr:
        for line in fileptr:
            yield line.strip()  #strip() removes leading/trailing whitespace/newline characters     
file_path = 'test.txt'  #make sure this file exists with some content
line_generator = read_file_line_by_line(file_path)
for line in line_generator:
    print(line)  #prints each line from the file one by one
#once all lines are read, it raises StopIteration exception


#we can also use next() to get the next line
line_gen = read_file_line_by_line(file_path)
print(next(line_gen))  #prints first line
print(next(line_gen))  #prints second line
print(next(line_gen))  #prints third line
#and so on until all lines are read
print(next(line_gen))  #raises StopIteration exception if no more lines


#we can also use try-except to handle StopIteration exception
line_gen2 = read_file_line_by_line(file_path)
try:
    while True:
        print(next(line_gen2))  #prints each line until StopIteration
except StopIteration:
    print("All lines read, StopIteration exception caught.")
#once all lines are read, it raises StopIteration exception
#we can also convert generator to list using list() function
line_gen3 = read_file_line_by_line(file_path)