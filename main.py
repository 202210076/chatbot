from chatbot import SimpleChatBot # chatbot.py 파이썬 파일에서 SimpleChatBot Class 를 Loading

if __name__ == "__main__":
    # 챗봇 객체를 생성.
    chatbot = SimpleChatBot("ChatbotData.csv")

    # '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행.
    while True:
        question = input('You: ') # 입력 확인.

        if question.lower() == '종료':
            print('Chatbot: Chatbot을 종료합니다.')
            break
        answer = chatbot.answer(question)
        print('Chatbot:', answer)