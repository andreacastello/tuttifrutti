import sys

if len(sys.argv) < 4:
    print("Usage python glue.py <source_file_nam> <dest_file_name> <how_mmany_times>")

src_file = sys.argv[1]
dst_file = sys.argv[2]
num_times = int(sys.argv[3])

# Read source file. I don't expect a huge file (otherwise I won't be using this hack)
src = open(src_file, 'r')
lines = src.readlines()
#
# write to file N copies of src file
dest = open(dst_file, 'w')
for i in range(num_times):
    dest.writelines(lines)
    dest.write('\n')
src.close()
dest.close()

print("content of file "
      + src_file
      + " copied "
      + str(num_times)
      + " to " + dst_file)
