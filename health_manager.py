import pymysql
from pymysql.cursors import Cursor

# db 연결하는 함수
def get_db_connection() -> pymysql.Connection:
    try:
        return pymysql.connect(
            host="localhost",
            port=3307,
            user="root",
            password='1234',
            database='health_db'
        )
    except Exception as e:
        print(f"데이터베이스 연결 실패: {e}")
        exit(1)

def add_record(cursor: Cursor):
    """건강 기록 추가"""
    try:
        height = int(input("키(cm):"))
        weight = int(input("몸무게(kg)"))
        memo = input("메모(선택사항):")

        sql = """
            INSERT INTO health_records (height, weight, memo)
            VALUE (%s,%s,%s)
        """

        cursor.execute(sql, (height, weight, memo if memo else None))
        print("건강 기록이 추가되었습니다.")
    except ValueError:
        print("키와 몸무게는 숫자로 입력해 주세요.")
    except Exception as e :
        print(f"기록 추가 중 오류 발생: {e}")


def get_records(cursor: Cursor):
    sql = "SELECT id, height,weight,memo,created_at FROM health_records ORDER BY created_at DESC "

    cursor.execute(sql)

    records = cursor.fetchall()

    if not records:
        print("등록된 건강 기록이 없습니다.")
        return []
    
    print("\n===건강 기록 목록 ===")
    for record in records:
        id,height,weight,memo,created_at =record

        print(f'\n[ID: {id}] 기록일시 {created_at}')
        print(f"    키: {height}cm, 몸무게: {weight}kg")
        if memo:
            print(f"    메모: {memo}")
    print()
    return records

def update_record(cursor: Cursor):
    try:
        id = int(input("수정할 기록의 ID : "))

        new_height = int(input(f'새 키 (cm)'))
        new_weight = int(input("f'새 몸무게(kg)"))
        new_memo = input(f'새 메모')

        sql = """
            UPDATE health_records SET height = %s, weight = %s, memo =%s WHERE id =%s
            """
        cursor.excute(sql,(new_height, new_weight, new_memo, id))
        print("건강 기록이 수정되었습니다")
    except ValueError:
        print("id, 키, 몸무게는 숫자입니다")
    except Exception as e:
        print(f'기록 수정 중 오류')    

def delete_record(cursor: Cursor):
    raise Exception("함수 미구현")

def show_menu() -> str:
    """메뉴 표시"""
    print("\n=== 건강 관리 프로그램 ===")
    print("1. 건강 기록 추가")
    print("2. 건강 기록 조회")
    print("3. 건강 기록 수정")
    print("4. 건강 기록 삭제")
    print("5. 종료")
    return get_user_choice()

def get_user_choice() -> str:
    """사용자 선택 입력"""
    return input("\n선택: ")

def main():
    """메인 함수"""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        while True:
            choice = show_menu()

            if choice == "1":
                add_record(cursor)
                conn.commit()
            elif choice == "2":
                get_records(cursor)
            elif choice == "3":
                update_record(cursor)
                conn.commit()
            elif choice == "4":
                delete_record(cursor)
                conn.commit()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("올바른 메뉴를 선택해주세요.")

    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()
