from tkinter import *
import random

answer = random.randint(1,100)
count = 0

def guessing():
    global answer
    global count
    guess = int(guessField.get())
    count = count + 1

    if guess > answer:
        msg = f"높음! {10-count}번 기회가 남았습니다."
    elif guess < answer:
        msg = f"낮음! {10-count}번 기회가 남았습니다."
    else:
        msg = "정답!"
    
    resultLabel["text"] = msg
    guessField.delete(0, 5)


    if count == 10:
        resultLabel["text"] = f"실패! 정답은 {answer} 입니다. 숫자를 초기화 합니다."
        answer = random.randint(1, 100)
        count = 0

def reset():
    global answer
    answer = random.randint(1, 100)
    resultLabel["text"] = "다시 한번 하세요!"

window = Tk()
window.configure(bg="white")
window.title("숫자를 맞춰보세요!")
window.geometry("500x80")

titleLabel = Label(window, text="숫자게임에 오신것을 환영합니다", bg = "white")
titleLabel.pack() 

guessField = Entry(window)
guessField.pack(side="left")
tryButton = Button(window, text="시도", fg="green", bg="white", command=guessing)
tryButton.pack(side="left")

resetButton = Button(window, text="초기화", fg="red", bg="white", command=reset)
resetButton.pack(side="left")
resultLabel = Label(window, text="1부터 100사이의 숫자를 입력하시오", bg="white")
resultLabel.pack(side="left")

window.mainloop()


