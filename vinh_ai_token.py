# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class VinhAIToken(gl.Contract):
    token_name: str
    token_symbol: str
    owner: Address
    # This variable stores the token's initial total supply
    total_supply: u256
    
    # Biến lưu trữ dữ liệu
    ai_prediction: str

    # Khởi tạo token
    def __init__(self, name: str, symbol: str):
        self.token_name = name
        self.token_symbol = symbol
        # Đã sửa thành cú pháp chuẩn của GenLayer:
        self.owner = gl.message.sender_address  
        self.total_supply = 1000000000  # Tổng cung 1 tỷ token
        self.ai_prediction = "Waiting for analysis..."

    # Hàm lấy thông tin cơ bản
    @gl.public.view
    # Standard view function to return contract details
    def get_token_info(self) -> str:
        return f"Token: {self.token_name} ({self.token_symbol}) - Total Supply: {self.total_supply}"

    # Hàm ghi dữ liệu on-chain (Tạo lịch sử hoạt động cho ví)
    @gl.public.write
    def update_market_insight(self, new_insight: str) -> None:
        self.ai_prediction = f"Insight: {new_insight}"

    # Hàm đọc kết quả
    @gl.public.view
    def get_ai_result(self) -> str:
        return self.ai_prediction
