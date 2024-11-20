import ccm
from ccm.lib.actr import *
log=ccm.log()

class SolveHanoi(ACTR):
    towers = Buffer()
    goal = Buffer()
    knowledge = Buffer()

    #--------------------------------CHECKS IF GOAL WAS REACHED-------------------------------------------
    def completed(goal='action:check_completion', towers='A None None None B None None None C l m s'):
        goal.clear()

    def not_completed_c(goal='action:check_completion', towers='A ? ? ? B ? ? ? C ? ? None'):
        goal.modify(action='think')

    def wrong_c1(goal='action:check_completion', towers='A ? ? ? B ? ? ? C !l ? ?'):
        goal.modify(action='think')

    def wrong_c2(goal='action:check_completion', towers='A ? ? ? B ? ? ? C ? !m ?'):
        goal.modify(action='think')

    #--------------------------------CHECKS FOR CLEAN NEED--------------------------------------------------
    def c_needs_empty(goal='action:think', towers='A ? ? ? B ? ? ? C ?c1!l!None ? ?'):
        knowledge.set('clean_until:{} next_disk:l'.format(c1))
        goal.modify(action='clean')

    def c_needs_parcial_clean(goal='action:think', towers='A ? ? ? B ? ? ? C l ?c2!m!None ?'):
        knowledge.set('clean_until:{} next_disk:m'.format(c2))
        goal.modify(action='clean')

    def c_needs_no_clean_next_l(goal='action:think', towers='A ? ? ? B ? ? ? C None ? ?'):
        knowledge.set('next_disk:l')

    def c_needs_no_clean_next_m(goal='action:think', towers='A ? ? ? B ? ? ? C l None ?'):
        knowledge.set('next_disk:m')

    def c_needs_no_clean_next_s(goal='action:think', towers='A ? ? ? B ? ? ? C l m None'):
        knowledge.set('next_disk:s')

    #---------------------------------CHECKS FOR UNOBSTRUCTION NEED=============================
    def a_needs_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A ?disk !None ? B ? ? ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:A'.format(disk))
        goal.modify(action='unobstruct')

    def b_needs_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A ? ? ? B ?disk !None ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:B'.format(disk))
        goal.modify(action='unobstruct')

    def a_needs_partial_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A !None ?disk !None B ? ? ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:A'.format(disk))
        goal.modify(action='unobstruct')

    def b_needs_partial_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A ? ? ? B !None ?disk !None C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:B'.format(disk))
        goal.modify(action='unobstruct')

    def a1_no_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A ?disk None ? B ? ? ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:A'.format(disk))
        goal.modify(action='transfer')

    def a2_no_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A ? ?disk None B ? ? ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:A'.format(disk))
        goal.modify(action='transfer')

    def a3_no_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A ? ? ?disk B ? ? ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:A'.format(disk))
        goal.modify(action='transfer')

    def b1_no_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A ? ? ? B ?disk None ? C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:B'.format(disk))
        goal.modify(action='transfer')

    def b2_no_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A ? ? ? B ? ?disk None C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:B'.format(disk))
        goal.modify(action='transfer')

    def b3_no_unobstruction(goal='action:think', knowledge='next_disk:?disk', towers='A ? ? ? B ? ? ?disk C ? ? ?' ):
        knowledge.set('next_disk:{} in_tower:B'.format(disk))
        goal.modify(action='transfer')
    #---------------------------Clean Actions-----------------------------------------------------------------
    def clean_two_last(goal='action:clean', knowledge='clean_until:?until', towers='A ?a1 ?a2 ?a3 B ?b1 ?b2 ?b3 C l ?until ?c3!None'):
        towers.set('A {} None None B None None None C l {} None'.format(c3, until))
        print 'Disk {} was moved to peg A'.format(c3)
        print 'Peg A has disks [{}], peg B has disks [], peg C has disks [l,{}]'.format(c3, until)
        towers.set('A {} None None B {} None None C l None None'.format(c3, until))
        print 'Disk {} was moved to peg B'.format(until)
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [l]'.format(c3, until)
        goal.modify(action='think')

    def clean_all_l_second(goal='action:clean', knowledge='clean_until:?until', towers='A ?a1 ?a2 ?a3 B ?b1 ?b2 ?b3 C ?until l ?c3!None'):
        towers.set('A {} None None B None None None C {} l None'.format(c3, until))
        print 'Disk {} was moved to peg A'.format(c3)
        print 'Peg A has disks [{}], peg B has disks [], peg C has disks [l,{}]'.format(c3, until)
        towers.set('A {} None None B l None None C {} None None'.format(c3, until))
        print 'Disk l was moved to peg B'
        print 'Peg A has disks [{}], peg B has disks [l], peg C has disks [{}]'.format(c3, until)
        towers.set('A {} {} None B l None None C None None None'.format(c3, until))
        print 'Disk {} was moved to peg A'.format(until)
        print 'Peg A has disks [{},{}], peg B has disks [l], peg C has disks []'.format(c3, until)
        goal.modify(action='think')

    def clean_all_l_third(goal='action:clean', knowledge='clean_until:?until', towers='A ?a1 ?a2 ?a3 B ?b1 ?b2 ?b3 C ?until ?c2 l'):
        towers.set('A None None None B l None None C {} {} None'.format(until, c2))
        print 'Disk l was moved to peg B'
        print 'Peg A has disks [], peg B has disks [l], peg C has disks [{},{}]'.format(until, c2)
        towers.set('A {} None None B l None None C {} None None'.format(c2, until))
        print 'Disk {} was moved to peg A'.format(c2)
        print 'Peg A has disks [{}], peg B has disks [l], peg C has disks [{}]'.format(c2, until)
        towers.set('A {} {} None B l None None C None None None'.format(c2, until))
        print 'Disk {} was moved to peg B'.format(until)
        print 'Peg A has disks [{},{}], peg B has disks [l], peg C has disks []'.format(c2, until)
        goal.modify(action='think')

    def clean_two_first_to_b(goal='action:clean', knowledge='clean_until:?until', towers='A l ? ? B ? ? ? C ?until ?c2 None'):
        towers.set('A l None None B {} None None C {} None None'.format(c2, until))
        print 'Disk {} was moved to peg B'.format(c2)
        print 'Peg A has disks [l], peg B has disks [{}], peg C has disks [{}]'.format(c2, until)
        towers.set('A l None None B {} {} None C None None None'.format(c2, until))
        print 'Disk {} was moved to peg B'.format(until)
        print 'Peg A has disks [l], peg B has disks [{},{}], peg C has disks []'.format(c2, until)
        goal.modify(action='think')

    def clean_two_first_mixed_a(goal='action:clean', knowledge='clean_until:?until', towers='A ?a1!None!l ? ? B ? ? ? C ?until l None'):
        towers.set('A {} None None B l None None C {} None None'.format(a1, until))
        print 'Disk l was moved to peg B'
        print 'Peg A has disks [{}], peg B has disks [l], peg C has disks [{}]'.format(a1, until)
        towers.set('A {} {} None B l None None C None None None'.format(a1, until))
        print 'Disk {} was moved to peg A'.format(until)
        print 'Peg A has disks [{},{}], peg B has disks [l], peg C has disks []'.format(a1, until)
        goal.modify(action='think')

    def clean_two_first_mixed_b(goal='action:clean', knowledge='clean_until:?until', towers='A ? ? ? B ?b1!None!l ? ? C ?until l None'):
        towers.set('A l None None B {} None None C {} None None'.format(b1, until))
        print 'Disk l was moved to peg B'
        print 'Peg A has disks [l], peg B has disks [{}], peg C has disks [{}]'.format(b1, until)
        towers.set('A l None None B {} {} None C None None None'.format(b1, until))
        print 'Disk {} was moved to peg B'.format(until)
        print 'Peg A has disks [l], peg B has disks [{},{}], peg C has disks []'.format(b1, until)
        goal.modify(action='think')

    def clean_two_first_to_a(goal='action:clean', knowledge='clean_until:?until', towers='A ? ? ? B l ? ? C ?until ?c2 None'):
        towers.set('A {} None None B l None None C {} None None'.format(c2, until))
        print 'Disk {} was moved to peg A'.format(c2)
        print 'Peg A has disks [{}], peg B has disks [l], peg C has disks [{}]'.format(c2, until)
        towers.set('A {} {} None B l None None C None None None'.format(c2, until))
        print 'Disk {} was moved to peg A'.format(until)
        print 'Peg A has disks [{},{}], peg B has disks [l], peg C has disks []'.format(c2, until)
        goal.modify(action='think')

    def clean_first_to_a1(goal='action:clean', knowledge='clean_until:?until', towers='A None ? ? B ?b1 ?b2 ? C ?until None None'):
        towers.set('A {} None None B {} {} None C None None None'.format(until, b1, b2))
        print 'Disk {} was moved to peg A'.format(until)
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format(until,b1,b2)
        goal.modify(action='think')

    def clean_first_to_a2(goal='action:clean', knowledge='clean_until:?until', towers='A ?a1 ? ? B l None ? C ?until None None'):
        towers.set('A {} {} None B l None None C None None None'.format(a1, until))
        print 'Disk {} was moved to peg A'.format(until)
        print 'Peg A has disks [{},{}], peg B has disks [l], peg C has disks []'.format(a1,until)
        goal.modify(action='think')

    def clean_first_to_b1(goal='action:clean', knowledge='clean_until:?until', towers='A ?a1 ?a2 ? B None ? ? C ?until None None'):
        towers.set('A {} {} None B {} None None C None None None'.format(a1, a2, until))
        print 'Disk {} was moved to peg B'.format(until)
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format(a1,a2,until)
        goal.modify(action='think')

    def clean_first_to_b2(goal='action:clean', knowledge='clean_until:?until', towers='A l None ? B ?b1 ? ? C ?until None None'):
        towers.set('A l None None B {} {} None C None None None'.format(b1, until))
        print 'Disk {} was moved to peg B'.format(until)
        print 'Peg A has disks [l], peg B has disks [{},{}], peg C has disks []'.format(a1,until)
        goal.modify(action='think')
    #-------------------------- UNOBSTRUCTION ACTIONS------------------------------------------------------------
    def unobstruct_full_a_completely(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:A', towers='A ?disk ?a2 ?a3!None B ? ? ? C ? ? ?'):
        towers.set('A {} {} None B {} None None C None None None'.format(disk, a2, a3))
        print 'Disk {} was moved to peg B'.format(a3)
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format(disk, a2, a3)
        towers.set('A {} None None B {} {} None C None None None'.format(disk, a3, a2))
        print 'Disk {} was moved to peg B'.format(a2)
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format(disk, a3, a2)
        goal.modify(action='transfer')

    def unobstruct_full_a_partialy(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:A', towers='A ?a1 ?disk ?a3!None B ? ? ? C ? ? ?'):
        towers.set('A {} {} None B {} None None C None None None'.format(a1, disk, a3))
        print 'Disk {} was moved to peg B'.format(a3)
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format(a1, disk, a3)
        goal.modify(action='transfer')

    def unobstruct_partial_a_empty_c(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:A', towers='A ?disk ?a2 None B ?b1 ? ? C None ? ?'):
        towers.set('A {} None None B {} {} None C None None None'.format(disk, b1, a2))
        print 'Disk {} was moved to peg B'.format(a2)
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format(disk, b1, a2)
        goal.modify(action='transfer')

    def unobstruct_partial_a_empty_b(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:A', towers='A ?disk ?a2 None B None ? ? C ?c1 ? ?'):
        towers.set('A {} None None B {} None None C {} None None'.format(disk, a2, c1))
        print 'Disk {} was moved to peg B'.format(a2)
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format(disk, a2, c1)
        goal.modify(action='transfer')

    def unobstruct_full_b_completely(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:B', towers='A ? ? ? B ?disk ?b2 ?b3!None C ? ? ?'):
        towers.set('A {} None None B {} {} None C None None None'.format(b3, disk, b2))
        print 'Disk {} was moved to peg A'.format(b3)
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format(b3, disk, b2)
        towers.set('A {} {} None B {} None None C None None None'.format(b3, b2, disk))
        print 'Disk {} was moved to peg A'.format(b2)
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format(b3, b2, disk)
        goal.modify(action='transfer')

    def unobstruct_full_b_partialy(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:B', towers='A ? ? ? B ?b1 ?disk ?b3!None C ? ? ?'):
        towers.set('A {} None None B {} {} None C None None None'.format(b3, b2, disk))
        print 'Disk {} was moved to peg A'.format(b3)
        print 'Peg A has disks [{}], peg B has disks [{},{}], peg C has disks []'.format(b3, b2, disk)
        goal.modify(action='transfer')

    def unobstruct_partial_b_empty_c(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:B', towers='A ?a1 ? ? B ?disk ?b2 ? C None ? ?'):
        towers.set('A {} {} None B {} None None C None None None'.format(a1, b2, disk))
        print 'Disk {} was moved to peg A'.format(b2)
        print 'Peg A has disks [{},{}], peg B has disks [{}], peg C has disks []'.format(a1, b2, disk)
        goal.modify(action='transfer')

    def unobstruct_partial_b_empty_a(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:B', towers='A None ? ? B ?disk ?b2 ? C ?c1 ? ?'):
        towers.set('A {} None None B {} None None C {} None None'.format(b2, disk, c1))
        print 'Disk {} was moved to peg A'.format(b2)
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format(b2, disk, c1)
        goal.modify(action='transfer')

    #---------------------------------------Transfer Actions---------------------------------------------
    def transfer_a1c1(goal='action:transfer', knowledge='next_disk:?disk in_tower:A', towers='A ?disk ? ? B ?b1 ?b2 ? C None ? ?'):
        towers.set('A None None None B {} {} None C {} None None'.format(b1, b2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [{},{}], peg C has disks [{}]'.format(b1, b2, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_a1c2(goal='action:transfer', knowledge='next_disk:?disk in_tower:A', towers='A ?disk ? ? B ?b1 ? ? C ?c1!None None ?'):
        towers.set('A None None None B {} None None C {} {} None'.format(b1, c1, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [{}], peg C has disks [{},{}]'.format(b1, c1, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_a1c3(goal='action:transfer', knowledge='next_disk:?disk in_tower:A', towers='A ?disk ? ? B ? ? ? C ?c1!None ?c2!None ?'):
        towers.set('A None None None B None None None C {} {} {}'.format(c1, c2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [], peg C has disks [{},{},{}]'.format(c1, c2, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_a2c1(goal='action:transfer', knowledge='next_disk:?disk in_tower:A', towers='A ?a1 ?disk ? B ?b1 ? ? C None ? ?'):
        towers.set('A {} None None B {} None None C {} None None'.format(a1, b1, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format(b1, c1, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_a2c2(goal='action:transfer', knowledge='next_disk:?disk in_tower:A', towers='A ?a1 ?disk ? B ? ? ? C ?c1!None ? ?'):
        towers.set('A {} None None B None None None C {} {} None'.format(a1, c1, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [{}], peg B has disks [], peg C has disks [{},{}]'.format(a1, c1, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_a3c1(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ?a1 ?a2 ?disk B ? ? ? C ? ? ?'):
        towers.set('A {} {} None B None None None C {} None None'.format(a1, a2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [{},{}], peg B has disks [], peg C has disks [{}]'.format(a1, a2, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_b1c1(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ?a1 ?a2 ? B ?disk ? ? C None ? ?'):
        towers.set('A {} {} None B None None None C {} None None'.format(a1, a2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [{},{}], peg B has disks [], peg C has disks [{}]'.format(a1, a2, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_b1c2(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ?a1 ? ? B ?disk ? ? C ?c1!None None ?'):
        towers.set('A {} None None B None None None C {} {} None'.format(a1, c1, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [{}], peg B has disks [], peg C has disks [{},{}]'.format(a1, c1, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_b1c3(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ? ? ? B ?disk ? ? C ?c1!None ?c2!None ?'):
        towers.set('A None None None B None None None C {} {} {}'.format(c1, c2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [], peg C has disks [{},{},{}]'.format(c1, c2, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_b2c1(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ?a1 ? ? B ?b1 ?disk ? C None ? ?'):
        towers.set('A {} None None B {} None None C {} None None'.format(a1, b1, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [{}], peg B has disks [{}], peg C has disks [{}]'.format(a1, b1, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_b2c2(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ? ? ? B ?b1 ?disk ? C ?c1!None ? ?'):
        towers.set('A None None None B {} None None C {} {} None'.format(b1, c1, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [{}], peg C has disks [{},{}]'.format(b1, c1, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

    def transfer_b3c1(goal='action:transfer', knowledge='next_disk:?disk in_tower:B', towers='A ? ? ? B ?b1 ?b2 ?disk C ? ? ?'):
        towers.set('A None None None B {} {} None C {} None None'.format(b1, b2, disk))
        print 'Disk {} was moved to peg C'.format(disk)
        print 'Peg A has disks [], peg B has disks [{},{}], peg C has disks [{}]'.format(b1, b2, disk)
        knowledge.clear()
        goal.modify(action='check_completion')

model = SolveHanoi()
ccm.log_everything(model)
model.goal.set('action:think')
model.towers.set('A l m s B None None None C s m None')
model.run()
            
        
