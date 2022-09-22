from collections import Counter
import platform, time


def readthecss(filename):
    try:
        checks = [True if '.css' in filename else False]
        if checks:
            with open(filename,'r') as the_read:
                okey = [that.strip('\n') for that in the_read]
            return okey
        else:
            return checks
    except Exception as err:
        print('file not found or missing !!')


def collector(thenames):
    okeys = []
    taga = []
    count = 0
    for z in [x.strip() for x in readthecss(thenames) if ':' in x]:
        count += 1
        (a,b) = z.split(':',maxsplit=1)
        okeys.append((a,b.strip())); taga.append(''.join('%s' % jj for jj in a if '.' not in a if '#' not in a))
        pp = {y + ' - ' + str(sum(Counter([z for k,z in okeys if y in k]).values())) + ' lnofcode': [z for k,z in okeys if y in k] for k,z in okeys for y in [taga[jhg] for jhg in range(0,len(taga)) if len(taga[jhg]) > 1] if y in k}
    return pp



def make_txt(those,filename):
    with open(filename,'w') as pp:
        for k,v in those.items():
            print('-' * 32,file=pp)
            print(k,file=pp)
            print('-' * 32,file=pp)
            print(''.join('%s \n' % z for z in v),file=pp)


def css_reporter(a,b='css_complete_report.txt'):
    make_txt(collector(a),b)
    time.sleep(2)
    print(' \n', 
            'Hello ' + platform.node() + ' !! \n',
            '    successfully created a complete report about your css file \n','    file name - ' +  b + ' \n \n',
            '------thank you for using cssreporter :)-----------------------------'
        )



