import os

for i in range(1000, 17300, 100):
    try:
        if not(os.path.isdir(f'{i} - {i+99}')):
            os.makedirs(os.path.join(f'{i} - {i+99}'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print('폴더가 이미 존재합니다.')
            raise