import requests


def text_to_handwriting(text, filename):
	data = requests.get(f"https://pywhatkit.herokuapp.com/handwriting?text={str(text)}&rgb=0,1,2").content
	with open(filename, 'wb') as file:
		file.write(data)
		file.close()
	return filename
if __name__ == '__main__':
	text_to_handwriting("hello world", "test.jpg")
