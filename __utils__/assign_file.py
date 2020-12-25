import sys, os, glob, shutil


def move_file(src, number, problem):
        # src 별로 파일 처리
    if src == "boj":
        move_boj()
    elif src == "programmers":
        move_programmers()
    else:
        move_others()


def parse(file):
    '''
    주어진 파일을 알맞은 이름으로 변경한 뒤 알맞은 폴더로 이동시킵니다.
    - file: [src_problem]으로 이루어진 파일명으로 src는 출처를, problem은 문제명을 뜻합니다.
    '''
    # src와 problem으로 분리
    try:
        src, number, problem = file.split('_')
    except:
        print("잘못된 파일 형식입니다. [src_problem] 형식으로 변경해주세요.")
        sys.exit()
    
    folder, new_name = move_file(src, number, problem)

    return folder, new_name


target = '*.py'
pyfiles = glob.glob(target)

print(parse.__doc__)
if pyfiles:
    for file in pyfiles:
        try:
            folder, new_name = parse(file)
            os.rename(file, new_name)
            shutil.move(new_name, folder)
        except:
            print()
else:
    print("현재 존재하는 py 파일이 없습니다.")

# 파일 이름 불러와서 분류하기
# Programmers, Boj, Python-For-Coding-Test로 분류
# 원하는 대로 하기
# *.py 파일이 없으면 stage에 올라가 있는 파일이 없다고 하기

