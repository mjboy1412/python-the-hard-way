from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

print("Let me write some thing stupid to the target file first !!!")
in_file_to_write = open(from_file, "w")
in_file_to_write.write("This the text int test.txt \n This text will be copy to the test_copy.txt")
in_file_to_write.close()

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
in_file.close()

print("The input file is %d bytes long" % len(indata))
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()

print("Alright, all done.")
print("Here is the out file:")
out_file_to_read = open(to_file)
print(out_file_to_read.read())
out_file_to_read.close()

