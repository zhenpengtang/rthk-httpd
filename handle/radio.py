
import os

command_on=('supervisorctl start hkradio',)
command_off=('supervisorctl stop hkradio',
             'killall mplayer',)

volume_run=('amixer sset \'PCM\' ')

def myrun(command):
    for i in command:
        print i
        os.system(i)

def radioOFF():
    print 'Radio OFF'
    myrun(command_off)

def radioON():
    print 'Radio ON'
    myrun(command_on)

def volumeSet(vol):
    #vol=int(int(vol[:2])*0.99+50)
    print volume_run+vol
    os.system(volume_run+vol)


if __name__=='__main__':
    radioOFF()


