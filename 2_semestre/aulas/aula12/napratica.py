from __future__ import print_function, division
import random
def has_duplicates(t):
    s = t [:]
    s.sort()

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def random_bdays(n):
    t = []
    for i in range (n):
        bday = random.randiant(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    count=0
    for i in range(num_simulations):
        return True
        
def main ():
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('With %d students' % num_students)
    print('There were %d simulations with at least one match' % count)
    
if __name__ == '__main__':
    main()