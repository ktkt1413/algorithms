

# 생일 중복 문제

def test_birthday_problem():
    import random
    TRIALS = 100000
    same_birthdays = 0

    for _ in range(TRIALS):
        birthdays = []
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)

    print(f"{same_birthdays / TRIALS * 100}%")


if __name__ == "__main__":          # <- 파이썬 스크립트가 직접 실행될 때 해당 블록 안의 코드가 실행되도록 하는 관용적 코드
    test_birthday_problem()         #    단 다른 스크림트에 모듈로서 import되지 않았았을때 한정
    test_hashtable()