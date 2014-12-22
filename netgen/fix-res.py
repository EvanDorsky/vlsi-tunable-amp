import re, sys

def fix_resistors(netlist_path):
	newfile_name = netlist_path[:-6]+"-fixed.spice"
	fixed = open(newfile_name, 'w')

	resistors = 0
	with open(netlist_path, 'r') as netlist:
		for line in netlist:
			find_res = re.match(r"M(\d{4})(( \w+#?)+) phrResistor w=(\d+.?\d+)u? l=(\d+.?\d+)u?", line)

			if (find_res):
				resistors+=1
				name = find_res.group(1)
				nets = find_res.group(2).strip().split(" ")
				w = float(find_res.group(4))
				l = float(find_res.group(5))

				R = l/w*1e3
				# overwrite this line with the corrected one
				line = "R"+name + " " + nets[0] + " " + nets[2] + " " + str(R/1000.0)+"k\n"

			fixed.write(line)
	fixed.close()
	print "Fixed",resistors,"resistors."

if (__name__ == "__main__"):
	fix_resistors(sys.argv[1])