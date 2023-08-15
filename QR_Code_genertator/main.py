# % pip install -r requirements.txt
import qrcode

class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size = size, border = padding)


    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input('Enter your text: ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color = fg, back_color= bg)
            qr_image.save(file_name)

            print(f'QR code has been created ({file_name})')
        except Exception as exc:
            print(f'Error: {exc}')


def main():
    myqrcode = MyQR(size=40, padding=2)
    myqrcode.create_qr('Output_QRCode.png', fg='black', bg='white')

if __name__ == '__main__':
    main()