questions = (
("1. Menu minuman yang berwarna hijau bernama?"),
("2. Negara yang akan dikunjungi Sana adalah?"),
("3. Nama tumbuhan yang seluruh bagian bisa dimanfaatkan adalah?"),
("4. Alat pernapasan manusia apa?")
)

options = (
("A. Teh", "B. Kopi", "C. Susu", "D. Matcha"),
("A. Malaysia", "B. Switzerland", "C. Inggris", "D. London"),
("A. Kelapa", "B. Apel", "C. mangga", "D. anggur"),
("A. Paru-paru", "B. Insang", "C. Kaki", "D. omnivora"),
)

answer = ["D", "B", "A", "A"]
question_num = 0
score = 0
guesses = []

for question in questions:
    print("=================")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ")
    guesses.append(guess)
    if guess.upper() == answer[question_num]:
        score += 1
        print("Good! Right answer")
    else:
        print("Wrong answer")
    question_num += 1
    
score = int(((score) / (len(questions))) * 100)

print("\n=================")
print(f"Your score is {score}%")