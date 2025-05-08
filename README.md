# Ứng dụng Nhận Diện Xe Hơi

Ứng dụng này sử dụng deep learning để nhận diện các loại xe hơi khác nhau từ hình ảnh. Hiện tại, ứng dụng có thể nhận diện 4 loại xe:
- Sedan
- Sports Car
- SUV
- Truck

## Cài đặt

### Windows

1. Cài đặt Python:
   - Tải Python từ [python.org](https://www.python.org/downloads/)
   - Khi cài đặt, nhớ chọn "Add Python to PATH"
   - Khuyến nghị sử dụng Python 3.8 trở lên

2. Mở Command Prompt (cmd) hoặc PowerShell:
   - Nhấn Windows + R
   - Gõ "cmd" hoặc "powershell" và nhấn Enter

3. Clone repository này về máy của bạn:
```bash
git clone <repository-url>
cd <repository-folder>
```

4. Cài đặt các thư viện cần thiết:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### macOS/Linux

1. Clone repository này về máy của bạn
2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Cấu trúc thư mục

```
.
├── README.md
├── requirements.txt
├── app.py
├── best_model.h5
└── dataset/
    └── train/
        ├── sedan/
        ├── sports_car/
        ├── suv/
        └── truck/
```

## Sử dụng

### Windows

1. Khởi chạy ứng dụng:
   - Mở Command Prompt hoặc PowerShell
   - Di chuyển đến thư mục chứa ứng dụng:
   ```bash
   cd đường\dẫn\đến\thư\mục\ứng\dụng
   ```
   - Chạy ứng dụng:
   ```bash
   streamlit run app.py
   ```

2. Mở trình duyệt và truy cập địa chỉ được hiển thị (thường là http://localhost:8501)

3. Sử dụng ứng dụng:
   - Upload một ảnh xe (định dạng jpg, jpeg, hoặc png)
   - Nhấn nút "Predict"
   - Xem kết quả dự đoán với xác suất và thông tin về loại xe

### macOS/Linux

1. Khởi chạy ứng dụng:
```bash
streamlit run app.py
```

2. Mở trình duyệt và truy cập địa chỉ được hiển thị (thường là http://localhost:8501)

3. Sử dụng ứng dụng:
   - Upload một ảnh xe (định dạng jpg, jpeg, hoặc png)
   - Nhấn nút "Predict"
   - Xem kết quả dự đoán với xác suất và thông tin về loại xe

## Xử lý lỗi thường gặp trên Windows

1. Lỗi "python not found":
   - Kiểm tra lại việc cài đặt Python và PATH
   - Thử sử dụng lệnh `py` thay vì `python`

2. Lỗi khi cài đặt thư viện:
   - Cập nhật pip: `python -m pip install --upgrade pip`
   - Cài đặt Visual C++ Build Tools nếu cần

3. Lỗi khi chạy Streamlit:
   - Đảm bảo đã cài đặt đúng phiên bản Streamlit
   - Thử chạy với quyền Administrator

## Tính năng

- Nhận diện 4 loại xe phổ biến
- Hiển thị top 3 dự đoán với xác suất
- Cung cấp thông tin chi tiết về loại xe được dự đoán
- Giao diện thân thiện với người dùng

## Yêu cầu hệ thống

- Python 3.8 trở lên
- RAM: tối thiểu 4GB
- GPU: không bắt buộc nhưng được khuyến nghị để tăng tốc độ dự đoán
- Windows 10 trở lên (cho Windows)