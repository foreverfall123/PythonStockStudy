class MarketDB:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목 코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='investar', charset='utf8' )
        self.codes = {}
        self.get_comp_info()

    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.conn.close()

    def get_comp_info(self):
        """company_info 테이블에서 읽어와서 codes에 저장"""

    def get_daily_price(self, code, start_date=None, end_date=None):
        """KRX 종목별 시세를 데이터 프레임 형태로 변환"""
