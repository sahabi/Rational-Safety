from tulip import transys, spec, synth
import time


obstacles = [1, 3, 12, 14, 16, 18, 21, 25, 27, 28, 30, 31, 43, 44, 47, 56, 57, 60, 62, 69, 73, 74, 75, 77, 78, 79]


for q in [9]:

	x = q
	y = q
	s_states = x*y
	e_states = x*y
	stateslista = []
	stateslistb = []
	atomiclist = []
	atomiclistb = []
	sys = transys.FTS()
	env1 = transys.FTS()
	env1.owner = 'env'
	speclist = []

	for s in range(0,e_states):
		if s not in obstacles:
			    atomiclistb.append('b'+str(s))

	for s in range(0,s_states):
		if s not in obstacles:
			    atomiclist.append('a'+str(s))

	for s in range(0,s_states):
		if s not in obstacles:
		    stateslista.append('s'+str(s))

	for s in range(0,e_states):
		if s not in obstacles:
		    stateslistb.append('e'+str(s))

	sys.states.add_from(stateslista)
	env1.states.add_from(stateslistb)
	sys.states.initial.add('s9')
	env1.states.initial.add('e9')

	atomicset = set(atomiclist)
	atomicsetb = set(atomiclistb)
	sys.atomic_propositions.add_from(atomicset)
	env1.atomic_propositions.add_from(atomicsetb)

	for i in range(0,s_states):

		if i == 0:
			if (i not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i+x)})
			elif (i not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1)})
		elif i == x - 1:
			if (i not in obstacles) and (i+x not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x)})
			elif (i not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1)})
		elif i == (x * y) - 1:
			if (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i-x)})
			elif (i not in obstacles) and (i-x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)},{'s'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1)})
		elif i == x * (y - 1):
			if (i not in obstacles) and (i-x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i-x)})
			elif (i not in obstacles) and (i-x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1)})
		elif i < x:
			if (i not in obstacles) and (i+x not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i+x),'s'+str(i-1)})
			elif (i not in obstacles) and (i+x not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x),'s'+str(i-1)})
			elif (i not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i-1)})
			elif (i not in obstacles) and (i+1 not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i+x)})
			elif (i not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1)})
		elif i >= x * (y - 1):
			if (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i-x),'s'+str(i-1)})

			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) :
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-x),'s'+str(i-1)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i-1)})

			elif (i not in obstacles) and (i-x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1)})

		elif i % x == 0:
			if (i not in obstacles) and (i-x not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i+x),'s'+str(i-x)})

			elif (i not in obstacles) and (i-x not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x),'s'+str(i-x)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i-1)})

			elif (i not in obstacles) and (i-x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1)})

		elif i % x == x - 1:
			if (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x),'s'+str(i-x)})

			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x),'s'+str(i-x)})

			elif (i not in obstacles) and (i-x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1)})
			elif (i not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x)})

		else:
			if (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x),'s'+str(i-x),'s'+str(i+1)})

			elif (i not in obstacles)and (i-x not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x),'s'+str(i-x),'s'+str(i+1)})
			elif (i not in obstacles)  and (i-1 not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x),'s'+str(i+1)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i-x),'s'+str(i+1)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x),'s'+str(i-x)})

			elif (i not in obstacles)and (i-x not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x),'s'+str(i-x)})
			elif (i not in obstacles)  and (i-1 not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+1)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i-x)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-x),'s'+str(i+1)})
			elif (i not in obstacles) and (i+x not in obstacles) and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x)})
			elif (i not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x),'s'+str(i+1)})

			elif (i not in obstacles) and (i-x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1)})
			elif (i not in obstacles)and (i-1 not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1)})
			elif (i not in obstacles) and (i+x not in obstacles):
				sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+x)})



	for i in range(0,e_states):

		if i == 0:
			if (i not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i+x)})
			elif (i not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1)})
		elif i == x - 1:
			if (i not in obstacles) and (i+x not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x)})
			elif (i not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1)})
		elif i == (x * y) - 1:
			if (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i-x)})
			elif (i not in obstacles) and (i-x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)},{'e'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1)})
		elif i == x * (y - 1):
			if (i not in obstacles) and (i-x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i-x)})
			elif (i not in obstacles) and (i-x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1)})
		elif i < x:
			if (i not in obstacles) and (i+x not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i+x),'e'+str(i-1)})
			elif (i not in obstacles) and (i+x not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x),'e'+str(i-1)})
			elif (i not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i-1)})
			elif (i not in obstacles) and (i+1 not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i+x)})
			elif (i not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1)})
		elif i >= x * (y - 1):
			if (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i-x),'e'+str(i-1)})

			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) :
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-x),'e'+str(i-1)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i-1)})

			elif (i not in obstacles) and (i-x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1)})

		elif i % x == 0:
			if (i not in obstacles) and (i-x not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i+x),'e'+str(i-x)})

			elif (i not in obstacles) and (i-x not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x),'e'+str(i-x)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i-1)})

			elif (i not in obstacles) and (i-x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1)})

		elif i % x == x - 1:
			if (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x),'e'+str(i-x)})

			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x),'e'+str(i-x)})

			elif (i not in obstacles) and (i-x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-x)})
			elif (i not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1)})
			elif (i not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x)})

		else:
			if (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x),'e'+str(i-x),'e'+str(i+1)})

			elif (i not in obstacles)and (i-x not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x),'e'+str(i-x),'e'+str(i+1)})
			elif (i not in obstacles)  and (i-1 not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x),'e'+str(i+1)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i-x),'e'+str(i+1)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x),'e'+str(i-x)})

			elif (i not in obstacles)and (i-x not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x),'e'+str(i-x)})
			elif (i not in obstacles)  and (i-1 not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+1)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i-x)})
			elif (i not in obstacles) and (i-x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-x),'e'+str(i+1)})
			elif (i not in obstacles) and (i+x not in obstacles) and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x)})
			elif (i not in obstacles) and (i+x not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x),'e'+str(i+1)})

			elif (i not in obstacles) and (i-x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-x)})
			elif (i not in obstacles) and (i+1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1)})
			elif (i not in obstacles)and (i-1 not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1)})
			elif (i not in obstacles) and (i+x not in obstacles):
				env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+x)})

	specstring = ''
	for x in range(0,e_states):
		if x not in obstacles:
			    sys.states.add('s'+str(x), ap={'a'+str(x)})
			    env1.states.add('e'+str(x), ap={'b'+str(x)})

	for x in range(0,s_states-1):
		if x not in obstacles:
			    specstring += '(a'+str(x)+' && b'+str(x)+') || '

	specstring += '(a'+str(s_states-1)+' && b'+str(s_states-1)+')'
	speclist.append(specstring)

	specset = set(speclist)
	print specset
	env_vars = set()

	env_init = set()

	env_prog = set()

	env_safe = set()

	sys_vars = set()

	sys_init = set()

	sys_prog = set()

	sys_safe = specset

	specs = spec.GRSpec(env_vars, sys_vars, env_init, sys_init,
		            env_safe, sys_safe, env_prog, sys_prog, )
	start = time.clock()
	ctrl = synth.synthesize('gr1c',specs, sys=sys,env = env1)
	finish = time.clock()
	#if not ctrl.save('disceretee'+str(q)+'.png'):
#		print(ctrl)

	print finish - start

	with open("Output2d.txt", "a") as text_file:
	    text_file.write("{0}: {1} Size: {2}\n".format(q,finish - start,ctrl.size()))

	#ignore_env_init= True env = env1
