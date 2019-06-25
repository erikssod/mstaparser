import numpy as np

class MSTA():

    def __init__(self,val):
        assert(type(val)==int)
        assert(val>0)
        self.val = val

        self.MSTA = {
        'DIRECTION':1,
        'DONE':2,
        'PLUS_LS':3,
        'HOMELS':4,
        'Unused':5,
        'POSITION':6,
        'SLIP_STALL':7,
        'HOME':8,
        'PRESENT':9,
        'PROBLEM':10,
        'MOVING':11,
        'GAIN_SUPPORT':12,
        'COMM_ERR':13,
        'MINUS_LS':14,
        'HOMED':15}

    def check(self,PV):
        key = self.MSTA[PV]
        bitkey = len(self.MSTA)  - key
        string = np.binary_repr(self.val)
        bit = int(string[bitkey])
        return bit

    @property
    def direction(self):
        return self.check('DIRECTION')

    @property
    def done(self):
        return self.check('DONE')

    @property
    def plus_ls(self):
        return self.check('PLUS_LS')

    @property
    def homels(self):
        return self.check('HOMELS')

    @property
    def unused(self):
        return self.check('Unused')

    @property
    def position(self):
        return self.check('POSITION')

    @property
    def slip_stall(self):
        return self.check('SLIP_STALL')

    @property
    def home(self):
        return self.check('HOME')

    @property
    def present(self):
        return self.check('PRESENT')

    @property
    def problem(self):
        return self.check('PROBLEM')

    @property
    def moving(self):
        return self.check('MOVING')

    @property
    def gain_support(self):
        return self.check('GAIN_SUPPORT')

    @property
    def comm_err(self):
        return self.check('COMM_ERR')

    @property
    def minus_ls(self):
        return self.check('MINUS_LS')

    @property
    def homed(self):
        return self.check('HOMED')


