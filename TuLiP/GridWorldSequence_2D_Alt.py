from tulip import transys, spec, synth
import time

for x in [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]:
	xMaxBound = x + 1
	xMinBound = 0
	stateslist = ['B1','B2','farB1','farB2','U1','U2','farU1','farU2','UR1','UR2','UL1','UL2','BL1','BL2','BR1','BR2','farL1','farR1','L1','R1','In1','In2','R2','L2','farR2','farL2','faraway']
	atomiclist = ['aB1','aB2','afarB1','afarB2','aU1','aU2','afarU1','afarU2','aUR1','aUR2','aUL1','aUL2','aBL1','aBL2','aBR1','aBR2','afarL1','afarR1','aL1','aR1','aIn1','aIn2','aR2','aL2','afarR2','afarL2','afaraway']
	#stateslist = ['farL1','farR1','L1','R1','In1','In2','R2','L2','farR2','farL2','faraway']
	#atomiclist = ['aIn2','aR2','aL2','afarR2','afarL2','aIn1','aR1','aL1','afarR1','afarL1','afaraway']	
	sys = transys.FTS()
	speclist = []
	sys.states.add_from(stateslist)
	sys.states.initial.add('R2')
	atomicset = set(atomiclist)
	sys.atomic_propositions.add_from(atomicset)

	sys.transitions.add_comb({'farL1'},{'faraway','L2','farL2'})
	sys.transitions.add_comb({'farR1'},{'faraway','R2','farR2'})
	sys.transitions.add_comb({'L1'},{'In2','farL2','L2','UL2','BL2'})
	sys.transitions.add_comb({'R1'},{'In2','farR2','R2','UR2','BR2'})
	sys.transitions.add_comb({'In1'},{'In2','R2','L2','U2','B2'})
	#sys.transitions.add_comb({'In2'},{'In1','R1','L1','U1','B1'})
	sys.transitions.add_comb({'R2'},{'In1','R1','farR1','UR1','BR1'})
	sys.transitions.add_comb({'L2'},{'In1','L1','farL1','UL1','BL1'})
	sys.transitions.add_comb({'farR2'},{'faraway','R1','farR1'})
	sys.transitions.add_comb({'farL2'},{'faraway','L1','farL1'})
	#sys.transitions.add_comb({'faraway'},{'faraway'})
	sys.transitions.add_comb({'U1'},{'In2','farU2','UR2','UL2','U2'})
	sys.transitions.add_comb({'U2'},{'In1','farU1','UR1','UL1','U1'})
	sys.transitions.add_comb({'B1'},{'In2','farB2','BR2','BL2','B2'})
	sys.transitions.add_comb({'B2'},{'In1','farB1','BR1','BL1','B1'})
	sys.transitions.add_comb({'farU1'},{'faraway','U2','farU2'})
	sys.transitions.add_comb({'farU2'},{'faraway','U1','farU1'})
	sys.transitions.add_comb({'farB1'},{'faraway','B2','farB2'})
	sys.transitions.add_comb({'farB2'},{'faraway','B1','farB1'})
	sys.transitions.add_comb({'UR1'},{'faraway','R2','U2'})
	sys.transitions.add_comb({'UR2'},{'faraway','R1','U1'})
	sys.transitions.add_comb({'BR1'},{'faraway','R2','B2'})
	sys.transitions.add_comb({'BR2'},{'faraway','R1','B1'})
	sys.transitions.add_comb({'UL1'},{'faraway','U2','L2'})
	sys.transitions.add_comb({'UL2'},{'faraway','U1','L1'})
	sys.transitions.add_comb({'BL1'},{'faraway','B2','L2'})
	sys.transitions.add_comb({'BL2'},{'faraway','B1','L1'})

	for i,m in enumerate(stateslist):
		sys.states.add(m, ap={atomiclist[i]})


	speclist.append('!afaraway')
	speclist.append('!aIn2')

	speclist.append('(stay && aR2) -> X(aR1)')
	speclist.append('(stay && aL2) -> X(aL1)')
	speclist.append('(stay && aB2) -> X(aB1)')
	speclist.append('(stay && aU2) -> X(aU1)')

	speclist.append('(stay && aUR2) -> X(aUR1)')
	speclist.append('(stay && aUL2) -> X(aUL1)')
	speclist.append('(stay && aBR2) -> X(aBR1)')
	speclist.append('(stay && aBL2) -> X(aBL1)')

	#speclist.append('(stay && afarU2) -> X(afarU1)')
	#speclist.append('(stay && afarB2) -> X(afarB1)')
	#speclist.append('(stay && afarR2) -> X(afarR1)')
	#speclist.append('(stay && afarL2) -> X(afarL1)')

	speclist.append('(right && aR2) -> X(afarR1)')
	speclist.append('(right && aL2) -> X(aIn1)')
	speclist.append('(right && afarR2) -> X(afaraway)')
	#speclist.append('(right && afarL2) -> X(aL1)')
	speclist.append('(right && aB2) -> X(aBR1)')
	speclist.append('(right && aU2) -> X(aUR1)')
	speclist.append('(right && aUR2) -> X(afaraway)')
	#speclist.append('(right && aUL2) -> X(aU1)')
	speclist.append('(right && aBR2) -> X(afaraway)')
	#speclist.append('(right && aBL2) -> X(aB1)')
	speclist.append('(right && afarU2) -> X(afaraway)')
	speclist.append('(right && afarB2) -> X(afaraway)')

	speclist.append('(up && aR2) -> X(aUR1)')
	speclist.append('(up && aL2) -> X(aUL1)')
	speclist.append('(up && afarR2) -> X(afaraway)')
	speclist.append('(up && afarL2) -> X(afaraway)')
	speclist.append('(up && aB2) -> X(aIn1)')
	speclist.append('(up && aU2) -> X(afarU1)')
	speclist.append('(up && aUR2) -> X(afaraway)')
	speclist.append('(up && aUL2) -> X(afaraway)')
	#speclist.append('(up && aBR2) -> X(aR1)')
	#speclist.append('(up && aBL2) -> X(aL1)')
	speclist.append('(up && afarU2) -> X(afaraway)')
	#speclist.append('(up && afarB2) -> X(aB1)')

	speclist.append('(down && aR2) -> X(aBR1)')
	speclist.append('(down && aL2) -> X(aBL1)')
	speclist.append('(down && afarR2) -> X(afaraway)')
	speclist.append('(down && afarL2) -> X(afaraway)')
	speclist.append('(down && aB2) -> X(afarB1)')
	speclist.append('(down && aU2) -> X(aIn1)')
	#speclist.append('(down && aUR2) -> X(aR1)')
	#speclist.append('(down && aUL2) -> X(aL1)')
	speclist.append('(down && aBR2) -> X(afaraway)')
	speclist.append('(down && aBL2) -> X(afaraway)')
	#speclist.append('(down && afarU2) -> X(aU1)')
	speclist.append('(down && afarB2) -> X(afaraway)')

	speclist.append('(left && aR2) -> X(aIn1)')
	speclist.append('(left && aL2) -> X(afarL1)')
	#speclist.append('(left && afarR2) -> X(aR1)')
	speclist.append('(left && afarL2) -> X(afaraway)')
	speclist.append('(left && aB2) -> X(aBL1)')
	speclist.append('(left && aU2) -> X(aUL1)')
	#speclist.append('(left && aUR2) -> X(aU1)')
	speclist.append('(left && aUL2) -> X(afaraway)')
	#speclist.append('(left && aBR2) -> X(aB1)')
	speclist.append('(left && aBL2) -> X(afaraway)')
	speclist.append('(left && afarU2) -> X(afaraway)')
	speclist.append('(left && afarB2) -> X(afaraway)')

	speclist.append('stage != '+str(xMaxBound))
	speclist.append('stage != 0')
	speclist.append('ystage != '+str(xMaxBound))
	speclist.append('ystage != 0')

	specset = set(speclist)

	env_vars = {'right','left','stay','up','down'}

	env_init = {'!down'}
	env_prog = set()
	
	env_safe = {'(right && !left && !stay && !up && !down) || (!right && left && !stay && !up && !down) || (!right && !left && stay && !up && !down)|| (!right && !left && !stay && up && !down) || (!right && !left && !stay && !up && down)'}
	
	env_safe |= {'aL2 -> X(stay)'}
	env_safe |= {'aR2 -> X(stay)'}
	#env_safe |= {'afarR2 -> X(stay)'}
	#env_safe |= {'afarL2 -> X(stay)'}
	#env_safe |= {'aBL2 -> X(stay)'}
	#env_safe |= {'aBR2 -> X(stay)'}
	#env_safe |= {'aUL2 -> X(stay)'}
	#env_safe |= {'aUR2 -> X(stay)'}
	#env_safe |= {'afarB2 -> X(stay)'}
	#env_safe |= {'afarU2 -> X(stay)'}
	env_safe |= {'aB2 -> X(stay)'}
	env_safe |= {'aU2 -> X(stay)'}

	env_safe |= {'(stage = '+str(xMaxBound-1)+') -> X(!right)'}
	env_safe |= {'(stage = 1) -> X(!left)'}
	env_safe |= {'(ystage = '+str(xMaxBound-1)+') -> X(!up)'}
	env_safe |= {'(ystage = 1) -> X(!down)'}
	sys_vars = dict()
	sys_init = {'stage = 2'}
	sys_init |= {'ystage = 2'}
	sys_vars['stage'] = (0,xMaxBound)
	sys_vars['ystage'] = (0,xMaxBound)
	sys_prog = set()
	sys_safe = set()

	for i in range(1,xMaxBound):
		sys_safe |= {('((stage = '+str(i)+')  && right) -> (X (stage = '+str(i+1)+'))')}
		sys_safe |= {('((ystage = '+str(i)+')  && up) -> (X (ystage = '+str(i+1)+'))')}

	sys_safe |= {('(stage = '+str(xMaxBound-1)+') -> (!(aL1 || aL2 || afarL2 || afarL1 || aBL1 || aBL2 || aUL1 || aUL2  ))')}
	sys_safe |= {('(stage = 1) -> (!(aR1 || afarR2 || afarR1|| aR2 || aBR1 || aBR2 || aUR1 || aUR2    ))')}
	sys_safe |= {('(ystage = '+str(xMaxBound-1)+') -> (!(aB1 || afarB2 || afarB1|| aB2 || aBL1 || aBL2 || aBR1 || aBL2  ))')}
	sys_safe |= {('(ystage = 1) -> (!(aU1 || aU2 || afarU2 || afarU1 || aUL1 || aUL2 || aUR1 || aUL2))')} 

	for i in range(0,xMaxBound+1):
		sys_safe |= {('((stage = '+str(i)+')   && stay) -> (X (stage = '+str(i)+'))')}
		sys_safe |= {('((ystage = '+str(i)+')   && stay) -> (X (ystage = '+str(i)+'))')}

	for i in range(1,xMaxBound):
		sys_safe |= {('((stage = '+str(i)+')  && left) -> (X (stage = '+str(i-1)+'))')}
		sys_safe |= {('((ystage = '+str(i)+')  && down) -> (X (ystage = '+str(i-1)+'))')}

	sys_safe |= specset

	specs = spec.GRSpec(env_vars, sys_vars, env_init, sys_init,env_safe, sys_safe, env_prog, sys_prog )
	start = time.clock()
	ctrl = synth.synthesize('gr1c',specs, sys=sys)

	#if not ctrl.save('discerete'+str(x)+'.png'):
		#print(ctrl)

	finish = time.clock()

	with open("Output2da.txt", "a") as text_file:
	    text_file.write("{0}: {1}  Size: {2}\n".format(x,finish - start,ctrl.size()))

	#ignore_env_init= True env = env1
