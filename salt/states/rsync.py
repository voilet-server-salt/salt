# -*- coding: utf-8 -*-
'''
=====================================================
Rsync files from sour to dest.

'''

def rsync(name,
          sour=None,
          dest=None,
          delete=False,
          force=False,
          update=False,
          passwordfile=None,
          exclude=None,
          excludefrom=None,
          ):
    '''
    rsync files to dest.

    name
        The id
 
    sour
        The source

    dest
        The destination

    delete
        add option: '--delete'

    update
        add option: '--update'

    passworfile
        add option: '--password-file'

    exclude
        add option: '--exclude'

    excludefrom
        add option: '--exclude-from'

    .. code-block:: yaml

        test:
          rsync.rsync:
            - sour: 10.0.0.1::code
            - dest: /tmp
            - delete: True
            - passwordfile: /etc/pass.crt 
    '''

    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': ''}

    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = ('rsync files from {0} to {1}'
                ).format(sour, dest)
        return ret

    out =  __salt__['rsync.rsync'](sour, dest, delete, force, update, passwordfile, exclude, excludefrom)
    if out['retcode' ] == 0:
        ret['comment'] = 'rsync files from {0} to {1}'.format(sour, dest)
    else:
        ret['comment'] = out['stderr']
        ret['result'] = False

    return ret
    

