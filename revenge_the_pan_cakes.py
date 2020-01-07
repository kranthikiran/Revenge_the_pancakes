import argparse

def popFlipPush(qu, pos):
    qa,qb = [],[]
    try:
        qa = list(qu[:pos])
        qb = list(qu[pos:])
    except TypeError:
        pass

    # Flip qa and symbols
    qa.reverse()
    for i in range(len(qa)):
        qa[i] = '-' if qa[i] == '+' else '+'

    qa.extend(qb)
    return ''.join(qa)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_file", "-if", type=str, required=True)
	parser.add_argument("--output_file", "-of", type=str, required=True)
	args = parser.parse_args()
	f = open(args.input_file)
	lines = f.readlines()
	out_put=''
	T = int(lines[0].strip())
	out_put += 'T is %s' % T + '\n'
	for t in range(T):
	    S = str(lines[t+1]).strip()
	    # Happy side And bad side
	    G = ''
	    NG = ''
	    for i in range(len(S.strip())):
	        G += '+'
	        NG += '-'
	    count = 0
	    while True:
	        if S == G:
	            break
	        elif S == NG:
	            count += 1
	            break
	        else:
	            diff = 0
	            for i in range(1,len(S)):
	                if S[i] != S[0]:
	                    S = popFlipPush(S, i)
	                    count += 1
	                    break
	    out_put +='Case #' + str(t+1) + ': ' + str(count) + '\n'
	    print('Case #' + str(t+1) + ': ' + str(count))
	    with open(args.output_file, 'w') as output_file:
		output_file.write(out_put)
		output_file.close()
		
if __name__ == "__main__":
    main()
