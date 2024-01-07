import sys

source_file = sys.argv[1]
target_file = sys.argv[2]

print("\n HELLO -----------")
print(source_file)
print(target_file)
print("--------------------")

source = open(source_file, "r")
in_data = source.read()
source.close()

out_string = in_data.upper()
print("Finish --------------")

target = open(target_file, "w")
target.write(out_string)
target.close()