reg_count = 0
label_count = 0
arg_count = 0

def generate_new_temporary():
	global reg_count
	ret = "t" + str(reg_count)
	reg_count += 1
	return ret

def get_new_label():
	global label_count
	ret = "L"+str(label_count)
	label_count += 1
	return ret

def generate_new_argument():
	global arg_count
	ret = "a"+str(arg_count)
	arg_count += 1
	return ret

def reset():
	global arg_count
	arg_count = 0