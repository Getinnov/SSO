from Model.auth import *
from Model.user import *
from Model.registery import *

def setuproute(app, call):
    @app.route('/',                             ['OPTIONS', 'GET'],         lambda x = None: call([origin_check])) #done

    @app.route('/signup',                       ['OPTIONS', 'POST'],        lambda x = None: call([user_register, user_get_token])) #done
    @app.route('/signin',                       ['OPTIONS', 'POST'],        lambda x = None: call([user_login, user_get_token])) #done
    @app.route('/token',                        ['OPTIONS', 'GET'],         lambda x = None: call([user_verify_token, user_get_token])) #done

    @app.route('/user',                         ['OPTIONS', 'GET'],         lambda x = None: call([user_verify_token, user_infos])) #done
    @app.route('/user',                         ['OPTIONS', 'PUT'],         lambda x = None: call([user_verify_token, user_update])) #done
    @app.route('/user',                         ['OPTIONS', 'DELETE'],      lambda x = None: call([user_verify_token, user_disable])) #done
    @app.route('/user/invite',                  ['OPTIONS', 'POST'],        lambda x = None: call([user_verify_token, user_invite])) #done
    @app.route('/user/<>',                      ['OPTIONS', 'GET'],         lambda x = None: call([user_verify_token, user_infos])) #done
    @app.route('/user/<>/role',                 ['OPTIONS', 'GET'],         lambda x = None: call([user_verify_token, user_role])) #done
    @app.route('/user/<>/role',                 ['OPTIONS', 'POST'],        lambda x = None: call([user_verify_token, user_is_admin, user_set_role])) #done

    @app.route('/registeries/<>/key/<>/signin', ['OPTIONS', 'POST'],        lambda x = None: call([user_verify_token, user_get_token])) #done

    @app.route('/registery',                    ['OPTIONS', 'GET'],         lambda x = None:call([user_verify_token, ]))
    @app.route('/registery',                    ['OPTIONS', 'POST'],        lambda x = None:call([user_verify_token, user_is_admin, regi_create]))
    @app.route('/registery/<>/roles',           ['OPTIONS', 'GET'],         lambda x = None:call([user_verify_token,]))
    @app.route('/registery/<>/roles',           ['OPTIONS', 'POST'],        lambda x = None:call([user_verify_token,]))
    @app.route('/registery/<>/roles',           ['OPTIONS', 'DELETE'],      lambda x = None:call([user_verify_token,]))

    @app.route('/registery/<>/actions',           ['OPTIONS', 'GET'],         lambda x = None:call([user_verify_token,]))
    @app.route('/registery/<>/actions',           ['OPTIONS', 'POST'],        lambda x = None:call([user_verify_token,]))
    @app.route('/registery/<>/actions',           ['OPTIONS', 'DELETE'],      lambda x = None:call([user_verify_token,]))

    @app.route('/extern/key',                   ['OPTIONS', 'GET'],         lambda x = None: call([user_get_key])) #done
    @app.route('/extern/key/<>/token',          ['OPTIONS', 'POST'],        lambda x = None: call([user_wait_token])) #done

    @app.route('/password/reset',               ['OPTIONS', 'POST'],        lambda x = None: call([user_verify_token])) #done not imp
    @app.route('/password/change',              ['OPTIONS', 'POST'],        lambda x = None: call([user_verify_token])) # done not imp

    @app.route('/card',                         ['OPTIONS', 'GET'],         lambda x = None: call([user_verify_token]))
    @app.route('/card',                         ['OPTIONS', 'POST'],        lambda x = None: call([user_verify_token]))
    @app.route('/card/<>',                      ['OPTIONS', 'GET'],         lambda x = None: call([user_verify_token]))
    @app.route('/card/<>',                      ['OPTIONS', 'DELETE'],      lambda x = None: call([user_verify_token]))

    @app.route('/order/',                       ['OPTIONS', 'POST'],        lambda x = None: call([user_verify_token]))
    @app.route('/orderdetail/',                 ['OPTIONS', 'POST'],        lambda x = None: call([user_verify_token]))
    @app.route('/history/',                     ['OPTIONS', 'GET'],         lambda x = None: call([user_verify_token]))
    @app.route('/payments/',                    ['OPTIONS', 'GET'],         lambda x = None: call([user_verify_token]))
    @app.route('/paymentdetails/',              ['OPTIONS', 'POST'],        lambda x = None: call([user_verify_token]))
    def base():
        return
