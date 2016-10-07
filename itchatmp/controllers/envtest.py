import socket

from itchatmp.exceptions import ItChatEnvException

PYCRYPTO_WARNING = '''
pycrypto is not installed correctly.
* If you are using OSX or linux
    - you may uninstall and reinstall it use sudo
* If you are using Windows
    - you may uninstall and reinstall it in admin
    - you may change %PYTHONPATH%\\site-packages\\crypto
        to %PYTHONPATH%\\site-packages\\Crypto
* If they didn't work for you
    - contact me through i7meavnktqegm1b@qq.com
    - or through github.com/littlecodersh/
    - or report an issue \
'''
PORT_WARNING = 'port 80 is in use.'

def env_test():
    try:
        from Crypto.Cipher import AES
    except:
        raise ItChatEnvException(PYCRYPTO_WARNING)
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 80))
        s.listen(1)
        s.close()
    except:
        raise ItChatEnvException(PORT_WARNING)