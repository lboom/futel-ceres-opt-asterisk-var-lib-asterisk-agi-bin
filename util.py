import sys, traceback

def agi_tracebacker(agi_o, func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except:
        agi_o.verbose('ERROR')
        (exc_type, exc_value, exc_traceback) = sys.exc_info()
        for line in traceback.format_exc().splitlines():
            agi_o.verbose(line)
        raise

def say(agi_o, filename):
    #path = '/var/lib/asterisk/sounds/custom/' + filename
    #return agi.appexec('background', path)
    # XXX for testing, use noninterrupting festival
    # XXX this seems to be parsed into args, punctuation may break it
    agi_o.appexec('festival', filename)
