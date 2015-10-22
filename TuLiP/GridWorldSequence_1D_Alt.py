from tulip import transys, spec, synth
import time

for x in [3000,5000,10000]:
	xMaxBound = x + 1
	xMinBound = 0

	stateslist = ['farL1','farR1','L1','R1','In1','In2','R2','L2','farR2','farL2','faraway']
	atomiclist = ['aIn2','aR2','aL2','afarR2','afarL2','aIn1','aR1','aL1','afarR1','afarL1','afaraway']
	sys = transys.FTS()
	speclist = []
	sys.states.add_from(stateslist)
	sys.states.initial.add('R2')
	atomicset = set(atomiclist)
	sys.atomic_propositions.add_from(atomicset)

	sys.transitions.add_comb({'farL1'},{'faraway','L2','farL2'})
	sys.transitions.add_comb({'farR1'},{'faraway','R2','farR2'})
	sys.transitions.add_comb({'L1'},{'In2','farL2','L2'})
	sys.transitions.add_comb({'R1'},{'In2','farR2','R2'})
	sys.transitions.add_comb({'In1'},{'In2','R2','L2'})
	sys.transitions.add_comb({'In2'},{'In1','R1','L1'})
	sys.transitions.add_comb({'R2'},{'In1','R1','farR1'})
	sys.transitions.add_comb({'L2'},{'In1','L1','farL1'})
	sys.transitions.add_comb({'farR2'},{'faraway','R1','farR1'})
	sys.transitions.add_comb({'farL2'},{'faraway','L1','farL1'})
	sys.transitions.add_comb({'faraway'},{'faraway'})


	sys.states.add('faraway', ap={'afaraway'})
	sys.states.add('In2', ap={'aIn2'})
	sys.states.add('R2', ap={'aR2'})
	sys.states.add('L2', ap={'aL2'})
	sys.states.add('farR2', ap={'afarR2'})
	sys.states.add('farL2', ap={'afarL2'})
	sys.states.add('In1', ap={'aIn1'})
	sys.states.add('R1', ap={'aR1'})
	sys.states.add('L1', ap={'aL1'})
	sys.states.add('farR1', ap={'afarR1'})
	sys.states.add('farL1', ap={'afarL1'})

	speclist.append('!afaraway')
	speclist.append('!aIn2')
	speclist.append('(stay && aR2) -> X(aR1)')
	speclist.append('(stay && aL2) -> X(aL1)')
	speclist.append('(stay && afarR2) -> X(afarR1)')
	speclist.append('(stay && afarL2) -> X(afarL1)')
	speclist.append('(right && aR2) -> X(afarR1)')
	speclist.append('(right && aL2) -> X(aIn1)')
	speclist.append('(right && afarR2) -> X(afaraway)')
	speclist.append('(right && afarL2) -> X(aL1)')
	speclist.append('(left && aR2) -> X(aIn1)')
	speclist.append('(left && aL2) -> X(afarL1)')
	speclist.append('(left && afarR2) -> X(aR1)')
	speclist.append('(left && afarL2) -> X(afaraway)')
	speclist.append('stage !='+str(xMaxBound))
	speclist.append('stage != 0')

	specset = set(speclist)

	env_vars = {'right','left','stay'}
	#env_init = {'stay'}
	env_init = set()
	env_prog = set()
	env_safe = {'(right && !left && !stay) || (!right && left && !stay) || (!right && !left && stay)'}
	env_safe |= {'aL2 -> X(stay)'}
	env_safe |= {'aR2 -> X(stay)'}
	env_safe |= {'afarR2 -> X(stay)'}
	env_safe |= {'afarL2 -> X(stay)'}
	env_safe |= {'aIn2 -> X(stay)'}
	env_safe |= {'(stage = '+str(xMaxBound-1)+') -> X(!right)'}
	env_safe |= {'(stage = 1) -> X(!left)'}
	sys_vars = dict()
	sys_init = {'stage = 2'}
	sys_vars['stage'] = (xMinBound,xMaxBound)
	sys_prog = set()
	sys_safe = set()

	for i in range(1,xMaxBound):
		sys_safe |= {('((stage = '+str(i)+')  && right) -> (X (stage = '+str(i+1)+'))')}

	sys_safe |= {('(stage = 4) -> (!(aL1 || aL2 || afarL2 || afarL1))')}
	sys_safe |= {('(stage = 1) -> (!(aR1 || afarR2 || afarR1|| aR2  ))')} 
	
	for i in range(0,xMaxBound+1):
		sys_safe |= {('((stage = '+str(i)+')   && stay) -> (X (stage = '+str(i)+'))')}

	for i in range(1,xMaxBound):
		sys_safe |= {('((stage = '+str(i)+')  && left) -> (X (stage = '+str(i-1)+'))')}
	sys_safe |= specset

	specs = spec.GRSpec(env_vars, sys_vars, env_init, sys_init,env_safe, sys_safe, env_prog, sys_prog )
	start = time.clock()
	ctrl = synth.synthesize('gr1c',specs, sys=sys)

	#if not ctrl.save('discerete'+str(x)+'.png'):
	#	print(ctrl)

	finish = time.clock()

	with open("Output1da.txt", "a") as text_file:
	    text_file.write("{0}: {1}  Size: {2}\n".format(x,finish - start,ctrl.size()))

	#ignore_env_init= True env = env1
