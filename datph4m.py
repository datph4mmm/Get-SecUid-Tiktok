import requests
import re

def get_user_info(username):
    url = f'https://www.tiktok.com/@{username}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Referer': 'https://www.tiktok.com/',
    }
    
    # Gửi yêu cầu GET tới trang TikTok của người dùng
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Lấy nội dung HTML
        html_content = response.text
        
        # Sử dụng regex để tìm secUid và uniqueId trong HTML
        secuid_match = re.search(r'"secUid":"(.*?)"', html_content)
        id_match = re.search(r'"id":"(.*?)"', html_content)  # Thêm dòng này để tìm uniqueId

        secUid = secuid_match.group(1) if secuid_match else "Không tìm thấy secUid"
        uniqueId = id_match.group(1) if id_match else "Không tìm thấy uniqueId"
        
        return secUid, uniqueId
    else:
        return f"Lỗi {response.status_code} khi truy cập trang TikTok.", None

# Nhập username TikTok từ bàn phím
username = input("Nhập username TikTok: ")

# Gọi hàm get_user_info với username vừa nhập
secUid, uniqueId = get_user_info(username)

# Hiển thị kết quả
print(f"secUid của người dùng {username}: {secUid}")
print(f"ID của người dùng {username}: {uniqueId}")
