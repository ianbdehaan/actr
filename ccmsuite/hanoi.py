import ccm
from ccm.lib.actr import *
log=ccm.log()

class SolveHanoi(ACTR):
    towers = Buffer()
    goal = Buffer()
    knowledge = Buffer()


    def initial_state(goal='action:init', towers='A ?a1 ?a2 ?a3 B ?b1 ?b2 ?b3 C ?c1 ?c2 ?c3'):
        print 'Initial state:'
        print 'Peg A has disks [{},{},{}], peg B has disks [{},{},{}], peg C has disks [{},{},{}]'.format(a1,a2,a3,b1,b2,b3,c1,c2,c3)
        goal.modify(action='think')

    #--------------------------------CHECKS FOR CLEAN NEED--------------------------------------------------
    def clean_needed_1(goal='action:think', towers='A ? ? ? B ? ? ? C !None!l ? ?'):
        goal.modify(action='clean')

    def clean_needed_2(goal='action:think', towers='A ? ? ? B ? ? ? C l s ?'):
        goal.modify(action='clean')

    def l_next(goal='action:think', towers='A ? ? ? B ? ? ? C None ? ?'):
        knowledge.set('next_disk:l')
        goal.modify(action='think2')

    def m_next(goal='action:think', towers='A ? ? ? B ? ? ? C l None ?'):
        knowledge.set('next_disk:m')
        goal.modify(action='think2')

    def s_next(goal='action:think', towers='A ? ? ? B ? ? ? C l m None'):
        knowledge.set('next_disk:s')
        goal.modify(action='think2')

    def completed(goal='action:think', towers='A None None None B None None None C l m s'):
        goal.clear()
    #---------------------------------CHECKS FOR UNOBSTRUCTION NEED=============================
    def a_needs_unobstruction(goal='action:think2', knowledge='next_disk:?disk', towers='A ?disk !None ? B ? ? ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:A'.format(disk))
        goal.modify(action='unobstruct')

    def b_needs_unobstruction(goal='action:think2', knowledge='next_disk:?disk', towers='A ? ? ? B ?disk !None ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:B'.format(disk))
        goal.modify(action='unobstruct')

    def a_no_unobstruction(goal='action:think2', knowledge='next_disk:?disk', towers='A ?disk None ? B ? ? ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:A'.format(disk))
        goal.modify(action='transfer')

    def b_no_unobstruction(goal='action:think2', knowledge='next_disk:?disk', towers='A ? ? ? B ?disk None ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:B'.format(disk))
        goal.modify(action='transfer')

    #-------------------------- CLEAN ACTIONS------------------------------------------------------------
    def clean_any_to_None_A(goal='action:clean', towers='A None None None B ?b1 ?b2 None C ?c1!None None None'):
        towers.set('A {} None None B {} {} None C None None None'.format(c1, b1, b2))
        print 'Disk {} was moved to peg A'.format(c1)
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format(c1,b1,b2)
        goal.modify(action='think')

    def clean_s_to_A(goal='action:clean', towers='A m None None B l None None C s None None'):
        towers.set('A {} {} None B {} None None C None None None'.format('m', 's', 'l'))
        print 'Disk {} was moved to peg C'.format('s')
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format('m','s','l')
        goal.modify(action='think')

    def clean_ms_to_A(goal='action:clean', towers='A None None None B l None None C m s None'):
        towers.set('A None None None B {} {} None C {} None None'.format('l', 's', 'm'))
        print 'Disk {} was moved to peg B'.format('s')
        print 'Peg A has disks [], peg B has disks [{},{}], peg C has disks [{}]'.format('l','s','m')
        towers.set('A {} None None B {} {} None C None None None'.format('m', 'l', 's'))
        print 'Disk {} was moved to peg A'.format('m')
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format('m','l','s')
        towers.set('A {} None None B {} {} None C None None None'.format('m', 'l', 's'))
        print 'Disk {} was moved to peg A'.format('s')
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format('m','s','l')
        goal.modify(action='think')

    def clean_m_s_in_A(goal='action:clean', towers='A s None None B l None None C m None None'):
        towers.set('A None None None B {} {} None C {} None None'.format('l','s','m'))
        print 'Disk {} was moved to peg B'.format('s')
        print 'Peg A has disks [], peg B has disks [{},{}], peg C has disks [{}]'.format('l','s','m')
        towers.set('A {} None None B {} {} None C None None None'.format('m','l','s'))
        print 'Disk {} was moved to peg C'.format('s')
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format('m','l','s')
        towers.set('A {} {} None B {} None None C None None None'.format('m','s','l'))
        print 'Disk {} was moved to peg A'.format('m')
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format('m','s','l')
        goal.modify(action='think')

    def clean_any_to_None_B(goal='action:clean', towers='A ?a1 ?a2 None B None None None C ?c1!None None None'):
        towers.set('A {} {} None B {} None None C None None None'.format(a1, a2, c1))
        print 'Disk {} was moved to peg B'.format(c1)
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format(a1,a2,c1)
        goal.modify(action='think')

    def clean_s_to_B(goal='action:clean', towers='A l None None B m None None C s None None'):
        towers.set('A {} None None B {} {} None C None None None'.format('l','m','s'))
        print 'Disk {} was moved to peg B'.format('s')
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format('l','m','s')
        goal.modify(action='think')

    def clean_ms_to_B(goal='action:clean', towers='A l None None B None None None C m s None'):
        towers.set('A {} {} None B None None C {} None None'.format('l', 's', 'm'))
        print 'Disk {} was moved to peg B'.format('s')
        print 'Peg A has disks [{},{}], peg B has disks [], peg C has disks [{}]'.format('l','s','m')
        towers.set('A {} {} None B {} None None C None None None'.format('l', 's', 'm'))
        print 'Disk {} was moved to peg B'.format('m')
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format('l','s','m')
        towers.set('A {} None None B {} {} None C None None None'.format('l','m', 's'))
        print 'Disk {} was moved to peg B'.format('s')
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format('l','m','s',)
        goal.modify(action='think')
        
    def clean_m_s_in_B(goal='action:clean', towers='A l None None B s None None C m None None'):
        towers.set('A {} {} None B None None None C {} None None'.format('l','s','m'))
        print 'Disk {} was moved to peg A'.format('s')
        print 'Peg A has disks [{},{}], peg B has disks [], peg C has disks [{}]'.format('l','s','m')
        towers.set('A {} {} None B {} None None C None None None'.format('l','s','m'))
        print 'Disk {} was moved to peg B'.format('m')
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format('l','m','s')
        towers.set('A {} None None B {} {} None C None None None'.format('l','m','s'))
        print 'Disk {} was moved to peg B'.format('s')
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format('l','m','s')
        goal.modify(action='think')

    def clean_ls_to_A(goal='action:clean', towers='A None None None B m None None C l s None'):
        towers.set('A {} None None B {} None None C {} None None'.format('s', 'm', 'l'))
        print 'Disk {} was moved to peg A'.format('s')
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format('s','m','l')
        goal.modify(action='think')

    def clean_ls_to_B(goal='action:clean', towers='A m None None B None None None C l s None'):
        towers.set('A {} None None B {} None None C {} None None'.format('m', 's', 'l'))
        print 'Disk {} was moved to peg A'.format('s')
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format('m','s','l')
        goal.modify(action='think')

    #-------------------------- UNOBSTRUCTION ACTIONS------------------------------------------------------------
    def unobstruct_full_a(goal='action:unobstruct', knowledge='next_disk:l in_tower:A', towers='A ?disk ?a2 ?a3!None B ? ? ? C ? ? ?'):
        towers.set('A {} {} None B None None None C {} None None'.format(disk, a2, a3))
        print 'Disk {} was moved to peg C'.format(a3)
        print 'Peg A has disks [{},{}], peg B has disks [], peg C has disks [{}]'.format(disk, a2, a3)
        towers.set('A {} None None B {} None None C {} None None'.format(disk, a2, a3))
        print 'Disk {} was moved to peg B'.format(a2)
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format(disk, a2, a3)
        knowledge.clear()
        goal.modify(action='think')

    def unobstruct_ls_a(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:A', towers='A ?disk s None B ?b1 ? ? C None ? ?'):
        towers.set('A {} None None B {} {} None C None None None'.format(disk, b1, 's'))
        print 'Disk {} was moved to peg B'.format('s')
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format(disk, b1, 's')
        knowledge.clear()
        goal.modify(action='think')

    def unobstruct_ms_a(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:A', towers='A ?disk s None B ? ? ? C ?c1!None ? ?'):
        towers.set('A {} None None B {} None None C {} None None'.format(disk, 's', c1))
        print 'Disk {} was moved to peg B'.format('s')
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format(disk, 's', c1)
        knowledge.clear()
        goal.modify(action='think')

    def unobstruct_lm_a(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:A', towers='A ?disk m None B ?b1 ? ? C None ? ?'):
        towers.set('A {} {} None B None None None C {} None None'.format(disk, 'm', b1))
        print 'Disk {} was moved to peg C'.format(b1)
        print 'Peg A has disks [{},{}], peg B has disks [], peg C has disks [{}]'.format(disk, 'm', b1)
        towers.set('A {} None None B {} None None C {} None None'.format(disk, 'm', b1))
        print 'Disk {} was moved to peg B'.format('m')
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format(disk, 'm', b1)
        knowledge.clear()
        goal.modify(action='think')

    def unobstruct_full_b(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:B', towers='A ? ? ? B ?disk ?b2 ?b3!None C ? ? ?'):
        towers.set('A None None None B {} {} None C {} None None'.format(disk, b2, b3))
        print 'Disk {} was moved to peg C'.format(b3)
        print 'Peg A has disks [], peg B has disks [{},{}], peg C has disks [{}]'.format(disk, b2, b3)
        towers.set('A {} None None B {} None None C {} None None'.format(b2, disk, b3))
        print 'Disk {} was moved to peg A'.format(b2)
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format(b2, disk, b3)
        knowledge.clear()
        goal.modify(action='think')

    def unobstruct_ls_b(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:B', towers='A ?a1 ? ? B ?disk s None C None ? ?'):
        towers.set('A {} {} None B {} None None C None None None'.format(a1, 's', disk))
        print 'Disk {} was moved to peg A'.format('s')
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format(a1, 's', disk)
        knowledge.clear()
        goal.modify(action='think')

    def unobstruct_ms_b(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:B', towers='A ? ? ? B ?disk s None C ?c1!None ? ?'):
        towers.set('A {} None None B {} None None C {} None None'.format('s', disk, c1))
        print 'Disk {} was moved to peg A'.format('s')
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format('s', disk, c1)
        knowledge.clear()
        goal.modify(action='think')

    def unobstruct_lm_b(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:B', towers='A ?a1 None None B ?disk m ? C None ? ?'):
        towers.set('A None None None B {} {} None C {} None None'.format(disk, 'm', a1))
        print 'Disk {} was moved to peg C'.format(a1)
        print 'Peg A has disks [], peg B has disks [{},{}], peg C has disks [{}]'.format(disk, 'm', a1)
        towers.set('A {} None None B {} None None C {} None None'.format('m',disk, a1))
        print 'Disk {} was moved to peg A'.format('m')
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format('m', disk, a1)
        knowledge.clear()
        goal.modify(action='think')

    #---------------------------------------Transfer Actions---------------------------------------------
    def transfer_ac1(goal='action:transfer', knowledge='next_disk:?disk in_tower:A', towers='A ?disk ? ? B ?b1 ?b2 ? C None ? ?'):
        towers.set('A None None None B {} {} None C {} None None'.format(b1, b2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [{},{}], peg C has disks [{}]'.format(b1, b2, disk)
        knowledge.clear()
        goal.modify(action='think')

    def transfer_ac2(goal='action:transfer', knowledge='next_disk:?disk in_tower:A', towers='A ?disk ? ? B ?b1 ? ? C ?c1!None None ?'):
        towers.set('A None None None B {} None None C {} {} None'.format(b1, c1, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [{}], peg C has disks [{},{}]'.format(b1, c1, disk)
        knowledge.clear()
        goal.modify(action='think')

    def transfer_ac3(goal='action:transfer', knowledge='next_disk:?disk in_tower:A', towers='A ?disk ? ? B ? ? ? C ?c1!None ?c2!None ?'):
        towers.set('A None None None B None None None C {} {} {}'.format(c1, c2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [], peg C has disks [{},{},{}]'.format(c1, c2, disk)
        knowledge.clear()
        goal.modify(action='think')

    def transfer_bc1(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ?a1 ?a2 ? B ?disk ? ? C None ? ?'):
        towers.set('A {} {} None B None None None C {} None None'.format(a1, a2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [{},{}], peg B has disks [], peg C has disks [{}]'.format(a1, a2, disk)
        knowledge.clear()
        goal.modify(action='think')

    def transfer_bc2(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ?a1 ? ? B ?disk ? ? C ?c1!None None ?'):
        towers.set('A {} None None B None None None C {} {} None'.format(a1, c1, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [{}], peg B has disks [], peg C has disks [{},{}]'.format(a1, c1, disk)
        knowledge.clear()
        goal.modify(action='think')

    def transfer_bc3(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ? ? ? B ?disk ? ? C ?c1!None ?c2!None ?'):
        towers.set('A None None None B None None None C {} {} {}'.format(c1, c2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [], peg C has disks [{},{},{}]'.format(c1, c2, disk)
        knowledge.clear()
        goal.modify(action='think')

model = SolveHanoi()
ccm.log_everything(model)
model.goal.set('action:init')
model.towers.set('A l None None B s None None C m None None')
model.run(),{}
            
      
