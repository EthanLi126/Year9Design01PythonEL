#loops are for patterns and stuff

#this is a counted loop. i want you to think about
#count, check  change
# i = 0, 0 < 5, TRUE -RUN LOOP
# i = 1, 1 < 5, TRUE -RUN LOOP
# i = 2, 2 < 5, TRUE -RUN LOOP
# i = 3, 3 < 5, TRUE -RUN LOOP
# i = 4, 4 < 5, TRUE -RUN LOOP
# i = 5, 5 < 5, FALSE -EXIT AND MOVE ON
for i in range(1,1330,3):
	#    anything tabbed is in the liio bkicj
	#count,check,change
	# first number is starting second is inclusive what it's up to if u want 12345 second number is 6, 1 is increment
	print(i)

print("***BACKWARDS***")

for i in range(10,-1,-1):

	print(i)

print("***printing string characters***")

str= "Monkey"

#use loop to print out indexes in a word
#always indiate the length of a word using the function
#len
for i in range(0,6,1):
##or
##for i in range(0,len(str), 1):

	print(str[i])

print ("**printing string backwards**")

for i in range(5,-1,-1):
	#or
	#for i in range(len(str) -1,-1,-1):

	print(str[i])

print ("every second letter in str starting at index 0")
for i in range(0,len(str),2):

	print(str[i])


