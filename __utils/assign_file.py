import os, glob, shutil

def parse(file):
    '''
    file: [src_problem]으로 이루어진 파일명
        - src: 알고리즘 문제 출처 (boj, programmers, pfct 중 하나)
        - problem: 문제 이름 (boj는 [숫자_문제명], programmers는 [레벨_문제명])
    '''
    # src와 problem으로 분리

    # src 별로 파일 처리

    return folder, new_name

target = '*.py'
pyfiles = glob.glob(target)

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

