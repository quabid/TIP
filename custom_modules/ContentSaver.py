import os


def save(content, name="file", ext=".txt", location=os.environ['HOME']):
    if content:
        try:
            f = open("{}{}{}{}".format(location, os.sep, name, ext),
                     "wb").write(content)
            return {'status': True, 'data': f}
        except OSError as ose:
            print(ose)
            return {'status': False, 'error': ose}
