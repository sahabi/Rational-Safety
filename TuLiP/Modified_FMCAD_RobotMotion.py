from tulip import transys, spec, synth
import time



k = 100
stateslista = []
stateslistb = []
atomiclist = []
atomiclistb = []
sys = transys.FTS()
speclist = []
for x in range(0,k+1):
    atomiclistb.append('b'+str(x))
for x in range(0,k+1):
    atomiclist.append('a'+str(x))
for x in range(0,k+1):
    stateslista.append('s'+str(x))
for x in range(0,k+1):
    stateslistb.append('e'+str(x))

sys.states.add_from(stateslista)
sys.states.add_from(stateslistb)
sys.states.initial.add('s1')
#env1.states.initial.add('e1')

atomicset = set(atomiclist)
atomicset |= set(atomiclistb)
sys.atomic_propositions.add_from(atomicset)
for x in range(1,k/2):
    sys.transitions.add_comb({'s'+str(x)},{'e'+str(x-1),'e'+str(x)})
    sys.transitions.add_comb({'e'+str(x)},{'s'+str(x),'s'+str(x+1)})

for x in range(k/2,k):
    sys.transitions.add_comb({'s'+str(x)}, {'e'+str(x+1),'e'+str(x)})
    sys.transitions.add_comb({'e'+str(x)},{'s'+str(x)})
    sys.transitions.add_comb({'e'+str(x)},{'s'+str(x+1)})

sys.transitions.add_comb({'s0'}, {'e1','e0'})

sys.transitions.add_comb({'s'+str(k)}, {'e'+str(k)})


for x in range(1,k+1):
    sys.states.add('s'+str(x), ap={'a'+str(x)})
    sys.states.add('e'+str(x), ap={'b'+str(x)})
#env1.states.add('e'+str(k), ap={'b'+str(k)})
speclist.append('!a'+str(k))
#speclist.append('!b'+str(k))
specset = set(speclist)
env_vars = {'env3'}

#env_vars = set()

env_init = set()

env_prog = set()

env_safe = set()

sys_vars = set()

sys_init = set()

sys_prog = set()

sys_safe = specset
for x in range(k):
    sys_safe |= {('((env3) && b'+str(x)+') -> X (a'+str(x+1)+')')}

specs = spec.GRSpec(env_vars, sys_vars, env_init, sys_init,
                    env_safe, sys_safe, env_prog, sys_prog, )
start = time.clock()
ctrl = synth.synthesize('gr1c',specs, sys=sys)

if not ctrl.save('discerete.png'):
	print(ctrl)

finish = time.clock()

print finish - start
#ignore_env_init= True env = env1
