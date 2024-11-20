import ccm
from ccm.lib.actr import *
log=ccm.log()

class SolveHanoi(ACTR):
    towers = {'A':['l','m','s'],'B':[],'C':[]}
    print 'initial configuration:'
    print 'Peg A has disks {}, peg B has disks {}, peg C has disks {}'.format(towers['A'], towers['B'], towers['C'])
    c_goal = ['l','m','s','d']
    goal = Buffer()
    knowledge = Buffer()

    def check_completion(goal='action:check_completion'):
        if self.towers['C'] == self.c_goal[:3]:
            goal.clear()
        else:
            goal.modify(action='think')


    def think(goal='action:think'):
        c_len = len(self.towers['C'])
        need_clean = False
        clean_until = None
        in_tower=None
        next_disk='l'
        for i in range(c_len):
            if towers['C'][i]!=self.c_goal[i]:
                need_clean = True
                goal.modify(action='clean')
                clean_until = towers['C'][i]
                break
            next_disk=c_goal[i+1]
        for key in ['A','B']:
            if next_disk in towers[key]:
                in_tower = key
            else:
                discard_tower = key
        knowledge.set('next_disk:{} in_tower:{} discard_tower:{} clean_until:{}'.format(next_disk, in_tower, discard_tower, clean_until))
        if not need_clean:
            goal.modify(action='unobstruct')


    def clean(goal='action:clean', knowledge='clean_until:?disk next_disk:?next_disk discard_tower:?peg'):
        discard_tower = self.towers[peg]
        c_tower = self.towers['C']
        while c_tower:
            last_disk = c_tower[len(c_tower)-1]     
            c_tower.remove(last_disk)
            if last_disk == next_disk:
                self.towers['A'].append(last_disk)
                print 'Disk {} was moved to peg {}'.format(last_disk, 'A')
                knowledge.modify(in_tower='A')
            else:
                discard_tower.append(last_disk)
                print 'Disk {} was moved to peg {}'.format(last_disk, peg)
            print 'Peg A has disks {}, peg B has disks {}, peg C has disks {}'.format(self.towers['A'], self.towers['B'],self.towers['C'])
            if last_disk == disk:
                break
        goal.modify(action='unobstruct')

    def unobstruct(goal='action:unobstruct', knowledge='next_disk:?disk in_tower:?key discard_tower:?peg'):
        discard_tower = self.towers[peg]
        in_tower = self.towers[key]
        if in_tower:
            while True:
                last_disk = in_tower[len(in_tower)-1]        
                if last_disk == disk:
                    break
                else:
                    in_tower.remove(last_disk)
                    discard_tower.append(last_disk)
                    print 'Disk {} was moved to peg {}'.format(last_disk, peg)
                    print 'Peg A has disks {}, peg B has disks {}, peg C has disks {}'.format(self.towers['A'], self.towers['B'],self.towers['C'])
        goal.modify(action='transfer')

    def transfer(goal='action:transfer', knowledge='next_disk:?disk in_tower:?key'):
        del self.towers[key][-1]
        self.towers['C'].append(disk)
        print 'Disk {} was moved to peg {}'.format(disk, 'C')
        print 'Peg A has disks {}, peg B has disks {}, peg C has disks {}'.format(self.towers['A'], self.towers['B'],self.towers['C'])
        knowledge.clear()
        goal.modify(action='check_completion')


model = SolveHanoi()
ccm.log_everything(model)
model.goal.set('action:think')
model.run()
            
        
