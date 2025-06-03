# 고려사이버대학교 AI 개발 실무 14주차 과제

## Levenshtein 거리를 이용한 챗봇 구현
* 학습 데이터 셋 출처: (https://github.com/songys/Chatbot_data)

## 사용 Library
* pandas==2.2.3
* python-Levenshtein==0.27.1

## Library 설치 
~~~
pip install -r requirements.txt
~~~

## 구현
### chatbot.py (Module 형태)
~~~ python
import pandas as pd # pandas 패키지 Loading (pip install pandas)
from Levenshtein import distance # python-Levenshtein 패키지에서 Levenshtein 거리 함수를 Loading (pip install python-Levenshtein)

# 챗봇 객체 정의
class SimpleChatBot:
"""
    SimpleChatBot 클래스는 Q(Question), A(Answer) 가 있는 CSV 파일을 Parsing 하여 Input 질문에 대한 가장 유사한 A(Answer) 를 제공.

    Attributes:
        _data (list): csv 파일의 Q, A 값에 대한 list

    Method:
        answer(question: str) -> str: 입력된 질문과 CSV에서 불러온 모든 질문의 Levenshtein 거리를 계산하여 가장 유사한 질문의 답변을 반환. (문자열 return)
"""
def __init__(self, file="ChatbotData.csv"):
    """
    질문과 답변이 있는 csv 파일을 Loading 각각 Q(질문), A(답변)을 리스트 형태로 저장.
    해당 맴버 변수는 Private Member 변수로 외부 에서 값을 수정할 수 없도록 처리.
    :param self: SimpleChatBot 객체
    :param file: 질문과 답변이 있는 csv 파일 경로 (기본값 "ChatbotData.csv")
    """
    self._data = pd.read_csv(file)[['Q', 'A']].values.tolist()

def answer(self, question: str) -> str:
    """
    입력된 질문과 CSV에서 불러온 모든 질문의 Levenshtein 거리를 계산하여 가장 유사한 질문의 답변을 반환.
    :param self: SimpleChatBot 객체
    :param question: 사용자가 입력한 질문 (str)
    :return: 가장 유사한 답변 (str)
    """
    minDistance = float('inf')        # 최소 편집 거리를 무한대로 초기화.
    bestAnswer = None                 # 가장 유사한 답변을 저장할 변수를 초기화.

    # 모든 질문-답변 쌍을 순회하며 입력값과의 Levenshtein 거리를 계산.
    for Q, A in self._data:
        # 입력 질문과 현재 질문의 Levenshtein 거리(편집 거리)를 계산.
        currentDistance = distance(question, Q)
        # 만약 현재 거리가 지금까지의 최소 거리보다 작다면,
        if currentDistance < minDistance:
            minDistance = currentDistance  # 최소 거리를 갱신.
            bestAnswer = A                 # 해당 질문의 답변을 최적 답변으로 저장.
    # 모든 쌍을 비교한 후, 최적의 답변을 반환.
    return bestAnswer
~~~

### main.py (Excute)
~~~ python
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
~~~

## 실행
~~~
python main.py
~~~