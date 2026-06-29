# v0.2.16
# { "Depends": "py-genlayer" }

from genlayer import *

class VinhAIPredictionMarket(gl.Contract):
    market_title: str
    owner: Address
    ai_verdict: str
    is_resolved: bool

    def __init__(self, title: str):
        """
        Khởi tạo thị trường dự đoán với một chủ đề cụ thể.
        Ví dụ: "Will AI tokens outperform the general crypto market in Q3 2026?"
        """
        self.market_title = title
        self.owner = gl.message.sender
        self.ai_verdict = "Market is open. Pending real-world data for AI resolution."
        self.is_resolved = False

    @gl.public.write
    def resolve_market_with_ai(self, real_world_news_feed: str):
        """
        Hàm ghi dữ liệu: Gửi dữ liệu thực tế từ báo chí/on-chain vào để AI phân tích và đóng thị trường.
        Giao thức này kích hoạt các Validator LLM của GenLayer để đạt đồng thuận.
        """
        if self.is_resolved:
            return "Error: This market has already been resolved."
            
        # Hệ thống gọi tính năng xử lý ngôn ngữ tự nhiên của GenLayer Nodes
        prompt = (
            f"You are an decentralized AI Judge. Based strictly on this real-world data: '{real_world_news_feed}', "
            f"has the following prediction come true: '{self.market_title}'? "
            f"Provide a concise final verdict (YES, NO, or UNRESOLVED) and a brief 1-sentence justification."
        )
        
        # Lưu kết quả đồng thuận của AI vào trạng thái hợp đồng
        self.ai_verdict = gl.llm.query(prompt)
        self.is_resolved = True
        return "Market successfully resolved by GenLayer Subjective Consensus."

    @gl.public.view
    def get_market_status(self) -> str:
        """
        Hàm đọc dữ liệu: Kiểm tra trạng thái và phán quyết hiện tại của AI.
        """
        status_str = "RESOLVED" if self.is_resolved else "OPEN"
        return f"Market: {self.market_title} | Status: {status_str} | AI Verdict: {self.ai_verdict}"
