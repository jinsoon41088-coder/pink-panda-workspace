questions = [
    {
        "question": "Python에서 화면에 글자를 출력하는 함수는?",
        "options": ["input()", "print()", "len()", "type()"],
        "answer": 2
    },

    {
        "question": "Python에서 사용자 입력을 받는 함수는?",
        "options": ["print()", "len()", "input()", "type()"],
        "answer": 3
    },
    {
        "question": "Python에서 문자열의 길이를 구하는 함수는?",
        "options": ["print()", "input()", "type()", "len()"],
        "answer": 4
    },
    {
        "question": "Python에서 정수를 나타내는 자료형은?",
        "options": ["str", "float", "int", "bool"],
        "answer": 3
    },
    {
        "question": "Python에서 반복 작업을 수행할 때 사용하는 키워드는?",
        "options": ["if", "for", "def", "return"],
        "answer": 2
    }
]
while True:



    print("=" * 40)
    print("🐼 핑크판다 파이썬 퀴즈 게임 🐼")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 최고 점수 확인")
    print("5. 종료")
    print("=" * 40)

    choice = input("메뉴 번호를 입력하세요: ").strip()
    
    if choice == "1":
       
        print("퀴즈 풀기를 선택했습니다.")
        score = 0
        for question in questions:
            print(question["question"])
            for number, option in enumerate(question["options"], start=1):
             print(f"{number}. {option}")
            answer = input("정답 번호를 입력하세요 (1~4): ")
            if answer == str(question["answer"]):
                 print("🎉 정답입니다!")
                 score += 1
            else:
                print("❌ 오답입니다!") 
        print(f"🐼 퀴즈 종료! 총 {len(questions)}문제 중 {score}문제를 맞혔습니다!")
    elif choice == "2":
        print("퀴즈 추가를 선택했습니다.")
        new_question = input("새로운 퀴즈 문제를 입력하세요: ")
        new_options = []
        for i in range(4):
                     option = input(f"{i + 1}번 보기를 입력하세요: ")
                     new_options.append(option)
        new_answer = int(input("정답 번호를 입력하세요 (1~4): "))
        questions.append({
            "question": new_question,
            "options": new_options,
            "answer": new_answer
        })
        print("🎉 새로운 퀴즈가 추가되었습니다!") 
    elif choice == "3":
        print("퀴즈 목록을 선택했습니다.")
        for number, question in enumerate(questions, start=1):
            print(f"{number}. {question['question']}")
            for option_number, option in enumerate(question["options"], start=1):
             print(f"{option_number}. {option}")
            print("-" * 30)
    elif choice == "4":
        print("최고 점수 확인을 선택했습니다.")
    elif choice == "5":
        print("게임을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")
         