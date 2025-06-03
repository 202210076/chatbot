import pandas as pd # pandas 패키지 Loading (pip install pandas)
from Levenshtein import distance # python-Levenshtein 패키지에서 Levenshtein 거리 함수를 Loading (pip install python-Levenshtein)

# 챗봇 객체 정의
class SimpleChatBot:
    """
        SimpleChatBot 클래스는 Q(Question), A(Answer) 가 있는 CSV 파일을 Parsing 하여 Input 질문에 대한 가장 유사한 A(Answer) 를 제공

        Attributes:
            _data (list): csv 파일의 Q, A 값에 대한 list

        Method:
            answer(question: str) -> str: 입력된 질문과 CSV에서 불러온 모든 질문의 Levenshtein 거리를 계산하여 가장 유사한 질문의 답변을 반환 (문자열 return).
    """
    def __init__(self, file="ChatbotData.csv"):
        """
        질문과 답변이 있는 csv 파일을 Loading 각각 Q(질문), A(답변)을 리스트 형태로 저장
        해당 맴버 변수는 Private Member 변수로 외부 에서 값을 수정할 수 없도록 처리
        :param self: SimpleChatBot. 객체
        :param file: 질문과 답변이 있는 csv 파일 경로 (기본값 "ChatbotData.csv")
        """
        self._data = pd.read_csv(file)[['Q', 'A']].values.tolist()

    def answer(self, question: str) -> str:
        """
        입력된 질문과 CSV에서 불러온 모든 질문의 Levenshtein 거리를 계산하여 가장 유사한 질문의 답변을 반환.
        :param self: SimpleChatBot. 객체
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
                minDistance = currentDistance  # 최소 거리를 갱신합니다.
                bestAnswer = A                 # 해당 질문의 답변을 최적 답변으로 저장.
        # 모든 쌍을 비교한 후, 최적의 답변을을 반환
        return bestAnswer