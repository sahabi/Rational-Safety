from tulip import transys, spec, synth
import time

for q in [2,3,4,5,6,7,8,9]:

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
	    atomiclistb.append('b'+str(s))
	for s in range(0,s_states):
	    atomiclist.append('a'+str(s))
	for s in range(0,s_states):
	    stateslista.append('s'+str(s))
	for s in range(0,e_states):
	    stateslistb.append('e'+str(s))

	sys.states.add_from(stateslista)
	env1.states.add_from(stateslistb)
	sys.states.initial.add('s1')
	env1.states.initial.add('e1')

	atomicset = set(atomiclist)
	atomicsetb = set(atomiclistb)
	sys.atomic_propositions.add_from(atomicset)
	env1.atomic_propositions.add_from(atomicsetb)
	for i in range(0,s_states):

		if i == 0:
			sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i+x)})
		elif i == x - 1:
			sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x)})
		elif i == (x * y) - 1:
			sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i-x)})
		elif i == x * (y - 1):
			sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i-x)})
		elif i < x:
			sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i+x),'s'+str(i-1)})
		elif i >= x * (y - 1):
			sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i-x),'s'+str(i-1)})
		elif i % x == 0:
			sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i+1),'s'+str(i+x),'s'+str(i-x)})
		elif i % x == x - 1:
			sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x),'s'+str(i-x)})
		else:
			sys.transitions.add_comb({'s'+str(i)}, {'s'+str(i),'s'+str(i-1),'s'+str(i+x),'s'+str(i-x),'s'+str(i+1)})

	for i in range(0,e_states):

		if i == 0:
			env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i+x)})
		elif i == x - 1:
			env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x)})
		elif i == (x * y) - 1:
			env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i-x)})
		elif i == x * (y - 1):
			env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i-x)})
		elif i < x:
			env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i+x),'e'+str(i-1)})
		elif i >= x * (y - 1):
			env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i-x),'e'+str(i-1)})
		elif i % x == 0:
			env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i+1),'e'+str(i+x),'e'+str(i-x)})
		elif i % x == x - 1:
			env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x),'e'+str(i-x)})
		else:
			env1.transitions.add_comb({'e'+str(i)}, {'e'+str(i),'e'+str(i-1),'e'+str(i+x),'e'+str(i-x),'e'+str(i+1)})



	specstring = ''
	for x in range(0,e_states+1):
	    sys.states.add('s'+str(x), ap={'a'+str(x)})
	    env1.states.add('e'+str(x), ap={'b'+str(x)})

	for x in range(0,s_states):
	    specstring += '(a'+str(x)+' && b'+str(x)+') || '

	specstring += '(a'+str(s_states)+' && b'+str(s_states)+')'
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
	if not ctrl.save('disceretee'+str(q)+'.png'):
		print(ctrl)

	print finish - start

	with open("Output2d.txt", "a") as text_file:
	    text_file.write("{0}: {1} Size: {2}\n".format(q,finish - start,ctrl.size()))

