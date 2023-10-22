f = open("paragraph.docx", "w")
f.write("""Here is a comprehension passage for class 4 with normal questions as well as their answers.

Passage: The sun is the star at the center of our solar system. It is a huge ball of hot gas that gives off light and heat. The sun is about 150 million kilometers away from Earth. It takes about eight minutes for the sunlight to reach us. The sun has a diameter of about 1.4 million kilometers, which is more than 100 times bigger than Earth's diameter. The sun rotates on its axis, but not at the same speed everywhere. The equator of the sun spins faster than the poles. One rotation at the equator takes about 25 days, while one rotation at the poles takes about 36 days.

Questions:
1) What is the sun?
2) How far is the sun from Earth?
3) How long does it take for the sunlight to reach us?
4) How big is the sun compared to Earth?
5) How does the sun rotate on its axis?

Answers:
1) The sun is the star at the center of our solar system.
2) The sun is about 150 million kilometers away from Earth.
3) It takes about eight minutes for the sunlight to reach us.
4) The sun has a diameter of about 1.4 million kilometers, which is more than 100 times bigger than Earth's diameter.
5) The sun rotates on its axis, but not at the same speed everywhere. The equator of the sun spins faster than the poles.""")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()